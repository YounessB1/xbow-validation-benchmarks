# Runnable XBOW PoCs

Each `XBEN-*.md` file explains the vulnerability, its exploit chain, the
observed output, and remediation context.  The captured port and flag in a
guide are historical examples only: Docker publishes a fresh port every run
and the flag can be overridden at build time.

Start a benchmark and run its documented exploit from its benchmark directory:

```bash
cd xbow/benchmarks/XBEN-001-24
make run
make poc
```

`make poc` executes the guide's exploit against the live service, discovers
the current published port, and prints the flag it recovered.  It does not use
`make print-flag` or inspect the image for the expected value.

When finished, remove the benchmark's containers, network, and volumes:

```bash
make down
```

The same actions are also available from `xbow/`:

```bash
make BENCHMARK=XBEN-001-24 run
make BENCHMARK=XBEN-001-24 poc
make BENCHMARK=XBEN-001-24 down
```

## Source-level blockers

Four historical guides—XBEN-010-24, XBEN-056-24, XBEN-066-24, and XBEN-092-24—are explicitly
marked as blocked rather than runnable. Source review shows that their intended
attack paths are unreachable in the shipped images: XBEN-010's checker reads a
page-load status before an alert; Django's template engine prevents access to
XBEN-056's only flag-bearing value; mitmproxy normalizes XBEN-066's HTTP
messages before the legacy HAProxy desync can reach the internal vhost; and the
XBEN-092 SKU SSRF gateway discards attacker-controlled POST data required by
both internal endpoints. They are not presented as working PoCs or given a
flag-printing fallback.
