import streamlit as st
import pandas as pd
import plotly.express as px
from cross_border_audit import generate_global_workforce_data, GlobalComplianceAuditEngine

# Injected 2026 High-Tech Neon Cyberpunk Structural CSS Overrides
st.set_page_config(page_title="AETHER // TRANSNATIONAL GOV", page_icon="⚡", layout="wide")
st.markdown("""
    <style>
    @import url('https://googleapis.com');
    
    /* Core Platform Structural Theme */
    .stApp { background: #05070B; color: #E2E8F0; font-family: 'Space Grotesk', sans-serif; }
    
    /* Cyber Grid Matrix Header Cards */
    .cyber-card { 
        background: linear-gradient(135deg, #0D1321 0%, #080B14 100%); 
        border-left: 4px solid #00F0FF; 
        border-top: 1px solid #1E293B;
        border-right: 1px solid #1E293B;
        border-bottom: 1px solid #1E293B;
        border-radius: 4px; padding: 24px; 
        box-shadow: 0 8px 32px rgba(0, 240, 255, 0.03); 
    }
    .cyber-card.violation { border-left-color: #FF0055; box-shadow: 0 8px 32px rgba(255, 0, 85, 0.03); }
    .cyber-card.warning { border-left-color: #FFB800; box-shadow: 0 8px 32px rgba(255, 184, 0, 0.03); }
    
    /* Technical Text Styling */
    h1, h2, h3, h4 { font-family: 'Space Grotesk', sans-serif; font-weight: 700; text-transform: uppercase; letter-spacing: -0.5px; }
    code, .stMarkdown pre, p.mono { font-family: 'JetBrains Mono', monospace; font-size: 13px; color: #A0AEC0; }
    
    /* Streamlit Interactive Component Adjustments */
    .stTabs [data-baseweb="tab-list"] { gap: 8px; background-color: transparent; }
    .stTabs [data-baseweb="tab"] { 
        background-color: #0D1321; border: 1px solid #1E293B; color: #718096; 
        border-radius: 4px; padding: 12px 24px; font-family: 'JetBrains Mono', monospace; 
    }
    .stTabs [aria-selected="true"] { background-color: #00F0FF !important; color: #05070B !important; font-weight: bold; }
    </style>
""", unsafe_allow_html=True)

# Main Application System Stream Header
st.markdown("<p class='mono' style='color:#00F0FF; margin-bottom:0;'>// CORE SECURE NODE_ NODE-ID: AETHER-UX-2026 // STATUS: ACTIVE</p>", unsafe_allow_html=True)
st.title("⚡ AETHER // ALGORITHMIC GOVERNANCE AUDITOR")
st.markdown("A cutting-edge sovereign risk workspace evaluating machine bias, tracking time precarity profiles, and enforcing cross-border legal compliance parameters.")
st.markdown("---")

# Control Sidebar Configuration Block
st.sidebar.markdown("### `// SET PARAMETERS`")
record_capacity = st.sidebar.slider("TELEMETRY INGESTION CAPACITY", 1000, 10000, 3000, step=500)
turnover_input = st.sidebar.number_input("GLOBAL ANNUAl TURNOVER (USD)", value=750000000, step=50000000)
risk_weight = st.sidebar.slider("SIMULATED EXTRACTION INTENSITY", 0.05, 0.85, 0.35, step=0.05)

# Execute Computational Analytics Engine Pipelines
raw_data = generate_global_workforce_data(num_records=record_capacity, violation_severity=risk_weight)
engine = GlobalComplianceAuditEngine(raw_data, turnover=turnover_input)
audit_payload = engine.execute_complete_audit()

# TOP ROW: Cyber High-Contrast KPI Cards
c1, c2, c3, c4 = st.columns(4)
with c1:
    st.markdown(f"<div class='cyber-card'><code style='color:#00F0FF;'>[NODE_INGEST]</code><h5 style='margin:10px 0 5px 0;'>LEDGER TELEMETRY</h5><h2>{record_capacity:,}</h2></div>", unsafe_allow_html=True)
