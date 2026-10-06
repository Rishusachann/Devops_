import os
import time
import random
from typing import List, Dict, Any
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
try:
    from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
    HAS_PROMETHEUS = True
except ImportError:
    HAS_PROMETHEUS = False
    Counter = None
    Histogram = None
    generate_latest = None
    CONTENT_TYPE_LATEST = "text/plain"

app = FastAPI(
    title="InfraMind AI — Autonomous Cloud & K8s SRE Platform",
    version="1.0.0",
    description="Hypergrowth AI Agent for AWS Incident Remediation & Cloud Ops"
)

# Setup Template Directory
TEMPLATES_DIR = os.path.join(os.path.dirname(__file__), "templates")
templates = Jinja2Templates(directory=TEMPLATES_DIR)

# Prometheus Metrics Definition
if HAS_PROMETHEUS:
    REQUEST_COUNT = Counter("http_requests_total", "Total HTTP Request Count", ["method", "endpoint", "status"])
    REQUEST_LATENCY = Histogram("http_request_duration_seconds", "HTTP Request Latency", ["endpoint"])
else:
    REQUEST_COUNT = None
    REQUEST_LATENCY = None

# Simulated Live Incident In-Memory State
MOCK_INCIDENTS = [
    {
        "id": "INC-8902",
        "service": "k8s/payment-gateway-pod",
        "severity": "CRITICAL",
        "status": "DETECTED",
        "cluster": "aws-eks-us-east-1-prod",
        "issue": "OOMKilled - Memory Limit Exceeded (512Mi / 512Mi)",
        "detected_at": "2 mins ago",
        "ai_recommendation": "Scale pod memory request to 1GiB & generate Terraform patch PR #412"
    },
    {
        "id": "INC-8903",
        "service": "aws/cloudwatch-rds-latency",
        "severity": "HIGH",
        "status": "ANALYZING",
        "cluster": "aws-rds-aurora-cluster",
        "issue": "Database IOPS Bottleneck (Buffer cache hit ratio < 82%)",
        "detected_at": "5 mins ago",
        "ai_recommendation": "Enable Auto-scaling Storage & Provisioned IOPS (io2)"
    },
    {
        "id": "INC-8904",
        "service": "k8s/auth-service-hpa",
        "severity": "MEDIUM",
        "status": "AUTO_HEALED",
        "cluster": "aws-eks-us-east-1-prod",
        "issue": "High CPU Spike (94% utilization)",
        "detected_at": "18 mins ago",
        "ai_recommendation": "HPA triggered automatically: scaled pods 3 -> 8"
    }
]

class RemediationRequest(BaseModel):
    incident_id: str
    action: str

@app.middleware("http")
async def monitor_requests(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    duration = time.time() - start_time
    
    if HAS_PROMETHEUS and REQUEST_COUNT and REQUEST_LATENCY:
        endpoint = request.url.path
        REQUEST_COUNT.labels(method=request.method, endpoint=endpoint, status=response.status_code).inc()
        REQUEST_LATENCY.labels(endpoint=endpoint).observe(duration)
    
    return response

@app.get("/", response_class=HTMLResponse)
async def serve_dashboard(request: Request):
    """Renders the SRE AI Agent Live Dashboard UI"""
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/health")
async def health_check():
    """Kubernetes Readiness & Liveness Probe Endpoint"""
    return {
        "status": "healthy",
        "timestamp": int(time.time()),
        "version": "1.0.0",
        "environment": os.getenv("ENVIRONMENT", "development"),
        "k8s_node": os.getenv("HOSTNAME", "local-docker-node")
    }

@app.get("/metrics")
async def metrics():
    """Prometheus Scrape Endpoint"""
    if HAS_PROMETHEUS:
        return HTMLResponse(content=generate_latest(), media_type=CONTENT_TYPE_LATEST)
    return JSONResponse({"status": "Prometheus metrics client not installed"})


@app.get("/api/incidents")
async def get_incidents():
    """Returns active AWS & K8s cluster incidents"""
    return {"incidents": MOCK_INCIDENTS}

@app.get("/api/cloud-status")
async def get_cloud_status():
    """Simulates real-time status of AWS & K8s infra nodes"""
    return {
        "aws_region": os.getenv("AWS_REGION", "us-east-1"),
        "eks_clusters": 2,
        "active_pods": 48,
        "healthy_nodes": 6,
        "cpu_utilization": f"{random.randint(35, 68)}%",
        "memory_utilization": f"{random.randint(52, 79)}%",
        "cost_savings_monthly": "$4,250",
        "ai_agent_status": "ONLINE (Autonomous Mode Active)"
    }

@app.post("/api/analyze")
async def analyze_incident(data: Dict[str, Any]):
    """AI Root Cause Analysis Engine Endpoint"""
    incident_id = data.get("incident_id", "INC-0000")
    time.sleep(0.5) # Simulate AI inference latency
    
    return {
        "incident_id": incident_id,
        "root_cause": "Microservice container failed due to unhandled memory leak in transaction pipeline.",
        "confidence_score": 0.96,
        "suggested_actions": [
            "Apply K8s Deployment patch to increase memory limits",
            "Trigger automated rollback to last stable Git SHA (a7f29b4)",
            "Submit Slack notification with diagnostic stacktrace"
        ]
    }

@app.post("/api/remediate")
async def remediate_incident(req: RemediationRequest):
    """Triggers automated auto-healing / kubectl / terraform fix"""
    for inc in MOCK_INCIDENTS:
        if inc["id"] == req.incident_id:
            inc["status"] = "AUTO_HEALED"
            inc["issue"] = f"[HEALED BY AI AGENT] {inc['issue']}"
            return {
                "success": True,
                "message": f"Successfully executed remediation for {req.incident_id}. Applied fix: {req.action}",
                "incident": inc
            }
    raise HTTPException(status_code=404, detail="Incident ID not found")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
