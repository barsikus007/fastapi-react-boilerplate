FROM python:3.9

WORKDIR /app

#RUN apt install -y postgresql-client

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
