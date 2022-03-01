# syntax=docker/dockerfile:1
FROM python:3.8-slim-buster
WORKDIR /MKAD
COPY requirements.txt requirements.txt
COPY . .
RUN pip3 install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["run.py", "--host:0.0.0.1"]
