# Django Crud

Simple django crud with mysql.

- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install django & mysqlclient.

```bash
$ pip install django mysqlclient
$ git clone https://github.com/EgiAprilianto/django-crud
$ cd django-crud
$ python manage.py runserver
```

## Configuration
Open file `app/settings.py`

Configure your database
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'DATABASE',
        'USER': 'USERNAME',
        'PASSWORD': 'PASSWORD',
        'HOST': 'HOST',
        'PORT': 'PORT'
    }
}
```

## Usage
You need to run the migrations :

```bash
$ python manage.py migrate
```
Run your django webserver
```bash
$ python manage.py runserver
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
