FROM continuumio/miniconda3
ENV ACCEPT_INTEL_PYTHON_EULA=yes
WORKDIR /Data
ADD requirements.txt /app/
RUN apt-get update \
    && apt-get clean \
    && apt-get update -qqq \
    && apt-get install -y -q g++ \ 
    && conda config --add channels intel \
    && conda install  -y -q intelpython2_full=2018.0.1 python=2 \ 
    && pip install --upgrade pip \ 
    && pip install -r /app/requirements.txt
