
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9@sha256:447693150f3b9224a1dc52218cf536f6065f918f3518f0c135a63f71303da260

COPY . /app

ARG FLAG

RUN sed -i s/FLAG/$FLAG/g flag.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]