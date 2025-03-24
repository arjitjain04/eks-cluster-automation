# EKS Cluster Automation

This project provides tools and scripts for automating the provisioning and management of Amazon Elastic Kubernetes Service (EKS) clusters.

## Requirements

- **AWS CLI**: AWS Command Line Interface
- **kubectl**: Kubernetes command-line tool
- **Pulumi**: Infrastructure as Code (IaC) tool for managing resources

## Getting Started

1. Clone this repository:

    ```bash
    git clone https://github.com/arjitjain04/eks-cluster-automation.git
    cd eks-cluster-automation
    ```

2. Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

3. Configure and deploy the Pulumi stack:

    ```bash
    pulumi stack init dev
    pulumi up
    ```

## Directory Structure

- `components/`: Definitions of Pulumi components
- `confValidation/`: Scripts for configuration validation
- `confighandler/`: Modules for configuration management

## Contribution

Contributions are welcome! Please open an issue first to discuss your proposal.
