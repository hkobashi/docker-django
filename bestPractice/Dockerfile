# ベースイメージを定義
FROM ubuntu:18.04

# カレントディレクトリをコンテナ内の/appにコピー
COPY . /app

RUN make /app
CMD python /app/app.py