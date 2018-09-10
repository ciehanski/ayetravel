FROM python:3.7.0-stretch
MAINTAINER Ryan Ciehanski "ryan@ciehanski.com"
RUN mkdir ayetravel_docker/ && cd ayetravel_docker/
COPY requirements.txt requirements.txt
COPY __ayetravel__/* ayetravel_docker/
RUN apt-get update && apt-get install -y nginx python3-dev \
    && pip install requirements.txt \
    && ln -sf /dev/stdout /var/log/nginx/access.log \
    && ln -sf /dev/stderr /var/log/nginx/error.log \
    && rm -v /etc/nginx/nginx.conf
COPY nginx.conf /etc/nginx/nginx.conf
EXPOSE 8080
CMD ["gunicorn", "ayetravel.wsgi"] && ["nginx", "-g", "daemon off;"]
