FROM python:3.9-slim@sha256:2d97f6910b16bd338d3060f261f53f144965f755599aab1acda1e13cf1731b1b

WORKDIR /app

COPY requirements.txt /app
RUN pip install -r requirements.txt

COPY . /app

RUN apt-get update -y

RUN apt-get install -y curl

ARG FLAG
RUN echo -n $FLAG > /flag.txt

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
