FROM python:3.11

ADD . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD flask --app api.index run
EXPOSE 5000
