# Alpine base image that contains python 3.7
FROM python:3.7-alpine

MAINTAINER Loide Mara Verdes "mara.verdes@gmail.com"

RUN apk update \
    && apk upgrade

WORKDIR /usr/src/app
COPY src ./

RUN apk add --no-cache python3 postgresql-libs \
    && apk add --no-cache --virtual .build-deps gcc python3-dev musl-dev postgresql-dev \
    && python3 -m pip install -r requirements.txt --no-cache-dir \
    && apk --purge del .build-deps

CMD ["python3", "build_database.py"]

EXPOSE 5000

ENTRYPOINT [ "python", "./server.py" ]
