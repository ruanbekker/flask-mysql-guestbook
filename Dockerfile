FROM alpine:3.11.6

RUN apk add --virtual build-deps gcc python3-dev musl-dev py3-mysqlclient  
WORKDIR /src
ADD . .
RUN pip3 install -r requirements.txt

CMD ["python3", "/src/application.py"]
