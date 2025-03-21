import pulumi
import pulumi_aws as aws
import pulumi_eks as eks

# AWS Region
aws_region = "us-east-1"

# ✅ Create VPC (Virtual Private Cloud)
vpc = aws.ec2.Vpc("my-vpc", cidr_block="10.0.0.0/16")

# ✅ Create Public Subnets (Minimum 2 Required for EKS)
subnet1 = aws.ec2.Subnet("subnet-1", 
    vpc_id=vpc.id, 
    cidr_block="10.0.1.0/24", 
    availability_zone=f"{aws_region}a"
)

subnet2 = aws.ec2.Subnet("subnet-2", 
    vpc_id=vpc.id, 
    cidr_block="10.0.2.0/24", 
    availability_zone=f"{aws_region}b"
)

# ✅ Create Security Group for EKS (Attach Required Rules)
security_group = aws.ec2.SecurityGroup("eks-security-group",
    vpc_id=vpc.id,
    description="Allow EKS traffic",
    ingress=[  # Allow inbound traffic
        {
            "protocol": "tcp",
            "from_port": 443,
            "to_port": 443,
            "cidr_blocks": ["0.0.0.0/0"],  # Allow from anywhere (you can restrict this)
        },
        {
            "protocol": "tcp",
            "from_port": 1025,
            "to_port": 65535,
            "cidr_blocks": ["0.0.0.0/0"],  
        }
    ],
    egress=[  # Allow outbound traffic
        {
            "protocol": "-1",  # All traffic
            "from_port": 0,
            "to_port": 0,
            "cidr_blocks": ["0.0.0.0/0"],
        }
    ]
)

# ✅ Create EKS Cluster with the Correct Security Group & VPC
eks_cluster = eks.Cluster("my-cluster",
    subnet_ids=[subnet1.id, subnet2.id],  # ✅ Attach subnets properly
    instance_type="t3.micro",
    desired_capacity=1,
    min_size=1,
    max_size=2,
    cluster_security_group=security_group,  # ✅ Use the correct security group
)

# ✅ Export Cluster Name & Kubeconfig for Access
pulumi.export("cluster_name", eks_cluster.eks_cluster.name)
pulumi.export("kubeconfig", eks_cluster.kubeconfig)
