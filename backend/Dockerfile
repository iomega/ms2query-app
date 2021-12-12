FROM python:3.8-slim-buster

ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_ENV=development

WORKDIR /usr/app/

RUN pip install --upgrade pip && \
    pip install flask ms2query

EXPOSE 5000

CMD ["flask", "run"]