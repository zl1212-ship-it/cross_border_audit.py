from fastapi import FastAPI, HTTPException, Depends, Security
from fastapi.security import OAuth2PasswordBearer
from fastapi.responses import HTMLResponse
from pydantic import BaseModel, Field
import os
import asyncio

ENV_STAGE = os.getenv("APP_ENV", "production")
ALLOWED_HOST = os.getenv("API_GATEWAY_HOST", "api.governance.internal")

app = FastAPI(
    title="Quantum Governance Audit Engine",
    version="3.0.0",
    docs_url=None if ENV_STAGE == "production" else "/docs",
    redoc_url=None
)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="v1/auth/token")

async def verify_auditor_credentials(token: str = Depends(oauth2_scheme)):
    if not token or len(token) < 32:
        raise HTTPException(status_code=401, detail="Invalid token vector.")
    return {"scope": "compliance:write"}

class EnterpriseAuditPayload(BaseModel):
    selection_ratio_group_a: float = Field(..., ge=0.0, le=1.0)
    selection_ratio_group_b: float = Field(..., ge=0.0, le=1.0)
    unvalidated_autonomous_incidents: int = Field(..., ge=0)
    uncompensated_alignment_hours: float = Field(..., ge=0.0)
    total_contract_hours: float = Field(..., gt=0.0)