with c2:
    eu_status = audit_payload.get("EU_AI_Act_2024", {}).get("Status", "VERIFIED COMPLIANT")
    v_class = "violation" if "VIOLATION" in eu_status else ""
    st.markdown(f"<div class='cyber-card {v_class}'><code style='color:#FF0055;'>[EU_AI_ACT]</code><h5 style='margin:10px 0 5px 0;'>EUROPEAN MATRIX</h5><h4>{eu_status}</h4></div>", unsafe_allow_html=True)
with c3:
    us_status = audit_payload.get("US_EEOC_4_5ths_Rule", {}).get("Status", "VERIFIED COMPLIANT")
    v_class = "violation" if "VIOLATION" in us_status else ""
    st.markdown(f"<div class='cyber-card {v_class}'><code style='color:#00FF66;'>[US_EEOC]</code><h5 style='margin:10px 0 5px 0;'>DISCRIMINATION RISK</h5><h4>{us_status}</h4></div>", unsafe_allow_html=True)
with c4:
    jp_status = audit_payload.get("Japan_METI_Society_5_0", {}).get("Status", "VERIFIED COMPLIANT")
    w_class = "warning" if "WARNING" in jp_status else ""
    st.markdown(f"<div class='cyber-card {w_class}'><code style='color:#FFB800;'>[METI_S5]</code><h5 style='margin:10px 0 5px 0;'>TEMPORAL LABOR INDEX</h5><h4>{jp_status}</h4></div>", unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# LOWER ROW: Tabbed Analytics Views
st.subheader("`// AUDIT DISCOVERY TIERS`")
tab1, tab2, tab3, tab4 = st.tabs(["[US_EEOC_BIAS]", "[EU_AI_OVERSIGHT]", "[JP_TIME_SOVEREIGNTY]", "[RAW_LEDGER_STREAM]"])

with tab1:
    st.markdown("### Systemic Selection Trends Matrix")
    metrics = audit_payload.get("US_EEOC_4_5ths_Rule", {})
    ratios = metrics.get("Impact_Ratios", {})
    chart_df = pd.DataFrame(list(ratios.items()), columns=["Demographic Group", "Selection Metric Ratio"])
    
    fig_us = px.bar(chart_df, x="Demographic Group", y="Selection Metric Ratio", color="Selection Metric Ratio", 
                    color_continuous_scale=["#FF0055", "#00FF66"], template="plotly_dark")
    fig_us.add_hline(y=0.8, line_dash="dash", line_color="#FF0055", annotation_text="EEOC Statuary Cutoff Threshold (0.80)")
    st.plotly_chart(fig_us, use_container_width=True)

with tab2:
    st.markdown("### Automated Accountability Framework Violations")
    eu_metrics = audit_payload.get("EU_AI_Act_2024", {})
    unmanaged = eu_metrics.get("Unmanaged_Autonomous_Records", 0)
    liability = eu_metrics.get("Assessed_Statutory_Liability_USD", 0.0)
    
    ec1, ec2 = st.columns(2)
    ec1.metric(label="Isolated Non-Compliant High-Risk Records", value=f"{unmanaged} Telemetry Hits")
    ec2.metric(label="Calculated Liability Fine Ceiling (USD)", value=f"${liability:,.2f}")

with tab3:
    st.markdown("### Labor Extraction Curves & The 'Life Stall'")
    fig_jp = px.violin(raw_data[raw_data["Jurisdiction"] == "Japan_HQ"], x="Gender", y="Uncompensated_Overtime_Hours", 
                       color="Gender", box=True, points="all", template="plotly_dark", color_discrete_sequence=["#00F0FF", "#FF0055", "#FFB800"])
    st.plotly_chart(fig_jp, use_container_width=True)

with tab4:
    st.markdown("### Ingested Data Stream Records")
    st.dataframe(raw_data, use_container_width=True)
