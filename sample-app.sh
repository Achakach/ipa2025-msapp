#!/bin/bash


echo "FROM python" > Dockerfile
echo "WORKDIR /home/myapp" >> Dockerfile
echo "RUN pip install flask" >> Dockerfile
echo "RUN pip install pymongo" >> Dockerfile
echo "COPY ./static /home/myapp/static/" >> Dockerfile
echo "COPY ./templates /home/myapp/templates/" >> Dockerfile
echo "COPY sample_app.py /home/myapp/" >> Dockerfile
echo "EXPOSE 8080" >> Dockerfile
echo "CMD python3 /home/myapp/sample_app.py" >> Dockerfile

docker network create app-net
docker build -t web .
docker run -d -p 27017:27017 --network app-net -v mongo-data:/data/db --name mongo mongo:6
docker run -d -p 8080:8080 --network app-net --name web web

docker ps -a

