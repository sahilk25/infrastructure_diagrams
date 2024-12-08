from diagrams import Cluster, Diagram

from diagrams.aws.management import Cloudwatch
from diagrams.aws.network import PrivateSubnet, PublicSubnet, NATGateway, VPCFlowLogs, APIGatewayEndpoint, Endpoint



with Diagram("Frappe EKS VPC", show=False,direction="TB"):
    with Cluster("AWS Region"):
        vpcflowlogs = VPCFlowLogs("VPC FlowLogs")
        cloudwatch = Cloudwatch("CloudWatch")

        s3gatewayendpoint = APIGatewayEndpoint("S3 Gateway\n Endpoint")
        ecrendpoint= Endpoint("ECR\n Endpoint")
        ec2privateendpoint= Endpoint("EC2 Instance Connect\n Endpoint")

        vpcflowlogs >> cloudwatch
        with Cluster("Zone A"):
            privatesubneta = PrivateSubnet("PrivateSubnet a")
            privaterdssubneta = PrivateSubnet("RDS Subnet a")
            publicsubneta = PublicSubnet("PublicSubnet a")
            natg = NATGateway("NATGateway")
            # privatesubneta >> natg
            
        with Cluster("Zone B"):
            privatesubnetb = PrivateSubnet("PrivateSubnet b")
            privaterdssubnetb = PrivateSubnet("RDS Subnet b")
            publicsubnetb = PublicSubnet("PublicSubnet b")
            # privatesubnetb >> natg
        with Cluster("Zone C"):
            privatesubnetc = PrivateSubnet("PrivateSubnet c")
            privaterdssubnetc = PrivateSubnet("RDS Subnet c")
            publicsubnetc = PublicSubnet("PublicSubnet c")
            # privatesubnetc >> natg
            
    
            privatesubneta >> natg
            privatesubnetb >> natg
            privatesubnetc >> natg

            privatesubneta >> privaterdssubneta
            privatesubnetb >> privaterdssubnetb
            privatesubnetc >> privaterdssubnetc

            privatesubneta >> s3gatewayendpoint
            privatesubnetb >> s3gatewayendpoint
            privatesubnetc >> s3gatewayendpoint

            privatesubneta >> ecrendpoint
            privatesubnetb >> ecrendpoint
            privatesubnetc >> ecrendpoint

            privatesubneta >> ec2privateendpoint
            privatesubnetb >> ec2privateendpoint
            privatesubnetc >> ec2privateendpoint



    