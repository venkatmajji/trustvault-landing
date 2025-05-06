
import streamlit as st

st.set_page_config(page_title="TrustVault | Immutable Audit Layer for AI", page_icon="🔒", layout="wide")

# ---- Branding and Styling ----
st.markdown("""
<style>
body {
    background-color: #f8f9fb;
}
.hero-title { font-size: 48px; color: #1d4ed8; text-align: center; font-weight: bold; margin-top: 30px; animation: fadeIn 2s ease-in;}
.hero-subtitle { font-size: 22px; color: #444; text-align: center; margin-bottom: 40px; animation: fadeIn 2s ease-in;}
.section-title { font-size: 28px; color: #1d4ed8; margin-top: 50px; margin-bottom: 20px; }
.feature-box { background-color: #ffffff; padding: 20px; border-radius: 12px; margin-bottom: 20px; box-shadow: 0 2px 12px rgba(0,0,0,0.05);}
.feature-box:hover { background-color: #eef2ff; }
.footer {text-align: center; padding: 30px; color: gray; margin-top: 50px;}
.logo {text-align:center; margin-top:20px; margin-bottom:20px;}
.cta-button {font-size: 20px; padding: 14px; background-color: #2563eb; color: white; border-radius: 8px; text-align: center; display: block; margin: 10px auto; text-decoration: none;}
.cta-button:hover {background-color: #1d4ed8;}
@keyframes fadeIn {
  0% {opacity:0;}
  100% {opacity:1;}
}
</style>
""", unsafe_allow_html=True)

# ---- Logo ----
st.markdown("""<div class="logo"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/7/73/Flat_tick_icon.svg/2048px-Flat_tick_icon.svg.png" width="100"></div>""", unsafe_allow_html=True)

# ---- Hero Section ----
st.markdown("""
<div class="hero-title">TrustVault</div>
<div class="hero-subtitle">🔒 Capture. Certify. Verify. Comply.<br>Immutable Audit Layer for AI & LLMs</div>
""", unsafe_allow_html=True)

st.markdown("<a href='/Investor_Pitch_Agent' class='cta-button'>💼 Launch Investor Agent</a>", unsafe_allow_html=True)
st.markdown("<a href='mailto:founder@trustvault.ai' class='cta-button'>📩 Contact Founders</a>", unsafe_allow_html=True)

# ---- Features ----
st.markdown("<div class='section-title'>✨ Key Features</div>", unsafe_allow_html=True)

features = [
    ("🛡️ Immutable Storage + Merkle Hashing", "Ensure tamper-proof records of all AI interactions with WORM storage."),
    ("📜 Daily PDF Certification", "Generate daily sealed audit reports for traceability."),
    ("🏪 Evaluator Marketplace", "Access 3rd party evaluators to verify model outputs."),
    ("⚙️ Compliance Automation", "Automate processes for EU AI Act, SOC 2, HIPAA and more."),
]

for title, desc in features:
    st.markdown(f"""
    <div class='feature-box'>
    <b>{title}</b><br>
    {desc}
    </div>
    """, unsafe_allow_html=True)

# ---- Market Opportunity ----
st.markdown("<div class='section-title'>📈 Market Opportunity</div>", unsafe_allow_html=True)
st.markdown("""
- **TAM:** $15B+
- **SAM:** $2.5B
- **SOM:** $100M wedge from regulated AI teams
""")

# ---- Business Model ----
st.markdown("<div class='section-title'>💰 Business Model</div>", unsafe_allow_html=True)
st.markdown("""
- **Free Tier:** Basic usage
- **Pro Tier:** $199/month
- **Compliance Tier:** $999/month
- **Enterprise:** $50K+/year custom plans
""")

# ---- Roadmap ----
st.markdown("<div class='section-title'>🗺️ Roadmap</div>", unsafe_allow_html=True)
st.markdown("""
1️⃣ Immutable Vault (launched)  
2️⃣ Real-time Evaluator Proxy (in development)  
3️⃣ Evaluator Marketplace (next)  
4️⃣ Compliance Automation (future)
""")

# ---- Footer ----
st.markdown("""
<div class='footer'>© 2025 TrustVault.ai — All rights reserved.</div>
""", unsafe_allow_html=True)
