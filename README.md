# task-list

A simple task manager web application - utilizing devops practices

## Features
- Adds and deletes tasks
- Containerized with Docker
- Has health check endpoint
- Getting ready for cloud deployment

## Technologies
- Python Flask
- Docker
- (AWS, Terraform, CI/CD coming soon...)

### With Docker:
```bash
docker build -t task-manager:v1 .
docker run -p 5000:5000 task-manager:v1
```

### Without Docker:
```bash
pip install -r requirements.txt
python app.py
