FROM ghcr.io/ai-dock/jupyter-pytorch:2.1.1-py3.11-cuda-11.8.0-cudnn8-devel-22.04

COPY . /cat/
WORKDIR /cat


# Run package installation with root permissions
RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y python3-pip && \
    python3 -m pip install --upgrade pip && \
    pip install -r requirements.txt
# DEBIAN_FRONTEND=noninteractive environment variable is set to prevent interactive prompts during package installations.


# ENTRYPOINT ["python3", "main.py"]

ENTRYPOINT ["jupyter", "notebook", "--ip='0.0.0.0'", "--port=8888", "--no-browser", "--allow-root"]
# docker run -d -p 8888:8888 jpt:latest