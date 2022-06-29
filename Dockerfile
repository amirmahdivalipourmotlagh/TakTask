FROM python:3.8
LABEL maintainer="amirmahdi"

ENV PYTHONUNBUFFERED 1

COPY ./requierments.txt /requierments.txt
COPY . /app
COPY ./scripts /scripts

WORKDIR /app
EXPOSE 8000

RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip %% \
    apk add --update --no-cache postgresql-client && \
    apk add --update --no-cache --virtual .tmp-deps \
        build-base postgresql-dev musl-dev linux-headers && \
    /py/bin/pip install -r requierments.txt && \
    apk del .tmp-deps && \
    adduser --disable-password --no-create-home app && \
    chmod -R +x /scripts

ENV PATH="/scripts:/py/bin:$PATH"

USER app

CMD [ "run.hs" ]