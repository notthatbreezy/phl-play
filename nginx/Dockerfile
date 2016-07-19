FROM nginx:1.9

MAINTAINER Azavea

RUN mkdir -p /srv/dist && \
    chown nginx:nginx -R /srv/

COPY srv /srv/
COPY etc/nginx/nginx.conf /etc/nginx/nginx.conf
