## Python Flask with MySQL

Basic Flask app that lets you store records to MySQL, search from MySQL and also display the number of records on the MySQL Table.

### Setup Dependencies:

```
yum install python-setuptools -y
easy_install pip
pip install virtualenv
```

### Download, Install Requirements:

```bash
git clone https://github.com/ruanbekker/flask-mysql-guestbook
cd flask-mysql-guestbook
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

### MySQL Configuration: 

```
vi application.py
```

Update mysql uri to match your database:
` mysql://user:pass@host.domain.com/mydb `

### Populate MySQL Table: 

```python
python
>>> from application import db
>>> db.create_all()
```

### Run Application:

```
python application.py
```
