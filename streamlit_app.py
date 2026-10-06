import streamlit as st
import time
import random
import pandas as pd

# Page Configuration
st.set_page_config(
    page_title="InfraMind AI — Cloud & K8s SRE Copilot",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for Modern UI Styling
st.markdown("""
<style>
    .main {
        background-color: #090d16;
        color: #f1f5f9;
    }
    .stMetric {
        background-color: rgba(18, 24, 38, 0.7);
        border: 1px solid rgba(255, 255, 255, 0.08);
        padding: 16px;
        border-radius: 12px;
    }
    .stButton>button {
        background: linear-gradient(135deg, #00f2fe, #4facfe);
        color: #090d16;
        font-weight: 700;
        border: none;
        border-radius: 8px;
        padding: 8px 16px;
    }
    .badge-critical {
        background-color: rgba(255, 71, 87, 0.2);
        color: #ff4757;
        padding: 4px 8px;
        border-radius: 6px;
        font-weight: bold;
    }
    .badge-healed {
        background-color: rgba(46, 213, 115, 0.2);
        color: #2ed573;
        padding: 4px 8px;
        border-radius: 6px;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# Session State for Live Incidents
if "incidents" not in st.session_state:
    st.session_state.incidents = [
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

# Header Section
st.title("🚀 InfraMind AI — Autonomous Cloud SRE Copilot")
st.caption("Real-Time Autonomous Incident Remediation for AWS & Kubernetes Clusters")

st.divider()

# Top Metrics Row
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric(label="Active AWS EKS Nodes", value="6 Nodes", delta="100% Healthy")
with col2:
    st.metric(label="Monitored K8s Pods", value="48 Pods", delta="Zero CrashLoop")
with col3:
    st.metric(label="CPU / Memory Utilization", value="42% / 68%", delta="-14% Optimization")
with col4:
    st.metric(label="Monthly Cloud Cost Savings", value="$4,250", delta="Auto-Rightsized")

st.divider()

# Sidebar Control
with st.sidebar:
    st.header("⚙️ Agent Settings")
    st.success("🟢 AI Autonomous Mode: ACTIVE")
    st.info("AWS Region: us-east-1")
    st.info("Cluster: aws-eks-prod-v1.29")
    
    if st.button("🔄 Trigger Simulated Cluster Alert"):
        new_id = f"INC-{random.randint(9000, 9999)}"
        st.session_state.incidents.insert(0, {
            "id": new_id,
            "service": "k8s/checkout-api",
            "severity": "CRITICAL",
            "status": "DETECTED",
            "cluster": "aws-eks-us-east-1-prod",
            "issue": "504 Gateway Timeout - Connection Pool Exhausted",
            "detected_at": "Just now",
            "ai_recommendation": "Increase max_connections parameter & trigger autoscaling"
        })
        st.toast(f"New Alert Received: {new_id}!", icon="🚨")

# Main Content Tabs
tab1, tab2, tab3 = st.tabs(["🚨 Active Incidents & Auto-Healing", "🧠 AI Diagnostics & Root Cause", "📄 Terraform & Patch Generator"])

with tab1:
    st.subheader("Live Incidents Feed")
    
    for idx, inc in enumerate(st.session_state.incidents):
        with st.container():
            c1, c2, c3 = st.columns([3, 2, 1])
            with c1:
                is_healed = inc["status"] == "AUTO_HEALED"
                badge = f"🟢 {inc['status']}" if is_healed else f"🔴 {inc['status']}"
                st.markdown(f"### {inc['id']} — `{inc['service']}` ({badge})")
                st.write(f"**Issue:** {inc['issue']}")
                st.info(f"💡 **AI Recommendation:** {inc['ai_recommendation']}")
            with c2:
                st.write(f"**Cluster:** {inc['cluster']}")
                st.write(f"**Severity:** {inc['severity']}")
                st.write(f"**Time:** {inc['detected_at']}")
            with c3:
                if not is_healed:
                    if st.button(f"⚡ Auto-Heal", key=f"heal_{idx}"):
                        inc["status"] = "AUTO_HEALED"
                        inc["issue"] = f"[HEALED BY AI AGENT] {inc['issue']}"
                        st.toast(f"Successfully healed {inc['id']}!", icon="✅")
                        st.rerun()
                else:
                    st.success("✓ Healed")
            st.divider()

with tab2:
    st.subheader("AI Root Cause Analysis Engine")
    selected_inc = st.selectbox("Select Incident to Analyze:", [i["id"] for i in st.session_state.incidents])
    
    if st.button("🔍 Run Deep AI Diagnostic"):
        with st.spinner("Analyzing Kubernetes telemetry, pod logs & CloudWatch traces..."):
            time.sleep(1.2)
        
        st.success("Diagnostic Complete (Confidence Score: 96.8%)")
        st.markdown("""
        #### 📌 Primary Root Cause:
        Container process crashed due to memory leaks in worker thread allocation during peak traffic spike.
        
        #### 🛠️ Recommended Action Sequence:
        1. **Patch Kubernetes Deployment:** Increase container `memory.limit` from `512Mi` to `1Gi`.
        2. **GitOps Action:** Auto-submit Pull Request to `k8s/deployment.yaml`.
        3. **Traffic Rerouting:** Temporarily shift 15% traffic to fallback deployment zone.
        """)

with tab3:
    st.subheader("Auto-Generated Terraform Infrastructure Patch")
    st.code("""
# Auto-generated by InfraMind AI Agent
resource "kubernetes_deployment" "payment_gateway" {
  metadata {
    name      = "payment-gateway"
    namespace = "inframind"
  }
  spec {
    template {
      spec {
        container {
          name  = "payment-gateway-pod"
          image = "inframind-ai/payment:v2.1"
          resources {
            limits = {
              cpu    = "1000m"
              memory = "1024Mi" # Auto-scaled by InfraMind AI
            }
            requests = {
              cpu    = "500m"
              memory = "512Mi"
            }
          }
        }
      }
    }
  }
}
    """, language="hcl")

st.caption("Powered by InfraMind AI • Ready for Streamlit Community Cloud Deployment")
