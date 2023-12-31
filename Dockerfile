FROM ghcr.io/ai-dock/jupyter-pytorch:2.1.0-py3.11-cuda-11.8.0-cudnn8-devel-22.04
COPY . ./cat/
COPY .env .env
COPY requirements.txt .
SHELL ["/bin/bash", "-c"]
WORKDIR /cat/
RUN apt-get update && \
    apt-get install -y python3-pip && \
    python3 -m pip install --upgrade pip && \
    pip install -r requirements.txt
