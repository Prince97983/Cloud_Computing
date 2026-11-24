# Visitor Counter Web App — Cloud Computing Mini Project

**Stack:** Flask, Redis, Docker, Docker Compose, Kubernetes (Minikube), HPA  
**Hybrid cloud:** simulated locally using two Minikube profiles on one laptop.

## 1. Application
Each visit to `/` increments a Redis counter. `/api/count` returns JSON; `/health` is a health endpoint.

## 2. Requirements (Windows)
Install Docker Desktop, Minikube, kubectl, Git and Python only if you want to run Flask outside containers. Enable virtualization in BIOS and ensure Docker Desktop is running.

Verify:
```powershell
docker version
kubectl version --client
minikube version
```

## 3. Task A — Containerize (Docker Compose)
From this repository folder:
```powershell
docker compose up --build -d
docker compose ps
```
Open http://localhost:5000 and refresh; counter should increase. Verify:
```powershell
Invoke-RestMethod http://localhost:5000/api/count
docker compose logs web
```
Stop:
```powershell
docker compose down
```

## 4. Task B — Kubernetes on Minikube
Start cluster and enable metrics:
```powershell
minikube start --driver=docker
minikube addons enable metrics-server
```
Build image inside Minikube's Docker environment:
```powershell
minikube image build -t visitor-counter:1.0 .
```
Apply manifests:
```powershell
kubectl apply -f k8s.yaml
kubectl rollout status deployment/visitor-web -n visitor-counter
kubectl get pods,svc -n visitor-counter
```
Open app:
```powershell
kubectl port-forward -n visitor-counter svc/visitor-web 5000:5000
```
Visit http://localhost:5000. Capture pods/services screenshot.

### Self-healing evidence
```powershell
kubectl get pods -n visitor-counter
kubectl delete pod -n visitor-counter -l app=visitor-web
kubectl get pods -n visitor-counter -w
```
Capture before/after showing replacement pods.

## 5. Task C — HPA
```powershell
kubectl apply -f hpa.yaml
kubectl get hpa -n visitor-counter
```
In another terminal, port-forward the service (if not already running) and generate load. Use `scripts/load-test.ps1` or a controlled loop. Observe:
```powershell
kubectl get hpa,pods -n visitor-counter -w
```
HPA requires metrics-server. Capture HPA showing CPU and replica count. HPA may take a few minutes; the workload and laptop capacity affect scaling.

## 6. Task D — Hybrid cloud + failover simulation
Create a second independent cluster:
```powershell
minikube start -p minikube2 --driver=docker
minikube addons enable metrics-server -p minikube2
```
Build the image on cluster B and deploy:
```powershell
minikube image build -p minikube2 -t visitor-counter:1.0 .
kubectl --context=minikube2 apply -f k8s.yaml
kubectl --context=minikube2 rollout status deployment/visitor-web -n visitor-counter
```
The same namespace and manifests are deployed to both clusters. For a failover demonstration:
1. Confirm app works on primary (`kubectl --context=minikube ...`).
2. Confirm secondary works with `kubectl --context=minikube2 -n visitor-counter port-forward svc/visitor-web 5001:5000`.
3. Stop primary: `minikube stop -p minikube`.
4. Use secondary port-forward on 5000 (stop prior forwarding first) and refresh the app.
5. Capture cluster status and secondary working app.

**Report statement:** This is a local hybrid-cloud concept simulation. Two Minikube clusters run on one physical laptop; they are not two independent physical/cloud regions. Failover is manually switched for demonstration and is not automatic production failover. Redis data is not replicated between clusters in this basic project.

## 7. Task E — Cost/resource optimization (measure, do not fabricate)
Use at least three techniques and record actual values in `cost-analysis.csv`:
1. **Resource requests/limits:** bounded CPU/memory and scheduling predictability. Capture YAML and `kubectl top pods -n visitor-counter` before/after if you compare configurations.
2. **Small container image:** `python:3.12-slim`, no pip cache, non-root runtime. Record `docker images` image size versus your initial image.
3. **HPA:** keep minimum replicas during idle and scale under demand. Record replica count at baseline and load.
4. Optional: compare `docker compose` resource cap or remove unused packages.

Commands:
```powershell
docker images visitor-counter
kubectl top pods -n visitor-counter
kubectl get hpa -n visitor-counter
```
For cloud cost estimate, state provider, region, instance type, hourly price source/date and estimated hours. Since this runs locally, do not label laptop measurements as an actual cloud bill.

## 8. Evidence screenshots
Save screenshots in `screenshots/`:
- Docker containers running and browser counter
- Kubernetes deployments/pods/services
- Pod deletion and self-healing
- HPA under load showing replica scaling
- Both clusters listed and secondary app working after primary stopped
- Resource/image measurements

## 9. Submission contents
Include source files, YAMLs, screenshots, architecture diagram (`architecture.mmd`), filled cost-analysis CSV, report, and your public GitHub URL in `github_link.txt`. Download ZIP using GitHub Code → Download ZIP and upload it plus project files to faculty Drive.

## Cleanup
```powershell
kubectl delete -f hpa.yaml
kubectl delete -f k8s.yaml
minikube delete -p minikube2
minikube delete -p minikube
docker compose down -v
```
