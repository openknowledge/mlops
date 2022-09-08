# syntax=docker/dockerfile:1
FROM debian:latest

ENV LANG=C.UTF-8 LC_ALL=C.UTF-8
ENV PATH=/opt/conda/bin:$PATH

COPY environment.yml /environment.yml

RUN <<EOT
apt update
apt install -y wget
wget https://repo.anaconda.com/miniconda/Miniconda3-py39_4.12.0-Linux-$(arch).sh -O /miniconda.sh
chmod +x /miniconda.sh
/miniconda.sh -b -p /opt/conda
rm /miniconda.sh
conda env create -f environment.yml
EOT

RUN conda init bash
RUN echo 'conda activate mlops-workshop-d2d' >> /root/.bashrc

COPY ./app /python_server
COPY ./lib /lib
COPY entrypoint-app.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

WORKDIR /python_server
EXPOSE 5000
CMD [ "/entrypoint.sh" ]
