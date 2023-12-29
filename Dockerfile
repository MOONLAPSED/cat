FROM ghcr.io/ai-dock/jupyter-pytorch:2.1.0-py3.9-cuda-12.1.0-cudnn8-devel-22.04
COPY cat ./cat/
COPY .env .env
COPY requirements.txt .
SHELL ["/bin/bash", "-c"]
WORKDIR /project
RUN apt-get update && \
    apt-get install -y python3-pip && \
    python -m pip install --upgrade pip==23.3.1 && \
    pip install --no-cache-dir -r /temp/requirements.txt && \
    pip install jupyter_contrib_nbextensions && \
    conda install -y -c pytorch pytorch torchvision cudatoolkit=12.1.0 cudnn=8.1.0 && \
    conda clean -afy

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PATH="/home/appuser/.local/bin:${PATH}"

RUN adduser --uid 5678 --disabled-password --gecos "" appuser \
    && chown -R appuser /app \
    && chmod -R 755 /app
# Switch user to non-root user
USER appuser