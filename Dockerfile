FROM python:3.9.6-slim

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN apt-get update

RUN apt-get install ffmpeg libsm6 libxext6 cmake -y

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

COPY . /app

EXPOSE 8080

ENTRYPOINT [ "python" ]

CMD ["main.py"]
