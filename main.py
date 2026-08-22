import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(page_title="Lumina BI | Home", layout="wide")

# --- PURE BLACK POSTER / BRUTALIST CSS ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700;900&display=swap');
    
    /* 1. Force absolute pure black background across the whole app */
    [data-testid="stAppViewContainer"], [data-testid="stHeader"] {
        background-color: #000000 !important;
        color: #FFFFFF !important;
    }

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif !important;
        color: #FFFFFF !important;
    }
    
    /* 2. The Massive Typography from your reference image */
    .mega-title {
        font-weight: 900;
        font-size: 8.5rem; /* Massive scale */
        letter-spacing: -0.06em; /* Extremely tight kerning */
        line-height: 0.85; /* Extremely tight line height */
        text-transform: uppercase;
        margin-bottom: 3rem;
        color: #FFFFFF;
    }
    
    .sub-heading {
        font-weight: 700;
        font-size: 3rem;
        letter-spacing: -0.04em;
        line-height: 1;
        text-transform: uppercase;
        margin-top: 2rem;
        margin-bottom: 1.5rem;
    }

    /* 3. Minimalist structural cards based on your image */
    .swiss-card {
        border-top: 2px solid #FFFFFF; /* High contrast top border */
        padding-top: 1rem;
        margin-bottom: 2rem;
    }
    
    .swiss-card h4 {
        font-weight: 700;
        font-size: 1.5rem;
        letter-spacing: -0.03em;
        text-transform: uppercase;
        margin-bottom: 0.5rem;
        color: #FFFFFF;
    }
    
    .swiss-card p {
        color: #A0A0A0; /* Light gray for contrast hierarchy */
        font-weight: 400;
        font-size: 0.95rem;
        line-height: 1.4;
    }
    
    /* Hide the default Streamlit top padding to make it look like a poster */
    .block-container {
        padding-top: 2rem !important;
    }
</style>
""", unsafe_allow_html=True)

# --- HERO SECTION ---
# Using the exact phrasing style from your reference image
st.markdown('<div class="mega-title">LUMINA<br>BI.</div>', unsafe_allow_html=True)

# --- ARCHITECTURE GRID ---
st.markdown('<div class="sub-heading">CARRY INNOVATION<br>WITH YOU</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="swiss-card">
        <h4>01 / Healing</h4>
        <p>LLM-driven contextual imputation and sequence pattern recognition. Zero manual cleanup required.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="swiss-card">
        <h4>02 / Workspace</h4>
        <p>Interactive multi-sheet data editor with real-time natural language query execution.</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="swiss-card">
        <h4>03 / Export</h4>
        <p>Binary SQLite database push and comprehensive audit trails for absolute data governance.</p>
    </div>
    """, unsafe_allow_html=True)

# --- SYSTEM STATUS ---
st.markdown('<div class="swiss-card" style="margin-top: 4rem;"><h4>SYSTEM STATUS</h4></div>', unsafe_allow_html=True)

if "cleaned_df" in st.session_state:
    df = st.session_state["cleaned_df"]
    
    st.success("🟢 Active in Memory")
    st.dataframe(df.head(4), use_container_width=True)
else:
    st.info("⚪ System Idle. Navigate to the sidebar to initialize the pipeline.")