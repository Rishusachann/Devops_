# 📘 DevOps & AWS EKS Master Practice Cheat Sheet
**Project Name:** InfraMind AI — Autonomous Cloud SRE Copilot  
**GitHub Repository:** [https://github.com/Rishusachann/Devops_](https://github.com/Rishusachann/Devops_)  
**Streamlit Deploy Link:** [https://share.streamlit.io/deploy?repository=Rishusachann/Devops_&branch=main&mainModule=streamlit_app.py](https://share.streamlit.io/deploy?repository=Rishusachann/Devops_&branch=main&mainModule=streamlit_app.py)  
**Date Created:** October 6, 2026  
**Author:** Aman Singh (`rishusinghsachan7878@gmail.com`)

---

## 📌 Table of Contents
1. [Architecture & Startup Strategy](#1-architecture--startup-strategy)
2. [Workspace File Structure](#2-workspace-file-structure)
3. [Step-by-Step Workflow Executed Today](#3-step-by-step-workflow-executed-today)
   - [Phase 1: Antigravity Codebase Generation](#phase-1-antigravity-codebase-generation)
   - [Phase 2: Git Identity & GitHub Push](#phase-2-git-identity--github-push)
   - [Phase 3: Streamlit Web Cloud App Setup](#phase-3-streamlit-web-cloud-app-setup)
   - [Phase 4: AWS CLI Configuration & Key Fix](#phase-4-aws-cli-configuration--key-fix)
   - [Phase 5: Docker Desktop & AWS ECR Image Push](#phase-5-docker-desktop--aws-ecr-image-push)
   - [Phase 6: EKS & Kubernetes Tooling Installation](#phase-6-eks--kubernetes-tooling-installation)
4. [Resume Guide for Next Session (AWS EKS Deployment)](#4-resume-guide-for-next-session-aws-eks-deployment)
5. [Useful Troubleshooting & Cheat Sheet Commands](#5-useful-troubleshooting--cheat-sheet-commands)

---

## 1. Architecture & Startup Strategy

### 🚀 Startup Concept: InfraMind AI
* **Value Proposition:** An autonomous AI SRE agent that monitors AWS CloudWatch & Kubernetes clusters, auto-detects pod crashes (OOMKilled, 504 timeouts), performs root cause analysis, generates Terraform patches, and auto-heals incidents.
* **Hypergrowth Playbook:** Inspired by Cursor, Cognition, Resend, and Supabase (0 to $100M+ ARR in 6–12 months).

### 🏗️ Workflow Diagram
```
[ Developer / SRE ]
       │
       ├──> [ Git Bash ] ──> Push Code ──> [ GitHub Repo (Rishusachann/Devops_) ]
       │                                            │
       │                                            ├──> [ Streamlit Cloud UI ]
       │                                            └──> [ GitHub Actions CI/CD ]
       │                                                        │
       ├──> [ Docker Desktop ] ──> Build Container              │
       │                                 │                      │
       │                                 v                      v
       └──> [ AWS CLI / ECR ] ──> Push Image ──> [ AWS EKS Cluster (k8s/) ]
```

---

## 2. Workspace File Structure

```
DEVOPS/
├── app/
│   ├── main.py                # FastAPI microservice with AI incident endpoints & fallback telemetry
│   └── templates/
│       └── index.html         # Live glassmorphism SRE Incident Dashboard UI
├── k8s/                       # Production Kubernetes Manifests
│   ├── namespace.yaml         # K8s Namespace (inframind)
│   ├── configmap.yaml         # App Configuration Environment Variables
│   ├── secret.yaml            # Database & API Key Secrets Template
│   ├── deployment.yaml        # Deployment specs (3 replicas, Liveness/Readiness probes)
│   ├── service.yaml           # ClusterIP Service routing
│   ├── ingress.yaml           # Nginx / AWS ALB Ingress Controller spec
│   └── hpa.yaml               # Horizontal Pod Autoscaler (CPU 75%, RAM 80%)
├── aws/                       # Terraform Infrastructure-as-Code
│   ├── main.tf                # AWS ECR, EKS Cluster, VPC, Subnet Terraform specs
│   ├── variables.tf           # Configurable AWS deployment variables
│   └── outputs.tf             # Terraform ECR & EKS output values
├── .github/workflows/
│   └── ci-cd.yml              # Production GitHub Actions pipeline for AWS ECR & EKS
├── scripts/
│   └── deploy.sh              # Bash script for local & cloud deployment automation
├── streamlit_app.py           # Streamlit Web App interface for 1-Click Cloud deployment
├── Dockerfile                 # Multi-stage production container build
├── docker-compose.yml         # Local development stack (App + Postgres + Redis)
├── requirements.txt           # Python dependencies
├── .gitignore                 # Standard Python, Docker, Terraform & OS ignore rules
├── README.md                  # Detailed startup documentation
└── DEVOPS_PRACTICE_CHEATSHEET.md # THIS REVISION SHEET
```

---

## 3. Step-by-Step Workflow Executed Today

### Phase 1: Antigravity Codebase Generation
- Built a complete production-ready microservice architecture in `c:\Users\rishu\OneDrive\Desktop\DEVOPS`.
- Created FastAPI server ([app/main.py](file:///c:/Users/rishu/OneDrive/Desktop/DEVOPS/app/main.py)) with endpoints:
  - `/` -> Live HTML Dashboard
  - `/health` -> Kubernetes Health Probe
  - `/metrics` -> Prometheus Telemetry
  - `/api/incidents` & `/api/remediate` -> AI Incident Management API
- Configured local container environment with [docker-compose.yml](file:///c:/Users/rishu/OneDrive/Desktop/DEVOPS/docker-compose.yml).

### Phase 2: Git Identity & GitHub Push
- Initialized local repository:
  ```bash
  git init
  git branch -M main
  ```
- Configured Git identity for commits:
  ```bash
  git config user.name "aman singh"
  git config user.email "rishusinghsachan7878@gmail.com"
  ```
- Connected GitHub remote repository with Personal Access Token (PAT):
  ```bash
  git remote add origin https://<YOUR_GITHUB_TOKEN>@github.com/Rishusachann/Devops_.git
  git add .
  git commit -m "feat: initial commit for InfraMind AI platform with K8s and AWS infrastructure"
  git push -u origin main
  ```
- Cleaned up token from local git remote URL for security:
  ```bash
  git remote set-url origin https://github.com/Rishusachann/Devops_.git
  ```

### Phase 3: Streamlit Web Cloud App Setup
- Created [streamlit_app.py](file:///c:/Users/rishu/OneDrive/Desktop/DEVOPS/streamlit_app.py) for interactive browser demonstration.
- Updated [requirements.txt](file:///c:/Users/rishu/OneDrive/Desktop/DEVOPS/requirements.txt) with `streamlit` & `pandas`.
- Pushed changes to GitHub repo.
- Generated 1-Click Streamlit Cloud Deploy Link:
  - `https://share.streamlit.io/deploy?repository=Rishusachann/Devops_&branch=main&mainModule=streamlit_app.py`

### Phase 4: AWS CLI Configuration & Key Fix
- Checked AWS CLI installation (`aws-cli/2.37.6` verified).
- Resolved `SignatureDoesNotMatch` authentication error by creating fresh AWS Access Keys in AWS IAM Console.
- Configured AWS CLI in Git Bash:
  ```bash
  aws configure
  # Access Key ID: <Your AWS Access Key>
  # Secret Access Key: <Your AWS Secret Key>
  # Default region: us-east-1
  # Output format: json
  ```
- Verified connection:
  ```bash
  aws sts get-caller-identity
  # Verified Account ID: 128793514319
  # ARN: arn:aws:iam::128793514319:root
  ```

### Phase 5: Docker Desktop & AWS ECR Image Push
- Started Docker Desktop application on Windows (`Docker Engine 29.6.1` running).
- Created AWS ECR repository:
  ```bash
  aws ecr create-repository --repository-name inframind-ai --region us-east-1
  ```
- Authenticated Docker daemon with AWS ECR:
  ```bash
  aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 128793514319.dkr.ecr.us-east-1.amazonaws.com
  ```
- Built, tagged, and pushed container image to AWS Cloud:
  ```bash
  docker build -t inframind-ai .
  docker tag inframind-ai:latest 128793514319.dkr.ecr.us-east-1.amazonaws.com/inframind-ai:latest
  docker push 128793514319.dkr.ecr.us-east-1.amazonaws.com/inframind-ai:latest
  ```
- Verified image upload in AWS ECR:
  - Image Tag: `latest`
  - Digest: `sha256:3752bb30ad6bd20ebfab557fabd9fcf82f7918e670c648e31d0a64eb7368c227`

### Phase 6: EKS & Kubernetes Tooling Installation
- Verified `kubectl` installation (`v1.36.1` ready).
- Downloaded and placed `eksctl` binary (`v0.231.0`) into Windows user PATH (`C:\Users\rishu\AppData\Local\Microsoft\WindowsApps\eksctl.exe`).
- Verified `eksctl version` command output: `0.231.0`.

---

## 4. Resume Guide for Next Session (AWS EKS Deployment)

When you return for your next practice session, follow these exact 3 steps:

### Step 1: Open Git Bash & Navigate to Folder
```bash
cd /c/Users/rishu/OneDrive/Desktop/DEVOPS
```

### Step 2: Create AWS EKS Cluster (1 Command)
```bash
eksctl create cluster --name inframind-cluster --region us-east-1 --nodegroup-name standard-workers --node-type t3.medium --nodes 2 --managed
```
*(Takes ~10–12 mins to provision VPC, Nodes, and EKS Control plane).*

### Step 3: Deploy Kubernetes Stack
```bash
# 1. Update k8s deployment manifest with your ECR Account ID
sed -i "s/<AWS_ACCOUNT_ID>/128793514319/g" k8s/deployment.yaml

# 2. Deploy to AWS EKS
kubectl apply -f k8s/namespace.yaml
kubectl apply -f k8s/configmap.yaml
kubectl apply -f k8s/secret.yaml
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
kubectl apply -f k8s/hpa.yaml

# 3. Check status & access app
kubectl get pods -n inframind
kubectl port-forward svc/inframind-service 8080:80 -n inframind
```
Open **`http://localhost:8080`** in your browser!

---

## 5. Useful Troubleshooting & Cheat Sheet Commands

| Action | Git Bash Command |
| :--- | :--- |
| **Check AWS Login** | `aws sts get-caller-identity` |
| **Check Docker Engine** | `docker info` |
| **Re-login to ECR** | `aws ecr get-login-password --region us-east-1 \| docker login --username AWS --password-stdin 128793514319.dkr.ecr.us-east-1.amazonaws.com` |
| **Check EKS Nodes** | `kubectl get nodes` |
| **Check K8s Pods** | `kubectl get pods -n inframind` |
| **Check Pod Logs** | `kubectl logs -f deployment/inframind-app -n inframind` |
| **Delete EKS Cluster** | `eksctl delete cluster --name inframind-cluster --region us-east-1` |
| **Git Push Updates** | `git add . && git commit -m "update code" && git push origin main` |

---
*Cheat Sheet saved locally at: `c:\Users\rishu\OneDrive\Desktop\DEVOPS\DEVOPS_PRACTICE_CHEATSHEET.md`*
