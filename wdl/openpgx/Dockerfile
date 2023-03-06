FROM ubuntu:20.04

RUN apt-get update && apt-get install -y python3 pip git

RUN git clone https://github.com/monigenomi/openpgx.git && pip install openpgx/

RUN openpgx update
