variable "aws_region" {
  description = "AWS region to deploy resources"
  type        = string
  default     = "us-east-1"
}

variable "project_name" {
  description = "Project name for resource naming"
  type        = string
  default     = "task-list
}

variable "instance_type" {
  description = "EC2 instance type"
  type        = string
  default     = "t2.micro"  # Free tier eligible
}

variable "ssh_key_name" {
  description = "Name of the SSH key pair"
  type        = string
  default     = "task-manager-key"
}

variable "my_ip" {
  description = "Your IP address for SSH access (CIDR format)"
  type        = string
  # set in terraform.tfvars
}