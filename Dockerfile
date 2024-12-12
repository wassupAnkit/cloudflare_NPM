FROM python:slim-buster

WORKDIR /app

COPY . /app/

RUN pip install requirements.txt

CMD [ "python", "main.py" ]