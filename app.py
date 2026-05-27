import streamlit as st
import pandas as pd
import plotly.express as px
from cross_border_audit import generate_global_workforce_data, GlobalComplianceAuditEngine

# Establish Light, High-Utility Theme Configuration
st.set_page_config(page_title="CivicAI Auditor", page_icon="⚖️", layout="wide")
st.markdown("""
    <style>
    /* Premium Minimal Light-Themed System Canvas */
    .stApp { background-color: #F8FAFC; color: #1E293B; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; }
    
    /* Clean Content Containment Cards */
    .gov-card {
        background-color: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-radius: 12px;
        padding: 24px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.05);
        margin-bottom: 20px;
    }
    
    /* Elegant Typography Alignment */
    h1, h2, h3, h4 { color: #0F172A; font-weight: 600; letter-spacing: -0.025em; }
    p, label { color: #475569 !important; font-size: 15px; }
    
    /* Distinctive Clean Corporate Branding Component */
    .logo-container { display: flex; align-items: center; gap: 12px; padding: 10px 0 25px 0; }
    .logo-mark { background-color: #2563EB; color: white; padding: 8px 14px; border-radius: 8px; font-weight: bold; font-size: 20px; letter-spacing: 1px; }
    .logo-text { font-size: 22px; font-weight: 700; color: #0F172A; }
    
    /* Unified Platform Status Highlights */
    .badge-clear { background-color: #EFF6FF; color: #2563EB; font-weight: 600; padding: 6px 12px; border-radius: 6px; font-size: 13px; display: inline-block; }
    .badge-alert { background-color: #FEF2F2; color: #DC2626; font-weight: 600; padding: 6px 12px; border-radius: 6px; font-size: 13px; display: inline-block; }
    
    /* Adjusting Native Streamlit Navigation Bar Elements */
    .stTabs [data-baseweb="tab"] { color: #64748B; font-weight: 500; padding: 12px 20px; }
    .stTabs [aria-selected="true"] { color: #2563EB !important; border-bottom-color: #2563EB !important; font-weight: 600; }
    </style>
""", unsafe_allow_html=True)

# Distinctive UI Branding Block
st.markdown("""
    <div class='logo-container'>
        <div class='logo-mark'>C</div>
        <div class='logo-text'>CivicAI <span style='color:#64748B; font-weight:400; font-size:16px;'>| Government Oversight Portal</span></div>
    </div>
""", unsafe_allow_html=True)

# Horizontal Filter Navigation Array for Government Officials
with st.container():
    st.markdown("<div class='gov-card'>", unsafe_allow_html=True)
    fc1, fc2, fc3 = st.columns(3)
    with fc1:
        target_company = st.selectbox("Select Regulated Enterprise Entity Target", ["All Registered Organizations", "AlphaLabs Intelligent Systems", "Horizon Automation Corp", "Nexus Predictive Tech"])
    with fc2:
        record_capacity = st.slider("Active Data Stream Sample Scale", 1000, 5000, 2500, step=500)
    with fc3:
        turnover_input = st.number_input("Registered Enterprise Global Turnover Baseline (USD)", value=500000000, step=50000000)
    st.markdown("</div>", unsafe_with_html=True)

# Execute core algorithms under-the-hood seamlessly
raw_data = generate_global_workforce_data(num_records=record_capacity, violation_severity=0.20)
engine = GlobalComplianceAuditEngine(raw_data, turnover=turnover_input)
audit_payload = engine.execute_complete_audit()

# Metrics Row Overview Panels
m1, m2, m3 = st.columns(3)
with m1:
    st.markdown("<div class='gov-card'>", unsafe_allow_html=True)
    st.markdown("📈 **Total Evaluated Ingestion Ledger Records**")
    st.subheader(f"{record_capacity:,}")
    st.markdown("<span class='badge-clear'>Pipeline Active</span>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
    
with m2:
    st.markdown("<div class='gov-card'>", unsafe_allow_html=True)
    st.markdown("🇪🇺 **EU AI Act Oversight Clearance Status**")
    eu_status = audit_payload.get("EU_AI_Act_2024", {}).get("Status", "VERIFIED COMPLIANT")
    st.subheader("Action Required" if "VIOLATION" in eu_status else "Compliant")
    badge = "badge-alert" if "VIOLATION" in eu_status else "badge-clear"
    st.markdown(f"<span class='{badge}'>{eu_status}</span>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

with m3:
    st.markdown("<div class='gov-card'>", unsafe_allow_html=True)
    st.markdown("🇺🇸 **U.S. EEOC Systemic Adverse Impact Metric**")
    us_status = audit_payload.get("US_EEOC_4_5ths_Rule", {}).get("Status", "VERIFIED COMPLIANT")
    st.subheader("Review Needed" if "VIOLATION" in us_status else "Passing")
    badge = "badge-alert" if "VIOLATION" in us_status else "badge-clear"
    st.markdown(f"<span class='{badge}'>{us_status}</span>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# Content Discovery Navigation Tabs
tab1, tab2, tab3 = st.tabs(["Compliance Scorecards", "Statistical Risk Maps", "Audit Source Data Ledger"])

with tab1:
    st.markdown("<div class='gov-card'>", unsafe_allow_html=True)
    st.markdown("### Statutory Audit Documentation Matrix")
    for rule, data in audit_payload.items():
        st.markdown(f"#### {rule.replace('_', ' ')}")
        st.markdown(f"**Legal Framework Reference Source:** {data['Statutory_Source']}")
        st.json({k: v for k, v in data.items() if k not in ['Protocol', 'Statutory_Source', 'Status']})
        st.markdown("---")
    st.markdown("</div>", unsafe_allow_html=True)

with tab2:
    st.markdown("<div class='gov-card'>", unsafe_allow_html=True)
    st.markdown("### Selection Index Disparities Chart")
    metrics = audit_payload.get("US_EEOC_4_5ths_Rule", {})
    ratios = metrics.get("Impact_Ratios", {})
    chart_df = pd.DataFrame(list(ratios.items()), columns=["Demographic Group", "Calculated Ratio"])
    
    # Render using the unified primary color strategy
    fig = px.bar(chart_df, x="Demographic Group", y="Calculated Ratio", color_discrete_sequence=["#2563EB"], template="plotly_white")
    fig.add_hline(y=0.8, line_dash="dash", line_color="#DC2626", annotation_text="EEOC Minimum Passing Index Limit (0.80)")
    st.plotly_chart(fig, use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

with tab3:
    st.markdown("<div class='gov-card'>", unsafe_allow_html=True)
    st.markdown("### Comprehensive Regulatory Inspection Log Ledger")
    st.dataframe(raw_data, use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)
