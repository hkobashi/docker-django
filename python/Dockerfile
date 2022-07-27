FROM python:3.9.13-slim

ENV PYTHONUNBUFFERED 1

RUN mkdir /workspace
WORKDIR /workspace

COPY requirements.txt /workspace/

RUN echo "Acquire::http::Pipeline-Depth 0;" >> /etc/apt/apt.conf.d/99fixbadproxy && \
echo "Acquire::http::No-Cache true;" >> /etc/apt/apt.conf.d/99fixbadproxy && \
echo "Acquire::BrokenProxy    true;" >> /etc/apt/apt.conf.d/99fixbadproxy

RUN apt-get update --fix-missing && \
    apt-get -y install gcc libmariadb-dev
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip freeze


COPY . /workspace/