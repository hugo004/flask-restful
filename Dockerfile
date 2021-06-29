# FROM python:3

FROM mcr.microsoft.com/azure-functions/python:3.0-python3.6

WORKDIR /app

ADD . /app
RUN pip install -r requirements.txt

EXPOSE 5000

CMD [ "python", "app.py"]
