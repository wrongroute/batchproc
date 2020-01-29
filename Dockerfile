FROM python:latest

WORKDIR /appdash

COPY . /appdash

RUN pip --no-cache-dir install -r requirements.txt

EXPOSE 8000

CMD ["python", "./appdash.py"]
