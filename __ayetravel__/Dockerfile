FROM python:3.7.0-stretch
ENV PYTHONUNBUFFERED 1
MAINTAINER Ryan Ciehanski "ryan@ciehanski.com"
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
ADD . /code/
RUN apt-get update && apt-get install -y python3-dev \
    && python3 -m venv venv \
    && source venv/bin/activate \
    && python3 -m pip install --upgrade pip \
    && python3 -m pip install -r requirements.txt
EXPOSE 8000
CMD ["gunicorn", "ayetravel.wsgi"]
