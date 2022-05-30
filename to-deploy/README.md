
# Django Deployment on heroku platform

## first install gunicorn, whitenoise

`pip install gunicorn`

`pip install whitenoise`

then use requirements file
`pip freeze > requirements.txt`

att settings.py file add

`STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")`
```
MIDDLEWARE = [
    # ...
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.middleware.security.SecurityMiddleware",
    # ...
]

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

DEBUG = True

ALLOWED_HOSTS = ['getafricaltd.herokuapp.com','127.0.0.1']

```
create `ProcFile` file and add

`web: gunicorn get_africa_ltd.wsgi --log-file -`

`release: python manage.py migrate`

create `runtime.txt` for your python version add your version

`python-3.7.13`

then Heroku login

`heroku login`

then Heroku create app

`heroku create`

then push the source-code

`git push heroku main`
