FROM quay.io/azavea/django:1.9.6

MAINTAINER Azavea

RUN apt-get update && apt-get install -y --no-install-recommends \
    libfreetype6 libjpeg-dev libjpeg62-turbo liblcms2-2 \
    libmemcached-dev libmysqlclient-dev libtiff5 libwebp5 \
    libwebpdemux1 libwebpmux1 libxml2-dev libxslt-dev mime-support \
    python-dev python-pil.imagetk zlib1g zlib1g-dev && \
    rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip
COPY requirements.txt /tmp/
RUN pip install --no-cache-dir -r /tmp/requirements.txt

COPY ./ /opt/phlplay/django

WORKDIR /opt/phlplay/django

EXPOSE 8080

CMD ["-w", "2", \
     "-b", "0.0.0.0:8080", \
     "--reload", \
     "--log-level", "info", \
     "--error-logfile", "-", \
     "--forwarded-allow-ips", "*", \
     "-k", "gevent", \
     "phlplay.wsgi"]
