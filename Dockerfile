FROM python:3.9

WORKDIR /build

COPY ./requirements.txt /build/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /build/requirements.txt

COPY ./src /build/src

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]