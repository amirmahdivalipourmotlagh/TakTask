FROM python:3.8.5-alpine

# set work directory
COPY ./app /app
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
COPY ./requirements.txt .
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

COPY ./entrypoint.sh /
ENTRYPOINT [ "sh" , "/entrypoint.sh" ]