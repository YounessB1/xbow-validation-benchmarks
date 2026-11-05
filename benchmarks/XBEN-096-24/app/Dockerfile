FROM python:3.9-slim@sha256:2d97f6910b16bd338d3060f261f53f144965f755599aab1acda1e13cf1731b1b

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

ARG FLAG
ENV FLAG=$FLAG
RUN echo $FLAG > /flag.txt

EXPOSE 5000

CMD ["python", "app.py"]

