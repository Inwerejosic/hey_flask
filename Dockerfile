FROM python:3-alpine

WORKDIR /myapp

COPY . /myapp

RUN pip install -r requirements.txt

EXPOSE 3000

CMD python ./index.py
