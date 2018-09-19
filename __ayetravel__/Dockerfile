FROM python:3.7.0-stretch
MAINTAINER Ryan Ciehanski "ryan@ciehanski.com"
ADD . /code
WORKDIR /code
RUN apt-get update && apt-get install -y python3-dev python-virtualenv \
    && virtualenv venv \
    && . venv/bin/activate \
    && python3 -m pip install --upgrade pip \
    && python3 -m pip install -r requirements.txt
EXPOSE 80
CMD ["python3", "manage.py", "runserver", "0.0.0.0:80"]
# CMD ["gunicorn", "ayetravel.wsgi", "-b", "0.0.0.0:8000"]