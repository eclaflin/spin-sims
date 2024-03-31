# python image
FROM python:3.12-slim

# set working directory of the container
WORKDIR /app 

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .


