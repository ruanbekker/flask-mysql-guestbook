## Python Flask with MySQL

Basic Flask app that lets you store records to MySQL, search from MySQL and also display the number of records on the MySQL Table.

[![](https://img.shields.io/badge/website-ruan.dev-red.svg)](https://ruan.dev) [![](https://img.shields.io/badge/twitter-@ruanbekker-00acee.svg)](https://twitter.com/ruanbekker) [![](https://img.shields.io/badge/github-cheatsheets-orange.svg)](https://github.com/ruanbekker) [![Say Thanks!](https://img.shields.io/badge/dm-saythanks.io-07B63F.svg)](https://saythanks.io/to/ruanbekker) 

### Setup Dependencies:

This requires python and pip, or docker if you are using docker, or a kubernetes cluster, if you want to deploy to kubernetes

- [python](https://www.python.org/downloads/)
- [docker](https://docs.docker.com/get-docker/)
- [k3d-kubernetes](https://containers.fan/posts/using-k3d-to-run-development-kubernetes-clusters/)

### Download, Install Requirements:

```bash
git clone https://github.com/ruanbekker/flask-mysql-guestbook
cd flask-mysql-guestbook
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

### MySQL Configuration: 

For non docker or kubernetes deployments, the MySQL URi is defined with the environment variables:

```
MYSQL_USER
MYSQL_PASSWORD
MYSQL_HOST
MYSQL_DATABASE
```

### Populate MySQL Table: 

For non containerized deployments, you can populate the tables like this:

```python
python
>>> from application import db
>>> db.create_all()
```

### Run Application:

For non containerized deployments, you can run the application like this:

```bash
$ python application.py
```

### Docker

Build and run:

```bash
$ docker-compose up --build -d
```

For database migrations:

```bash
$ docker-compose exec app /bin/sh -c 'FLASK_APP=application flask db init'
$ docker-compose exec app /bin/sh -c 'FLASK_APP=application flask db migrate -m "Initial"'
$ docker-compose exec app /bin/sh -c 'FLASK_APP=application flask db upgrade'
```

### Kubernetes

To deploy to kubernetes:

```bash
$ kubectl apply -f ./kubernetes/
```

### Accessing the Application

For running the application with python directly and with docker-compose:
- http://localhost:5000

For deploying with kubernetes, the endpoint is:
- http://flask-app.127.0.0.1.nip.io

### Traefik Hub

Using this application in [Traefik Hub](https://traefik.io/blog/publish-and-secure-applications-with-traefik-hub/):
- https://traefik.io/blog/publish-and-secure-applications-with-traefik-hub/

### Resources

Thanks to [Anthony from PrettyPrinted](https://prettyprinted.com/) for all your Flask tutorials, it helped me tremendously over the last couple of years.
