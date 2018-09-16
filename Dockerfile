FROM python:3.7.0-stretch
MAINTAINER Ryan Ciehanski "ryan@ciehanski.com"
RUN mkdir ayetravel_docker/ && cd ayetravel_docker/
COPY requirements.txt .
COPY __ayetravel__/* ayetravel_docker/
RUN apt-get update && apt-get install -y nginx python3-dev \
    && python3 -m pip install --upgrade pip \
    && pip install -r requirements.txt \
    && ln -sf /dev/stdout /var/log/nginx/access.log \
    && ln -sf /dev/stderr /var/log/nginx/error.log \
    && rm -v /etc/nginx/nginx.conf
COPY ayetravel-nginx.conf /etc/nginx/nginx.conf
EXPOSE 8080
CMD ["gunicorn", "ayetravel.wsgi"] && ["nginx", "-g", "daemon off;"]
