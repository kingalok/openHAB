Alok_Sharma@EPGBLIVW0020 grafana % helm install grafana -n grafana --create-namespace grafana/grafana
 -f values.yaml 
I1220 09:37:33.341447   46823 request.go:601] Waited for 1.161292708s due to client-side throttling, not priority and fairness, request: GET:https://127.0.0.1:6443/apis/certificates.k8s.io/v1?timeout=32s
NAME: grafana
LAST DEPLOYED: Tue Dec 20 09:37:41 2022
NAMESPACE: grafana
STATUS: deployed
REVISION: 1
NOTES:
1. Get your 'admin' user password by running:

   kubectl get secret --namespace grafana grafana -o jsonpath="{.data.admin-password}" | base64 --decode ; echo

2. The Grafana server can be accessed via port 80 on the following DNS name from within your cluster:

   grafana.grafana.svc.cluster.local

   Get the Grafana URL to visit by running these commands in the same shell:
     export POD_NAME=$(kubectl get pods --namespace grafana -l "app.kubernetes.io/name=grafana,app.kubernetes.io/instance=grafana" -o jsonpath="{.items[0].metadata.name}")
     kubectl --namespace grafana port-forward $POD_NAME 3000

3. Login with the password from step 1 and the username: admin
#################################################################################
######   WARNING: Persistence is disabled!!! You will lose your data when   #####
######            the Grafana pod is terminated.                            #####
#################################################################################