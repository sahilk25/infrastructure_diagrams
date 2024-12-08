from diagrams import Cluster, Diagram
from diagrams.onprem.client import Users
from diagrams.saas.identity import Okta

from diagrams.k8s.compute import Pod, Job
from diagrams.k8s.network import Ing, SVC
from diagrams.k8s.rbac import SA, RB


with Diagram("Flask Okta K8s", show=False):
    users = Users("Internal Users")
    okta = Okta()
    with Cluster("GKE CLuster"):
        with Cluster("Namespace: flask-okta"):
            ingress = Ing("Ingress")
            service = SVC("Service")
            with Cluster("Deployment"):
                Okta_pods = [
                    Pod("pod"),
                    Pod("pod"),
                    Pod("pod")]
            with Cluster("rbac"):
                service_account = SA("service account")
                role_binding = RB("Rolebinding")
                service_account >> Okta_pods
                role_binding >> service_account
            ingress >> service >> Okta_pods
        with Cluster("Namespace: Jobs"):
            # jobs = [Job("sync Job"),
            #        Job("sync Job")]
            job = Job("sync job")
    users >> ingress
    okta >> Okta_pods
    Okta_pods >> job
    
