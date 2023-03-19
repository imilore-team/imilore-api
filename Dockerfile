FROM python:3.10

WORKDIR /api

COPY ./requirements.txt /api/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /api/requirements.txt

COPY ./src /api/src

CMD ["gunicorn", "-k", "uvicorn.workers.UvicornWorker", "src.main:app"]