FROM python:3.8.1-alpine3.11

WORKDIR /appdash

COPY . /appdash

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["python", "./appdash.py"]
