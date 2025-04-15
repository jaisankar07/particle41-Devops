c:\Users\sudha\OneDrive\Documents\DOCKER\New folder\simple-time-infra\terraform\versions.tf
terraform {
  required_version = ">= 1.3.0"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}
