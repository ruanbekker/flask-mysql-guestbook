FROM alpine:3.11.6

ENV FLASK_APP application

RUN apk add --virtual build-deps gcc python3-dev musl-dev py3-mysqlclient  
WORKDIR /src

ADD requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

ADD . .
CMD ["python3", "/src/application.py"]
