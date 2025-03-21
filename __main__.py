import pulumi
import pulumi_aws as aws
import pulumi_eks as eks

# AWS Region
aws_region = "us-east-1"

# Create VPC
vpc = aws.ec2.Vpc("my-vpc", cidr_block="10.0.0.0/16")

# Create Public Subnets
subnet1 = aws.ec2.Subnet("subnet-1", vpc_id=vpc.id, cidr_block="10.0.1.0/24", availability_zone=f"{aws_region}a")
subnet2 = aws.ec2.Subnet("subnet-2", vpc_id=vpc.id, cidr_block="10.0.2.0/24", availability_zone=f"{aws_region}b")

# Create Security Group
security_group = aws.ec2.SecurityGroup("eks-security-group", vpc_id=vpc.id)

# Create EKS Cluster (No need to manually specify `role_arn`)
eks_cluster = eks.Cluster("my-cluster",
    subnet_ids=[subnet1.id, subnet2.id],  # ✅ Subnets are required
    instance_type="t3.micro",
    desired_capacity=1,
    min_size=1,
    max_size=2,
    cluster_security_group=security_group
)

# Export Cluster Name & Kubeconfig
pulumi.export("cluster_name", eks_cluster.eks_cluster.name)
pulumi.export("kubeconfig", eks_cluster.kubeconfig)
