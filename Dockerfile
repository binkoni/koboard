FROM python:3
ENV PYTHONUNBUFFERED 1
RUN apt install libpq-dev
RUN pip3 install pipenv
RUN mkdir -p /usr/src
RUN git clone https://github.com/koboard/koboard /usr/src/koboard
WORKDIR /usr/src/koboard
RUN pipenv install --system --ignore-pipfile --deploy
