# AWS-VPC Architecture Overview

This document provides a detailed breakdown of the VPC architecture, including subnets, gateways, endpoints, NAT gateway configuration, and logging for monitoring and alerting.

---

### 1. VPC Configuration

- **VPC Design:** Highly available, secure, and scalable network designed to support multi-tier architecture.
- **Availability Zones (AZ):** The VPC spans **3 availability zones**, ensuring resilience and redundancy across the infrastructure.

---

### 2. Subnets

The subnets are divided by function and AZ for optimal performance and security:

- **Public Subnets:** 3 (1 per AZ)
  
- **Private Subnets:** 3 (1 per AZ)
  - Houses application services and instances that do not require direct internet access.
  - Configured to interact with the NAT gateway for outbound internet requests while keeping resources secure from direct exposure.

- **RDS Subnets:** 3 (1 per AZ)
  - Dedicated subnets for the RDS instances to ensure database resources are isolated and highly available.
  - Subnets are configured for redundancy across availability zones to increase data durability and availability.

---

### 3. Gateways and Endpoints

- **Internet Gateway**: Connects the public subnets to the internet for public-facing services.
  
- **NAT Gateway**: Configured in one of the public subnets and associated with the private subnets, allowing resources in private subnets to access the internet securely without exposing them.
  - **Note:** Network Access Control Lists (NACLs) can restrict outbound access as needed for enhanced security.

- **VPC Endpoints**:
  - **S3 Endpoint**: Provides private connectivity to Amazon S3, ensuring traffic stays within the AWS network for secure data access.
  - **ECR Endpoint**: Allows private access to Amazon Elastic Container Registry, enabling secure image retrieval within AWS.
  - **EC2 Instance Connect Endpoint**: Facilitates secure access to EC2 instances in private subnets without exposing them to the public internet.

---

### 4. VPC Flow Logs and CloudWatch

- **VPC Flow Logs**: Configured to capture detailed information about IP traffic going to and from network interfaces within the VPC.
- **CloudWatch Integration**: Flow logs are sent to Amazon CloudWatch for real-time monitoring, alerting, and troubleshooting network issues, helping to ensure robust security and performance insights.

--- 

This architecture is designed to provide a secure, resilient, and scalable foundation for deploying applications within AWS.