FROM python:3.7-alpine
WORKDIR /src
ADD . .
RUN pip install -r requirements.txt
