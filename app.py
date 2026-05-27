import streamlit as st
import pandas as pd
from cross_border_audit import generate_global_workforce_data, GlobalComplianceAuditEngine

st.set_page_config(page_title="Global AI Audit Dashboard", layout="wide")
st.title("🌐 Silicon Valley Transnational Statutory Compliance Insights Engine")

# Interactive Sidebar Configurations
st.sidebar.header("Configuration Matrices")
records = st.sidebar.slider("Audit Record Capacity", 500, 5000, 2500, step=500)
turnover = st.sidebar.number_input("Global Annual Turnover (USD)", value=500000000, step=50000000)

if st.sidebar.button("Execute Complete Audit"):
    df = generate_global_workforce_data(num_records=records)
    engine = GlobalComplianceAuditEngine(df, global_annual_turnover_usd=turnover)
    report = engine.execute_complete_audit()
    
    # Display Scorecards
    for protocol, data in report.items():
        with st.container():
            st.subheader(f"📡 Metric Bundle: {protocol}")
            st.caption(f"Framework Context: {data['Statutory_Source']}")
            
            status = data['Status']
            if "NON-COMPLIANT" in status:
                st.error(f"Audit Verdict: {status}")
            else:
                st.success(f"Audit Verdict: {status}")
                
            st.json({k: v for k, v in data.items() if k not in ['Protocol', 'Statutory_Source', 'Status']})
            st.markdown("---")
