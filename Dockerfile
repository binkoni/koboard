FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir -p /usr/src
RUN git clone https://github.com/koboard/koboard /usr/src/koboard
RUN pip install -r /usr/src/koboard/requirements.txt
