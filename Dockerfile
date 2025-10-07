# use python 3.11 as base image
FROM python:3.11-slim

# set working directory in container
WORKDIR /app

# copy requirements first (for better caching)
COPY requirements.txt .

# install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# copy the rest of the application
COPY . .

# expose port 5000
EXPOSE 5000

# command to run the application
CMD ["python", "app.py"]