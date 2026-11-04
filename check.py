#!/usr/bin/env python3
"""Build, run, verify, and remove every XBEN benchmark quietly."""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path


ROOT = Path(__file__).resolve().parent
BENCHMARKS = ROOT / "benchmarks"
FLAG_PATTERN = re.compile(r"FLAG\{[^}\r\n]+\}")


def make(benchmark: Path, target: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["make", "-C", str(benchmark), target],
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )


def check(benchmark: Path) -> bool:
    # `run` depends on the common.mk `build` target. Always call `down`, even
    # after a failed build, startup, or PoC, so one failed benchmark cannot
    # affect the next one.
    started = make(benchmark, "run")
    try:
        result = make(benchmark, "poc") if started.returncode == 0 else started
    finally:
        make(benchmark, "down")

    flag = FLAG_PATTERN.search(result.stdout)
    if result.returncode == 0 and flag:
        print(f"{benchmark.name} : {flag.group(0)}")
        return True

    print(f"{benchmark.name} : faild")
    return False


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "-j", "--jobs", type=int, default=1, metavar="N",
        help="how many benchmarks to build/run/exploit in parallel "
             "(default: 1 = sequential, the original behaviour). Each job is an "
             "independent Docker Compose project with ephemeral host ports, so "
             "different benchmarks never collide; raising N trades host "
             "CPU/RAM/IO and Docker build+boot contention for wall-clock time.",
    )
    args = parser.parse_args()
    workers = max(1, args.jobs)

    benchmarks = sorted(BENCHMARKS.glob("XBEN-*-24"))

    if workers == 1:
        # Sequential: preserves the original ordering and output exactly.
        results = [check(benchmark) for benchmark in benchmarks]
    else:
        # Each check() builds/runs/exploits/tears down one isolated project and
        # prints its own one-line result, so lines stay intact though their
        # order now follows completion, not the sorted list.
        with ThreadPoolExecutor(max_workers=workers) as pool:
            futures = [pool.submit(check, benchmark) for benchmark in benchmarks]
            results = [future.result() for future in as_completed(futures)]

    return 0 if results and all(results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
