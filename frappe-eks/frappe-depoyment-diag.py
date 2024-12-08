from diagrams import Cluster, Diagram
from diagrams.onprem.client import Users

from diagrams.k8s.compute import Pod
from diagrams.k8s.network import Ing, SVC

from diagrams.aws.compute import EKS
from diagrams.aws.database import RDS, RDSMariadbInstance, ElasticacheForRedis
from diagrams.aws.network import ALB
from diagrams.aws.storage import EFS
from diagrams.aws.security import WAF


with Diagram("Frappe in EKS", show=False):
    users = Users("Internal Users")
    with Cluster("AWS"):
        alb = ALB("Loadbalancer")
        waf = WAF("WAF")
        with Cluster("EKS CLuster"):
            eks = EKS()
            with Cluster("Namespace: frappe"):
                ingress = Ing("Ingress")
                service = SVC("Service")
                with Cluster("Deployment"):
                    frappe_pods = [
                        Pod("pod"),
                        Pod("pod"),
                        Pod("pod")]
        with Cluster("RDS"):
                mariadb = RDSMariadbInstance()
        with Cluster("Redis"):
                redis = ElasticacheForRedis()
        with Cluster("EFS"):
             efs =EFS("EFS")

    ingress >> service >> frappe_pods
    users >> waf >> alb >> ingress
    frappe_pods >> mariadb
    frappe_pods >> efs
    frappe_pods >> redis
    
