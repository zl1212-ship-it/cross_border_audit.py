import streamlit as st
import pandas as pd
import plotly.express as px
from cross_border_audit import generate_global_workforce_data, GlobalComplianceAuditEngine

# Set clean, simple styling parameters
st.set_page_config(page_title="CivicAI Auditor", page_icon="⚖️", layout="wide")
st.markdown("""
    <style>
    .stApp { background-color: #F8FAFC; color: #1E293B; font-family: -apple-system, sans-serif; }
    .gov-card { background-color: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 12px; padding: 24px; box-shadow: 0 1px 3px rgba(0,0,0,0.05); margin-bottom: 20px; }
    h1, h2, h3, h4 { color: #0F172A; font-weight: 600; }
    p, label { color: #475569 !important; font-size: 15px; }
    .logo-container { display: flex; align-items: center; gap: 12px; padding: 10px 0 25px 0; }
    .logo-mark { background-color: #2563EB; color: white; padding: 8px 14px; border-radius: 8px; font-weight: bold; font-size: 20px; }
    .logo-text { font-size: 22px; font-weight: 700; color: #0F172A; }
    .badge-clear { background-color: #EFF6FF; color: #2563EB; font-weight: 600; padding: 6px 12px; border-radius: 6px; font-size: 13px; display: inline-block; }
    .badge-alert { background-color: #FEF2F2; color: #DC2626; font-weight: 600; padding: 6px 12px; border-radius: 6px; font-size: 13px; display: inline-block; }
    .stTabs [data-baseweb="tab"] { color: #64748B; font-weight: 500; padding: 12px 20px; }
    .stTabs [aria-selected="true"] { color: #2563EB !important; border-bottom-color: #2563EB !important; }
    </style>
""", unsafe_allow_html=True)

# Logo banner
st.markdown("""
    <div class='logo-container'>
        <div class='logo-mark'>C</div>
        <div class='logo-text'>CivicAI <span style='color:#64748B; font-weight:400; font-size:16px;'>| AI Inspection Tool for Government Officials</span></div>
    </div>
""", unsafe_allow_html=True)

# Step 1 Section
st.markdown("### 🛠️ Step 1: Choose the Company Settings")
with st.container():
    st.markdown("<div class='gov-card'>", unsafe_allow_html=True)
    fc1, fc2, fc3 = st.columns(3)
    with fc1:
        target_company = st.selectbox("Which company do you want to audit?", ["All Registered Organizations", "AlphaLabs Intelligent Systems", "Horizon Automation Corp", "Nexus Predictive Tech"])
    with fc2:
        record_capacity = st.slider("How many employee files do you want to test?", 1000, 5000, 2500, step=500)
    with fc3:
        turnover_input = st.number_input("What is the company's yearly revenue? (USD)", value=500000000, step=50000000)
    st.markdown("</div>", unsafe_allow_html=True)

# Run calculations in the background
raw_data = generate_global_workforce_data(num_records=record_capacity, violation_severity=0.20)
engine = GlobalComplianceAuditEngine(raw_data, turnover=turnover_input)
audit_payload = engine.execute_complete_audit()

# Step 2 Section
st.markdown("### 📊 Step 2: View Safety Results")
m1, m2, m3 = st.columns(3)
with m1:
    st.markdown("<div class='gov-card'>", unsafe_allow_html=True)
    st.markdown("📈 **Total Files Checked**")
    st.subheader(f"{record_capacity:,}")
    st.markdown("<span class='badge-clear'>Scanning Active</span>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
    
with m2:
    st.markdown("<div class='gov-card'>", unsafe_allow_html=True)
    st.markdown("🇪🇺 **Safe Automation Check (Europe rules)**")
    eu_status = audit_payload.get("EU_AI_Act_2024", {}).get("Status", "VERIFIED COMPLIANT")
    is_fail = "VIOLATION" in eu_status
    st.subheader("Failed Test" if is_fail else "Passed Test")
    badge = "badge-alert" if is_fail else "badge-clear"
    st.markdown(f"<span class='{badge}'>{'Missing Human Control Over AI' if is_fail else 'AI is Safely Monitored'}</span>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

with m3:
    st.markdown("<div class='gov-card'>", unsafe_allow_html=True)
    st.markdown("🇺🇸 **Fair Hiring Check (United States rules)**")
    us_status = audit_payload.get("US_EEOC_4_5ths_Rule", {}).get("Status", "VERIFIED COMPLIANT")
    is_fail = "VIOLATION" in us_status
    st.subheader("Failed Test" if is_fail else "Passed Test")
    badge = "badge-alert" if is_fail else "badge-clear"
    st.markdown(f"<span class='{badge}'>{'Unfair Hiring Patterns Found' if is_fail else 'Hiring is Socially Fair'}</span>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# Step 3 Section
st.markdown("### 🔍 Step 3: Deep-Dive Into the Details")
tab1, tab2, tab3 = st.tabs(["📋 Clear Summary Report", "📊 Discrimination Chart", "🗄️ Raw Spreadsheet Logs"])

with tab1:
    st.markdown("<div class='gov-card'>", unsafe_allow_html=True)
    st.markdown("### Simple Rule Breakdown")
    for rule, data in audit_payload.items():
        friendly_name = "United States Fair Hiring Rule" if "EEOC" in rule else "European Union Safe AI Rule" if "EU" in rule else "Japan Workplace Quality Rule"
        st.markdown(f"#### 🌐 {friendly_name}")
        st.markdown(f"**Official Rule Source:** {data['Statutory_Source']}")
        st.json({k: v for k, v in data.items() if k not in ['Protocol', 'Statutory_Source', 'Status']})
        st.markdown("---")
    st.markdown("</div>", unsafe_allow_html=True)

with tab2:
    st.markdown("<div class='gov-card'>", unsafe_allow_html=True)
    st.markdown("### Fairness Score by Group (Should be above 0.80)")
    metrics = audit_payload.get("US_EEOC_4_5ths_Rule", {})
    ratios = metrics.get("Impact_Ratios", {})
    chart_df = pd.DataFrame(list(ratios.items()), columns=["Demographic Group", "Calculated Fairness Score"])
    
    fig = px.bar(chart_df, x="Demographic Group", y="Calculated Fairness Score", color_discrete_sequence=["#2563EB"], template="plotly_white")
    fig.add_hline(y=0.8, line_dash="dash", line_color="#DC2626", annotation_text="Minimum Allowed Fairness Line (0.80)")
    st.plotly_chart(fig, use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

with tab3:
    st.markdown("<div class='gov-card'>", unsafe_allow_html=True)
    st.markdown("### Official Regulatory Audit Ledger")
    st.markdown("This spreadsheet contains the exact details used during the automated scanning process.")
    st.dataframe(raw_data, use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)
