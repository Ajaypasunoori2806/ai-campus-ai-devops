# 🚀 AI Campus Assistant – DevOps + AIOps Project

---

## 📌 Project Overview

This project demonstrates a **complete end-to-end DevOps pipeline** with **AIOps capabilities**.

It covers:

* CI/CD using GitHub Actions
* Containerization using Docker
* Deployment on Kubernetes (AKS)
* GitOps using ArgoCD
* Monitoring using Prometheus & Grafana
* AIOps (Anomaly Detection + Auto-Healing)

---

# 🏗️ Project Architecture

```
👨‍💻 Developer (You)
        │
        ▼
📦 GitHub Repository
        │
        ▼
⚙️ GitHub Actions (CI)
├── 🐳 Build Docker Image
├── 🧠 Code Validation
└── 📤 Push to ACR
        │
        ▼
📦 Azure Container Registry (ACR)
        │
        ▼
🚀 ArgoCD (GitOps CD)
        │
        ▼
☸️ AKS (Kubernetes Cluster)
├── 📄 K8s Manifests
├── 🤖 FastAPI App
└── 🌐 Ingress (Public Access)
        │
        ▼
📊 Monitoring Layer
├── 📈 Prometheus (Metrics)
└── 📉 Grafana (Dashboards)
        │
        ▼
🤖 AIOps Layer
├── 🔍 Anomaly Detection (Alerts)
├── ⚠️ Monitoring Analysis
└── 🔁 Auto-Healing (CronJob)
```

---

# ⚙️ STEP-BY-STEP IMPLEMENTATION

---

## 🔹 1. GitHub Repository Setup

* Created project repository
* Added application code
* Added `k8s/` folder for manifests

```bash
git init
git add .
git commit -m "initial commit"
git push
```

---

## 🔹 2. CI Pipeline (GitHub Actions)

### What happens:

* Code pushed → Workflow triggered
* Docker image built
* Image pushed to ACR

---

## 🔹 3. Azure Container Registry (ACR)

### Login:

```bash
docker login aiopsregistry123.azurecr.io -u USERNAME -p PASSWORD
```

---

## 🔹 4. Azure Setup

### Create Service Principal

```bash
az ad sp create-for-rbac \
  --name github-actions-sp \
  --role contributor \
  --scopes /subscriptions/<SUBSCRIPTION_ID> \
  --sdk-auth
```

---

## 🔹 5. AKS Cluster Creation

```bash
az aks create \
  --resource-group aiops-rg \
  --name aiops-aks \
  --node-count 1 \
  --enable-addons monitoring \
  --generate-ssh-keys
```

---

## 🔹 6. Connect to AKS

```bash
az aks get-credentials \
  --resource-group aiops-rg \
  --name aiops-aks
```

---

## 🔹 7. Attach ACR to AKS

```bash
az aks update \
  --name aiops-aks \
  --resource-group aiops-rg \
  --attach-acr aiopsregistry123
```

---

## 🔹 8. Kubernetes Deployment

Inside `k8s/`:

* deployment.yaml
* service.yaml
* ingress.yaml

Apply (initially):

```bash
kubectl apply -f k8s/
```

---

## 🔹 9. Verify Deployment

```bash
kubectl get pods
kubectl get svc
kubectl get ingress
```

---

## 🌐 10. Access Application

```
https://<EXTERNAL-IP>.nip.io
```

---

## 🔹 11. Install Monitoring (Prometheus + Grafana)

```bash
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo update

helm install monitoring prometheus-community/kube-prometheus-stack \
  -n monitoring --create-namespace
```

---

## 🔹 12. Access Grafana

```bash
kubectl port-forward svc/monitoring-grafana -n monitoring 3000:80
```

---

### Get Password (Windows PowerShell)

```powershell
[System.Text.Encoding]::UTF8.GetString(
[System.Convert]::FromBase64String(
(kubectl get secret monitoring-grafana -n monitoring -o jsonpath="{.data.admin-password}")
))
```

---

## 🔹 13. GitOps Setup (ArgoCD)

* Installed ArgoCD
* Connected GitHub repo
* Path used: `k8s/`

---

## 🔹 Enable Auto Sync

* Auto Sync ✅
* Self Heal ✅
* Prune ✅

---

## 🔹 Force Sync (if needed)

```bash
kubectl annotate application ai-campus \
  -n argocd \
  argocd.argoproj.io/refresh=hard --overwrite
```

---

# 🤖 AIOps IMPLEMENTATION

---

## 🔹 14. Anomaly Detection (Prometheus Rule)

📄 `k8s/aiops-alert.yaml`

```yaml
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  name: aiops-rules
  namespace: monitoring
spec:
  groups:
  - name: aiops.rules
    rules:
    - alert: PodRestartHigh
      expr: increase(kube_pod_container_status_restarts_total[1m]) > 1
      for: 1m
```

---

## 🔹 15. Auto-Healing (CronJob)

📄 `k8s/aiops-heal.yaml`

```yaml
apiVersion: batch/v1
kind: CronJob
metadata:
  name: aiops-healer
spec:
  schedule: "*/2 * * * *"
  jobTemplate:
    spec:
      template:
        spec:
          containers:
          - name: healer
            image: bitnami/kubectl
            command:
              - /bin/sh
              - -c
              - kubectl rollout restart deployment ai-campus-deployment
          restartPolicy: OnFailure
```

---

## 🔹 Deployment Flow (GitOps)

```bash
git add .
git commit -m "added aiops"
git push
```

👉 ArgoCD auto deploys changes

---

# 📊 Monitoring Flow

```
App → Metrics → Prometheus → Grafana → Dashboard
```

---

# 🔁 AIOps Flow

```
Pod issue → Prometheus Alert → Detection → CronJob → Auto-Heal
```

---

# 🧪 Testing

```bash
kubectl delete pod <pod-name>
```

👉 Pod recreated automatically
👉 System remains stable

---

# ❌ ERRORS FACED & FIXES

---

### 1. Docker Login Error

```
docker login requires at most 1 argument
```

✔ Fixed by correct syntax

---

### 2. ACR Unauthorized

```
authentication required
```

✔ Used correct credentials

---

### 3. PowerShell `< >` Issue

✔ Removed `< >` placeholders

---

### 4. Multi-line Command Errors

✔ Used single-line commands in PowerShell

---

### 5. VM Size Not Allowed

✔ Used supported VM size

---

### 6. Ingress Invalid Host

✔ Used correct format:

```
<IP>.nip.io
```

---

### 7. ArgoCD Not Syncing

✔ Enabled Auto Sync + Self Heal

---

### 8. base64 Not Working (Windows)

✔ Used PowerShell decoding

---

### 9. YAML Execution Error

✔ Understood YAML is not executable

---

### 10. Prometheus Rules Missing

✔ Added file to `k8s/` and pushed to Git

---

# 💸 CLEANUP (COST OPTIMIZATION)

```bash
az group delete --name aiops-rg --yes --no-wait
```

✔ Removed all billable resources

---

# 🎯 FINAL RESULT

✔ Fully automated CI/CD
✔ Kubernetes deployment
✔ GitOps workflow
✔ Monitoring + dashboards
✔ AIOps auto-healing

---

# 🧠 KEY LEARNING

This project covers:

* DevOps pipeline
* Kubernetes operations
* Monitoring systems
* GitOps principles
* Basic AIOps implementation

---

# 🚀 FUTURE IMPROVEMENTS

* Slack alerts
* AI log analysis
* Auto-scaling (HPA)
* Terraform automation

---

# 👨‍💻 AUTHOR

**Ajay Pasunoori**

---
