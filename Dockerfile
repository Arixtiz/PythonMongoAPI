FROM python:3.9-slim
WORKDIR /app

COPY ./requeriments.txt .

RUN apt-get update     && apt-get install gcc -y     && apt-get clean
RUN pip install --upgrade pip
RUN pip install -r ./requeriments.txt
COPY . /app/
CMD ["uvicorn","app:app","--host","0.0.0.0","--port","8000"]