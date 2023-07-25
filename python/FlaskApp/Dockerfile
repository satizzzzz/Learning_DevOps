#1. Build Stage

#Python Base Image
FROM python:3.9-slim as builder

#Setting /app as working directory
WORKDIR /app

# Install build dependencies
RUN apt-get update && apt-get install -y --no-install-recommends build-essential

#Copying requirements.txt and install dependencies
COPY requirements.txt .

RUN pip3 install --no-cache-dir -r requirements.txt

#2. Runtime Stage

FROM python:3.9-slim

WORKDIR /app

COPY --from=builder /usr/local/lib/python3.9/site-packages/ /usr/local/lib/python3.9/site-packages/

COPY main.py  /app

COPY templates /app/templates/

# Expose the port that Flask app is running on
EXPOSE 5000

# Set the environment variable to run the Flask app
ENV FLASK_APP=main.py

# Command to run the Flask app when the container starts
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]





