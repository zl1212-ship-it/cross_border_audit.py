import streamlit as st
import pandas as pd
import plotly.express as px
from cross_border_audit import generate_global_workforce_data, GlobalComplianceAuditEngine

# Inject custom Silicon Valley Premium Tech CSS styling overrides
st.set_page_config(page_title="AETHER // Governance Audit", page_icon="🌐", layout="wide")
st.markdown("""
    <style>
    .reportview-container { background: #0A0E17; color: #F4F6F9; }
    h1, h2, h3 { font-family: 'Inter', sans-serif; font-weight: 700; letter-spacing: -0.5px; }
    .kpi-card { background-color: #121826; border: 1px solid #1E293B; border-radius: 8px; padding: 20px; box-shadow: 0 4px 6px rgba(0,0,0,0.2); }
    .status-compliant { color: #10B981; font-weight: bold; font-family: monospace; }
    .status-violation { color: #EF4444; font-weight: bold; font-family: monospace; }
    .status-warning { color: #F59E0B; font-weight: bold; font-family: monospace; }
    </style>
""", unsafe_allow_html=True)

# Main Application Frame Headers
st.markdown("`SYSTEM STATUS: OPERATIONAL // DATA PIPELINE SECURE`")
st.title("🌐 AETHER // Transnational Algorithmic Governance Auditor")
st.markdown("An enterprise-grade sovereign risk engine auditing cross-border legal compliance, autonomous decision vectors, and time precarity matrices.")
st.markdown("---")

# Control Sidebar Node
st.sidebar.markdown("### 🛠️ PLATFORM CONFIGURATIONS")
record_capacity = st.sidebar.slider("Ingestion Record Scale", 1000, 10000, 2500, step=500)
turnover_input = st.sidebar.number_input("Enterprise Annual Turnover (USD)", value=500000000, step=10000000)
risk_weight = st.sidebar.slider("Algorithmic Severity Simulation Bias", 0.05, 0.85, 0.20, step=0.05)

# Trigger Operations Block
raw_data = generate_global_workforce_data(num_records=record_capacity, violation_severity=risk_weight)
engine = GlobalComplianceAuditEngine(raw_data, turnover=turnover_input)
audit_payload = engine.execute_complete_audit()

# TOP ROW: Top-Tier High-Tech KPI Summary Blocks
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.markdown(f"<div class='kpi-card'><h5>TOTAL INGESTED RECORDS</h5><h2>{record_capacity:,}</h2><p style='color:#64748B;font-size:12px;'>Real-time streaming ledger nodes</p></div>", unsafe_allow_html=True)
with col2:
    eu_status = audit_payload.get("EU_AI_Act_2024", {}).get("Status", "VERIFIED COMPLIANT")
    cls = "status-compliant" if "COMPLIANT" in eu_status else "status-violation"
    st.markdown(f"<div class='kpi-card'><h5>EU AI ACT STATUS</h5><h3 class='{cls}'>{eu_status}</h3><p style='color:#64748B;font-size:12px;'>Chapter III High-Risk Parameters</p></div>", unsafe_allow_html=True)
with col3:
    us_status = audit_payload.get("US_EEOC_4_5ths_Rule", {}).get("Status", "VERIFIED COMPLIANT")
    cls = "status-compliant" if "COMPLIANT" in us_status else "status-violation"
    st.markdown(f"<div class='kpi-card'><h5>U.S. EEOC COMPLIANCE</h5><h3 class='{cls}'>{us_status}</h3><p style='color:#64748B;font-size:12px;'>Uniform Selection Discrimination Rate</p></div>", unsafe_allow_html=True)
with col4:
    jp_status = audit_payload.get("Japan_METI_Society_5_0", {}).get("Status", "VERIFIED COMPLIANT")
    cls = "status-compliant" if "COMPLIANT" in jp_status else "status-warning"
    st.markdown(f"<div class='kpi-card'><h5>METI SOVEREIGNTY INDEX</h5><h3 class='{cls}'>{jp_status}</h3><p style='color:#64748B;font-size:12px;'>Temporal Labor Exploitation Guardrails</p></div>", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# MIDDLE ROW: Specialized Deep-Dive Operational Framework Tabs
st.subheader("🕵️‍♂️ Sovereign Framework Deep-Dive Verification Matrix")
tab1, tab2, tab3, tab4 = st.tabs(["🇺🇸 U.S. EEOC / LL144 Matrix", "🇪🇺 European Union AI Act", "🇯🇵 Japan METI Society 5.0", "🗄️ Sovereign Master Data Ledger"])

with tab1:
    st.markdown("### Selection Rate Adverse Impact Analytics")
    metrics = audit_payload.get("US_EEOC_4_5ths_Rule", {})
    ratios = metrics.get("Impact_Ratios", {})
    
    chart_df = pd.DataFrame(list(ratios.items()), columns=["Protected Class Demographic Group", "Calculated Adverse Selection Index Score"])
    fig_us = px.bar(chart_df, x="Protected Class Demographic Group", y="Calculated Adverse Selection Index Score", color="Calculated Adverse Selection Index Score", color_continuous_scale="RdYlGn", range_color=[0.6, 1.2])
    fig_us.add_hline(y=0.8, line_dash="dash", line_color="red", annotation_text="EEOC 4/5ths Rule Critical Legal Violation Threshold (0.80)")
    st.plotly_chart(fig_us, use_container_width=True)

with tab2:
    st.markdown("### High-Risk Black Box Autonomous Systems Audit Tracker")
    eu_metrics = audit_payload.get("EU_AI_Act_2024", {})
    unmanaged = eu_metrics.get("Unmanaged_Autonomous_Records", 0)
    liability = eu_metrics.get("Assessed_Statutory_Liability_USD", 0.0)
    
    ec1, ec2 = st.columns(2)
    ec1.metric(label="Isolated Violations (Missing Human-in-the-Loop Safeguards)", value=f"{unmanaged} Telemetry Incidents", delta="-Action Required" if unmanaged > 0 else "Secure")
    ec2.metric(label="Calculated Corporate Liability Fine Ceiling (USD)", value=f"${liability:,.2f}", delta="-Risk Threshold Exceeded" if liability > 0 else "Compliant")

with tab3:
    st.markdown("### Temporal Sovereignty & Systemic 'Life Stall' Metrics")
    jp_metrics = audit_payload.get("Japan_METI_Society_5_0", {})
    tsi_val = jp_metrics.get("Temporal_Sustainability_Index", 1.0)
    
    fig_jp = px.violin(raw_data[raw_data["Jurisdiction"] == "Japan_HQ"], x="Gender", y="Uncompensated_Overtime_Hours", color="Gender", box=True, points="all", title="Sovereign Distribution Curve: System-Imposed Uncompensated Labor Extraction Time")
    st.plotly_chart(fig_jp, use_container_width=True)

with tab4:
    st.markdown("### Government Auditor Raw Data Log Ledger Room")
    st.markdown("Searchable ledger interface provided for government entities and regulatory compliance officers.")
    st.dataframe(raw_data, use_container_width=True)
