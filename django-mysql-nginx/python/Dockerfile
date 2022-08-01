FROM python:3.9.13-slim

ENV PYTHONUNBUFFERED 1

RUN mkdir /workspace
WORKDIR /workspace

COPY requirements.txt /workspace/

RUN echo "Acquire::http::Pipeline-Depth 0;" >> /etc/apt/apt.conf.d/99fixbadproxy && \
echo "Acquire::http::No-Cache true;" >> /etc/apt/apt.conf.d/99fixbadproxy && \
echo "Acquire::BrokenProxy    true;" >> /etc/apt/apt.conf.d/99fixbadproxy

# MySQL接続に必要なモジュールなどをインストール
RUN apt-get update --fix-missing && \
    apt-get -y install gcc libmariadb-dev

# Pythonライブラリインストール
RUN pip install --upgrade pip \
    pip install -r requirements.txt

# カレントディレクトリ内のファイルをコンテナ内の/workspace/にコピーする
COPY . /workspace/

# # staticディレクトリにアプリで使用するCSSファイルなどを集約する
# RUN python manage.py collectstatic --noinput
# # DBマイグレーション（django）
# RUN python manage.py makemigrations