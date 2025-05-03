
import streamlit as st

st.set_page_config(page_title="TrustVault - Immutable Audit Layer for AI", page_icon="🔒", layout="wide")

st.markdown("""
<style>
.hero {text-align: center;padding: 80px 20px 40px 20px;}
.hero h1 {font-size: 60px;color: #2563eb;margin-bottom: 20px;}
.hero p {font-size: 24px;color: #555;margin-bottom: 40px;}
.cta-button {background-color: #2563eb;color: white;padding: 16px 40px;border-radius: 10px;font-size: 20px;text-decoration: none;display: inline-block;margin: 10px;}
.cta-button:hover {background-color: #1d4ed8;}
.feature-section {text-align: center;padding: 60px 20px;background-color: #ffffff;border-radius: 12px;margin: 20px;box-shadow: 0 4px 10px rgba(0,0,0,0.05);}
.feature-section h2 {font-size: 36px;color: #2563eb;margin-bottom: 20px;}
.feature-section p {font-size: 18px;color: #555;}
.footer {text-align: center;padding: 40px;color: gray;}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
    <h1>TrustVault</h1>
    <p>The Immutable Audit Layer for AI & LLMs. Capture. Certify. Verify. Comply.</p>
</div>
""", unsafe_allow_html=True)

st.page_link("pages/Investor_Pitch_Agent.py", label="💼 Launch Investor Agent", icon="💼")
st.markdown("[📩 Contact Founders](mailto:founder@trustvault.ai)", unsafe_allow_html=True)

st.markdown("""
<div class="feature-section">
    <h2>Why TrustVault?</h2>
    <p>EU AI Act. SOC 2. HIPAA. Regulations demand AI verifiability and traceability.<br>
    TrustVault makes every interaction audit-proof — immutable storage, certification, evaluator marketplace and compliance automation.</p>
</div>
<div class="feature-section">
    <h2>For Investors and Partners</h2>
    <p>Learn about market, roadmap, competition and why we are building the next critical infrastructure for enterprise AI trust.</p>
</div>
<div class="footer">© 2025 TrustVault.ai — All rights reserved.</div>
""", unsafe_allow_html=True)
