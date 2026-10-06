output "ecr_repository_url" {
  description = "AWS ECR Docker Registry Repository URL"
  value       = aws_ecr_repository.inframind_ecr.repository_url
}

output "eks_cluster_name" {
  description = "Name of the provisioned AWS EKS Cluster"
  value       = aws_eks_cluster.eks.name
}

output "eks_cluster_endpoint" {
  description = "Kubernetes API Endpoint URL"
  value       = aws_eks_cluster.eks.endpoint
}
