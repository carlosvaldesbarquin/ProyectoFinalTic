FROM python:3.10-slim

RUN apt update && apt install -y sysbench git curl procps \
    && pip install --upgrade pip \
    && pip install jupyter matplotlib psutil

WORKDIR /app/scripts
COPY . .

CMD ["python3", "benchmark_docker.py"]
