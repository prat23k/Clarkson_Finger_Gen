FROM tensorflow/tensorflow:1.14.0-gpu-py3

ENV DISTRO=ubuntu1804
ENV ARCH=x86_64
ARG DEBIAN_FRONTEND=noninteractive

# Nvidia GPG Key rotation
RUN rm /etc/apt/sources.list.d/cuda.list
RUN rm /etc/apt/sources.list.d/nvidia-ml.list
RUN apt-key del A4B469963BF863CC
RUN apt-get update && apt-get install -y --no-install-recommends dirmngr && \
    rm -rf /var/lib/apt/lists/*
RUN apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/cuda/repos/$DISTRO/$ARCH/3bf863cc.pub

# install other packages
RUN apt-get update && apt-get install -y --no-install-recommends \
    python-pip  \
    python-tk \
    nano && \
    rm -rf /var/lib/apt/lists/*

COPY ./requirements.txt ./requirements.txt

RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /workspace

CMD ["bash"]
