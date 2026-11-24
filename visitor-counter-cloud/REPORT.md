# Cloud Computing Mini Project Report
## Deploy a Visitor Counter Web App (Flask + Redis) on Docker and Kubernetes

**Student Name:** Prince Kumar  
**Roll Number:**2410031091
**Course:** Cloud Computing  
**Faculty:**Rohit Kumar
**GitHub Repository (Public):**

### Abstract
This project implements a web-based visitor counter using Flask and Redis. Docker packages the application, Docker Compose supports local multi-container execution, and Kubernetes deploys and manages the services. HPA demonstrates horizontal scaling. A two-Minikube-cluster setup simulates hybrid-cloud failover locally. Resource and image optimization techniques are evaluated using measurements collected during execution.

### Problem Statement
Build a small web application that counts visits while demonstrating containerization, orchestration, autoscaling, failover concepts, and resource optimization.

### Objectives
- Develop a Flask visitor counter backed by Redis.
- Containerize the application.
- Deploy web and database components on Kubernetes.
- Demonstrate pod self-healing and HPA.
- Simulate a primary/secondary hybrid-cloud arrangement.
- Measure at least three optimization techniques.

### Architecture
Insert the architecture diagram from `architecture.mmd` (render it using Mermaid-compatible Markdown preview or mermaid.live and save as PNG).

### Implementation
Describe `app.py`, Redis key `visitor_count`, Docker image, Compose configuration, Kubernetes Deployment/Services, probes, resource limits and HPA settings.

### Task-wise Demonstration
**Task 1 — Containerization:** Add Docker build/run screenshots and browser result.  
**Task 2 — Kubernetes:** Add deployment, pod, service and self-healing screenshots.  
**Task 3 — HPA:** Add HPA configuration and load-test/scale screenshots.  
**Task 4 — Hybrid cloud:** State that two Minikube clusters were simulated locally on one laptop. Explain manual failover and add primary-down/secondary-up evidence.  
**Task 5 — Cost optimization:** Add the completed `cost-analysis.csv` table and explain measurement conditions.

### Cost Optimization Results
| Technique | Before | After | Unit | Measurement |
|---|---:|---:|---|---|
| Resource requests/limits | Fill | Fill | CPU/Memory | kubectl output |
| Slim image/no pip cache | Fill | Fill | MB | docker images |
| HPA idle/load | Fill | Fill | replicas | kubectl get hpa |
| Optional fourth technique | Fill | Fill | Fill | Fill |

**Note:** Populate values from your actual laptop execution. Do not claim real cloud billing savings from a local simulation.

### Result
Write a brief summary of the features that successfully ran and attach actual screenshots.

### Limitations
The hybrid cloud is simulated locally; clusters share the same laptop and local resources. Failover is manually demonstrated. Redis persistence is local to each cluster and cross-cluster replication is not configured.

### Future Scope
- Deploy clusters in separate cloud regions.
- Add managed Redis with replication and backup.
- Implement automated traffic routing and health-based failover.
- Add monitoring with Prometheus and Grafana.
- Add CI/CD pipeline and secure image scanning.

### Conclusion
Summarize the practical learning in containerization, Kubernetes, autoscaling, failover simulation and optimization.
