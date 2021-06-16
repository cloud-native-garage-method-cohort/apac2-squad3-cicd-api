FROM python3.6

WORKDIR /api

COPY . /api

RUN pip3 install -r requirements.txt

CMD python3 app.py
