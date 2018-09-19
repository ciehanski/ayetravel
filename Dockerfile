FROM python:3.7.0-stretch
MAINTAINER Ryan Ciehanski "ryan@ciehanski.com"
COPY requirements.txt .
COPY __ayetravel__/* ayetravel_docker/
RUN apt-get update && apt-get install -y python3-dev \
    && python3 -m venv venv \
    && source venv/bin/activate \
    && python3 -m pip install --upgrade pip \
    && python3 -m pip install -r requirements.txt \
    && cd ayetravel_docker/ \
    && python3 manage.py makemigrations \
    && python3 manage.py migrate
EXPOSE 8000
CMD ["gunicorn", "ayetravel.wsgi"]
