"""
Module: main
Description: Enterprise orchestration gate for the statutory auditing platform.
"""

import os
import json
import logging
from cross_border_audit import generate_global_workforce_data, GlobalComplianceAuditEngine

logger = logging.getLogger("ProductionOrchestrator")


def run_pipeline() -> None:
    # Scale-ready configurations pulled dynamically from environments
    RECORD_CAPacity = int(os.getenv("AUDIT_RECORD_CAPACITY", 2500))
    GLOBAL_TURNOVER = float(os.getenv("AUDIT_GLOBAL_TURNOVER", 500000000.0))
    OUTPUT_FILE = os.getenv("AUDIT_OUTPUT_JSON", "compliance_report.json")
    
    logger.info("Bootstrapping Silicon Valley Analytics Audit Runtime Environment...")
    
    # Execution Layer 1: Ingesting Data Frame Matrix
    dataframe = generate_global_workforce_data(num_records=RECORD_CAPacity)
    
    # Execution Layer 2: Pipeline Initialization
    engine = GlobalComplianceAuditEngine(dataframe, global_annual_turnover_usd=GLOBAL_TURNOVER)
    audit_report = engine.execute_complete_audit()
    
    # Execution Layer 3: Structuring High-Tech Terminal Visualization
    print("\n" + "="*80)
    print("      SILICON VALLEY TRANSNATIONAL STATUTORY COMPLIANCE INSIGHTS ENGINE")
    print("="*80)
    
    for protocol, analytical_block in audit_report.items():
        print(f"\n📡 [METRIC BUNDLE]: {protocol}")
        print(f"   └── Framework Context: {analytical_block.get('Statutory_Source')}")
        
        status = analytical_block.get("Status", "UNKNOWN")
        status_color = "\033[92mCOMPLIANT\033[0m" if "COMPLIANT" in status and "NON" not in status else f"\033[91m{status}\033[0m"
        print(f"   └── Audit Verdict    : {status_color}")
        
        print("   └── Analytical Extractions:")
        for metric_key, val in analytical_block.items():
            if metric_key not in ['Protocol', 'Statutory_Source', 'Status']:
                print(f"       ├── {metric_key}: {val}")
                
    print("\n" + "="*80)
    
    # Execution Layer 4: Exporting structural records for Web/App frontends
    try:
        with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
            json.dump(audit_report, f, indent=4)
        logger.info(f"Production data payload successfully cached to absolute disk path: '{OUTPUT_FILE}'")
    except IOError as e:
        logger.error(f"DISK ACCESSIBILITY FAIL - Unable to write data payload: {str(e)}")


if __name__ == "__main__":
    run_pipeline()
