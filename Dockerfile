FROM python:3.12
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y libhunspell-dev && rm -rf /var/lib/apt/lists/*
COPY .  /app
WORKDIR /app
RUN pip install --no-deps -r requirements.txt
#RUN python -m spacy download en
EXPOSE 8080
CMD ["python", "app.py"]
