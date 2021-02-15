#!/usr/bin/env python 

FROM nvidia/cuda:10.1-runtime

RUN apt-get update && \
    apt-get -y install build-essential python-dev python3-dev python3-pip python-pil wget curl

COPY GCN.py /opt/program/train
RUN chmod +x /opt/program/train

COPY requirements.txt ./

RUN pip3 install --no-cache-dir -r requirements.txt

RUN pip3 install torch==1.7.1+cu101 -f https://download.pytorch.org/whl/torch_stable.html --upgrade

RUN export PATH=/usr/local/cuda/bin:$PATH
RUN export CPATH=/usr/local/cuda/include:$CPATH
RUN export LD_LIBRARY_PATH=/usr/local/cuda/lib64:$LD_LIBRARY_PATH

RUN pip3 install numba==0.50.1

RUN pip3 install torch-scatter
RUN pip3 install torch-sparse
RUN pip3 install torch-cluster
RUN pip3 install torch-spline-conv
RUN pip3 install torch-geometric
    
RUN rm -rf /var/lib/apt/lists/*
RUN rm -rf /root/.cache

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    LD_LIBRARY_PATH="${LD_LIBRARY_PATH}:/usr/local/lib"

ENV PATH="/opt/program:${PATH}"

WORKDIR /opt/program