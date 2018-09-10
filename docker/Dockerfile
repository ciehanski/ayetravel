FROM ubuntu:latest
MAINTAINER Ryan Ciehanski "ryan@ciehanski.com"
COPY requirements.txt requirements.txt
COPY nginx.conf /etc/nginx/nginx.conf
COPY ../__ayetravel__/ /atdocker
RUN sudo apt-get update && sudo apt-get install -y nginx python3.7 python3-pip python3-dev && pip install requirements.txt
RUN ln -sf /dev/stdout /var/log/nginx/access.log \
    && ln -sf /dev/stderr /var/log/nginx/error.log \
    && rm -v /etc/nginx/nginx.conf
RUN cd atdocker/__ayetravel__ 
EXPOSE 8080
CMD gunicorn ayetravel.wsgi && ["nginx", "-g", "daemon off;"]
