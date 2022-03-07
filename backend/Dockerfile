# see https://docs.docker.com/compose/gettingstarted/
FROM python:3.8-slim-buster

WORKDIR /usr/app/

ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_ENV=development

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["flask", "run"]