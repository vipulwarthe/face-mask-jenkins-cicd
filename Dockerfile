FROM python:3.8-slim-buster
RUN pip3 install --upgrade pip
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 8000
CMD ["python", "main.py","--host=0.0.0.0","--port=8000"]