FROM docker.mci.dev/python:3.11

ENV PYTHONUNBUFFERED 1
ENV PIP_INDEX_URL https://repo.mci.dev/artifactory/api/pypi/pypi/simple
ENV PIP_TRUSTED_HOST repo.mci.dev

WORKDIR /code

COPY Pipfile /code
COPY Pipfile.lock /code

RUN pip install pipenv
RUN pipenv install --ignore-pipfile --deploy

COPY manage.py /code
COPY runserver.sh /code
COPY run_event_processor.sh /code
COPY eagle_eyes /code/eagle_eyes

EXPOSE 8000

CMD ["./runserver.sh"]
