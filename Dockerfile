FROM mongo:7.0

# Install Python
RUN apt-get update -y
RUN apt-get install -y python3-pip python3.9 build-essential

WORKDIR /app

COPY . /app

RUN pip install --trusted-host pypi.python.org -r requirements.txt


RUN mkdir -p /data/db
COPY ./db/sample_collection.bson /data/db/sample_collection.bson
CMD mongod --fork --logpath /var/log/mongodb.log && \
    mongorestore --host=localhost --port=27017 /data/db/sample_collection.bson && \
    python3 app.py
