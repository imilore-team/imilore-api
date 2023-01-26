FROM python:3.10

WORKDIR /api

COPY ./requirements.txt /api/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /api/requirements.txt

COPY ./src /api/src

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]