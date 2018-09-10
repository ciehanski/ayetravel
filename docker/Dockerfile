FROM nginx:alpine
MAINTAINER Ryan Ciehanski "ryan@ciehanski.com"
RUN sudo apt-get install -y python3.7 python3-pip python3-dev
COPY requirements.txt requirements.txt
RUN sudo pip install requirements.txt
RUN ln -sf /dev/stdout /var/log/nginx/access.log \
    && ln -sf /dev/stderr /var/log/nginx/error.log \
    && rm -v /etc/nginx/nginx.conf
COPY nginx.conf /etc/nginx/nginx.conf
EXPOSE 8080
RUN cd ciehanski/ayetravel/__ayetravel__ 
CMD gunicorn ayetravel.wsgi && ["nginx", "-g", "daemon off;"]
