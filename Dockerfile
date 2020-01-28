FROM python:latest

WORKDIR /appdash

COPY . /appdash

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["python", "./appdash.py"]
