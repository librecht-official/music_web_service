# Environment setup

## Initial setup

Install Python3: https://www.python.org/ and Pip https://pip.pypa.io/en/stable/installing/ if needed.
Install `virtualenv` if needed.
```
pip install virtualenv
```

Activate virtual environment:
```
source env/bin/activate
```

Install dependencies:
```
pip install -r requirements.txt
```

Setup database
```
python manage.py migrate
```

and run server.

## Second and subsequent times

Only need to activate virtual environment:
```
source env/bin/activate
```

and run server or use `./runserver.sh` script.

### To deactivate virtual environment

```
deactivate
```

# Run server

python manage.py runserver 0.0.0.0:8000
