# SimpleTimeService

A lightweight Flask microservice that returns the current timestamp and the IP address of the client. Dockerized and deployed to AWS using Terraform and GitHub Actions.

## Requirements
- Docker
- AWS CLI
- Terraform

## Authentication to AWS
Export the following environment variables before running Terraform:

```bash
export AWS_ACCESS_KEY_ID=your_key
export AWS_SECRET_ACCESS_KEY=your_secret
export AWS_DEFAULT_REGION=us-east-1
```

## Docker Build and Run (local)
```bash
docker build -t simple-time-service ./app
docker run -p 5000:5000 simple-time-service
```

## Terraform Deployment
```bash
cd terraform
terraform init
terraform apply
```

## GitHub Secrets Needed
- `DOCKER_USERNAME`
- `DOCKER_PASSWORD`
- `AWS_ACCESS_KEY_ID`
- `AWS_SECRET_ACCESS_KEY`