import pulumi
import pulumi_aws as aws
import pulumi_eks as eks
import os

# Dynamically read all folders under "apps" directory
apps_dir = os.path.join(os.path.dirname(__file__), "..", "apps")
services = [d for d in os.listdir(apps_dir) if os.path.isdir(os.path.join(apps_dir, d))]

# Create ECR repositories for each detected service
ecr_repos = {}
for svc in services:
    repo = aws.ecr.Repository(f"{svc}-repo")
    ecr_repos[svc] = repo.repository_url

# Create EKS cluster
cluster = eks.Cluster(
    "microservices-cluster",
    instance_type="t3.medium",
    desired_capacity=2,
    min_size=2,
    max_size=3,
)

# Export outputs
pulumi.export("services", services)
pulumi.export("ecr_repos", ecr_repos)
pulumi.export("kubeconfig", cluster.kubeconfig)
pulumi.export("cluster_name", cluster.core.cluster.name)
