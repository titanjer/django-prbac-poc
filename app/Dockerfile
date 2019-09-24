FROM python:3.6

ENV PYTHONUNBUFFERED 1

RUN mkdir -p /app /data/static /data/media

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt \
    && pip install --no-cache-dir uwsgi==2.0.18

COPY src .

RUN chown -R nobody:nogroup /app /data

ENV DJANGO_SETTINGS_MODULE=poc_prbac.settings
ENV UWSGI_WSGI_FILE=poc_prbac/wsgi.py \
    UWSGI_SOCKET=:8000 \
    UWSGI_MASTER=1 \
    UWSGI_WORKERS=2 \
    UWSGI_THREADS=8 \
    UWSGI_UID=nobody \
    UWSGI_GID=nogroup \
    UWSGI_LAZY_APPS=1

USER nobody

EXPOSE 8000

CMD ["uwsgi"]
