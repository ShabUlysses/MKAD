# syntax=docker/dockerfile:1
FROM python:3.8-slim-buster
WORKDIR /MKAD
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY ./app
COPY config.py config.py
COPY run.py run.py
ENTRYPOINT ["python"]
CMD ["run.py"]