@app.get("/", response_class=HTMLResponse, tags=["Visual Interface Gateway"])
async def render_futuristic_hud():
    """Renders a 2030 glassmorphic cybersecurity compliance heads-up-display."""
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Quantum Governance Engine // HUD v3.0</title>
        <script src="https://tailwindcss.com"></script>
        <style>
            @import url('https://googleapis.com');
            body {
                background: radial-gradient(circle at 50% 50%, #060b19 0%, #02040a 100%);
                font-family: 'Rajdhani', sans-serif;
                overflow-x: hidden;
            }
            .cyber-panel {
                background: rgba(6, 11, 25, 0.65);
                backdrop-filter: blur(20px);
                border: 1px solid rgba(0, 242, 254, 0.2);
                box-shadow: 0 0 40px rgba(0, 242, 254, 0.05), inset 0 0 20px rgba(0, 242, 254, 0.05);
            }
            .glow-text {
                font-family: 'Orbitron', sans-serif;
                text-shadow: 0 0 15px rgba(0, 242, 254, 0.6);
            }
            .neon-border-pulse {
                animation: pulse 4s infinite alternate;
            }
            @keyframes pulse {
                0% { border-color: rgba(0, 242, 254, 0.2); box-shadow: 0 0 20px rgba(0, 242, 254, 0.05); }
                100% { border-color: rgba(0, 242, 254, 0.6); box-shadow: 0 0 40px rgba(0, 242, 254, 0.2); }
            }
        </style>
    </head>
    <body class="text-slate-200 min-h-screen p-8 flex flex-col justify-between">
        <header class="w-full max-w-7xl mx-auto flex justify-between items-center border-b border-cyan-500/20 pb-4 mb-8">
            <div>
                <h1 class="glow-text text-2xl font-bold tracking-widest text-cyan-400">QUANTUM_GOVERNANCE_ENGINE</h1>
                <p class="text-xs text-cyan-500/60 uppercase tracking-widest mt-1">Status: Operational // Node: Host_api.governance.internal</p>
            </div>
            <div class="flex items-center space-x-4">
                <span class="inline-block w-2 h-2 rounded-full bg-emerald-400 animate-ping"></span>
                <span class="text-xs font-mono text-emerald-400 tracking-wider">SECURE MESH LINK ACTIVE</span>
            </div>
        </header>

        <main class="w-full max-w-7xl mx-auto grid grid-cols-1 lg:grid-cols-3 gap-8 items-stretch flex-grow">
            <section class="cyber-panel neon-border-pulse rounded-xl p-6 flex flex-col justify-between lg:col-span-1">
                <div>
                    <h2 class="text-sm font-bold tracking-widest text-cyan-400 uppercase mb-6 border-b border-cyan-500/10 pb-2">// Control Vector Inputs</h2>
                    <form class="space-y-5 text-sm">
                        <div>
                            <label class="block text-xs uppercase text-slate-400 tracking-wider mb-2">Selection Ratio Group A</label>
                            <input type="number" step="0.0001" value="0.7412" class="w-full bg-slate-950/80 border border-cyan-500/30 rounded px-3 py-2 text-cyan-400 focus:outline-none focus:border-cyan-400 font-mono">
                        </div>
                        <div>
                            <label class="block text-xs uppercase text-slate-400 tracking-wider mb-2">Selection Ratio Group B</label>
                            <input type="number" step="0.0001" value="0.6845" class="w-full bg-slate-950/80 border border-cyan-500/30 rounded px-3 py-2 text-cyan-400 focus:outline-none focus:border-cyan-400 font-mono">
                        </div>
                        <div>
                            <label class="block text-xs uppercase text-slate-400 tracking-wider mb-2">Unvalidated Incidents (EU AI Act)</label>
                            <input type="number" value="3" class="w-full bg-slate-950/80 border border-cyan-500/30 rounded px-3 py-2 text-cyan-400 focus:outline-none focus:border-cyan-400 font-mono">
                        </div>
                        <div>
                            <label class="block text-xs uppercase text-slate-400 tracking-wider mb-2">Uncompensated Alignment Hours</label>
                            <input type="number" step="0.1" value="175.5" class="w-full bg-slate-950/80 border border-cyan-500/30 rounded px-3 py-2 text-cyan-400 focus:outline-none focus:border-cyan-400 font-mono">
                        </div>
                        <div>
                            <label class="block text-xs uppercase text-slate-400 tracking-wider mb-2">Total Contract Volume Hours</label>
                            <input type="number" step="0.1" value="1000.0" class="w-full bg-slate-950/80 border border-cyan-500/30 rounded px-3 py-2 text-cyan-400 focus:outline-none focus:border-cyan-400 font-mono">
                        </div>
                    </form>
                </div>
                <button class="w-full mt-6 bg-gradient-to-r from-cyan-500 to-blue-600 hover:from-cyan-400 hover:to-blue-500 text-slate-950 font-bold uppercase tracking-widest py-3 rounded shadow-lg shadow-cyan-500/20 transition-all font-mono">EXECUTE_AUDIT_SEQUENCE</button>
            </section>

            <section class="lg:col-span-2 grid grid-cols-1 md:grid-cols-2 gap-6">
                <div class="cyber-panel rounded-xl p-5 flex flex-col justify-between">
                    <div>
                        <div class="flex justify-between items-start">
                            <h3 class="text-xs uppercase tracking-widest text-slate-400 font-bold">// United States // EEOC</h3>
                            <span class="px-2 py-0.5 text-[10px] font-mono font-bold bg-emerald-500/10 text-emerald-400 border border-emerald-500/30 rounded">COMPLIANT</span>
                        </div>
                        <div class="mt-4">
                            <span class="text-xs text-slate-500 block uppercase tracking-wider">Four-Fifths Impact Ratio</span>
                            <span class="text-3xl font-mono font-bold text-slate-100 tracking-tight mt-1 block">0.9235</span>
                        </div>
                    </div>
                    <p class="text-xs text-slate-400 border-t border-cyan-500/10 pt-3 mt-4">Selection metric checks float comfortably within compliant boundaries.</p>
                </div>

                <div class="cyber-panel rounded-xl p-5 flex flex-col justify-between border-red-500/20 shadow-red-500/5">
                    <div>
                        <div class="flex justify-between items-start">
                            <h3 class="text-xs uppercase tracking-widest text-slate-400 font-bold">// European Union // AI ACT</h3>
                            <span class="px-2 py-0.5 text-[10px] font-mono font-bold bg-rose-500/10 text-rose-400 border border-rose-500/30 rounded">CRITICAL_FAIL</span>
                        </div>
                        <div class="mt-4">
                            <span class="text-xs text-slate-500 block uppercase tracking-wider">Autonomous Profiling Incidents</span>
                            <span class="text-3xl font-mono font-bold text-rose-400 tracking-tight mt-1 block">03 <span class="text-xs text-slate-500">Violations</span></span>
                        </div>
                    </div>
                    <div class="mt-4 border-t border-cyan-500/10 pt-3">
                        <span class="text-[10px] text-rose-400/60 uppercase tracking-widest block">Simulated Civil Liability Penalty</span>
                        <span class="text-lg font-mono font-bold text-rose-400 mt-0.5 block">\$619,500.00 USD</span>
                    </div>
                </div>

                <div class="cyber-panel rounded-xl p-5 flex flex-col justify-between border-red-500/20 shadow-red-500/5">
                    <div>
                        <div class="flex justify-between items-start">
                            <h3 class="text-xs uppercase tracking-widest text-slate-400 font-bold">// Japan // METI</h3>
                            <span class="px-2 py-0.5 text-[10px] font-mono font-bold bg-rose-500/10 text-rose-400 border border-rose-500/30 rounded">NON_COMPLIANT</span>
                        </div>
                        <div class="mt-4">
                            <span class="text-xs text-slate-500 block uppercase tracking-wider">Temporal Sustainability Index</span>
                            <span class="text-3xl font-mono font-bold text-rose-400 tracking-tight mt-1 block">0.8245</span>
                        </div>
                    </div>
