FROM python:3.6.13-stretch

WORKDIR /api

COPY . /api

RUN pip3 install -r requirements.txt

CMD python3 app.py
