# Local two-cluster failover demonstration (PowerShell).
# Cluster A = private-cloud simulation; Cluster B = public-cloud simulation.
# Both run the same application. This script switches the user-facing port-forward
# from primary to secondary. It is a demonstration, not production-grade global routing.

Write-Host "PRIMARY (cluster A) status:"
kubectl --context minikube -n visitor-counter get pods
Write-Host "SECONDARY (cluster B) status:"
kubectl --context minikube2 -n visitor-counter get pods

Write-Host "Stop primary cluster to simulate failure: minikube stop -p minikube"
Write-Host "Then open a NEW PowerShell window and run:"
Write-Host "kubectl --context minikube2 -n visitor-counter port-forward svc/visitor-web 5000:5000"
Write-Host "Open http://127.0.0.1:5000 to verify secondary service."
