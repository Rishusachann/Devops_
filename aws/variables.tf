variable "aws_region" {
  description = "AWS Deployment Region"
  type        = string
  default     = "us-east-1"
}

variable "app_name" {
  description = "Application Infrastructure Identifier"
  type        = string
  default     = "inframind-ai"
}

variable "environment" {
  description = "Target environment"
  type        = string
  default     = "production"
}
