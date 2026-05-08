import streamlit as st

# 1. Seiten-Konfiguration
st.set_page_config(page_title="moms of hamburg", page_icon="🧡", layout="centered")

# 2. Das CSS-Styling einschleusen
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    @import url('https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,700;1,9..144,400;1,9..144,700&family=Titan+One&display=swap');

    .stApp {
        background-color: #f46d24;
        color: #ffffff;
        font-family: 'Fraunces', serif;
        text-align: center;
    }

    .block-container {
        padding-top: 2rem !important;
        padding-bottom: 2rem !important;
        max-width: 800px;
    }

    .section {
        min-height: 80vh;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        padding: 60px 0;
        border-bottom: 2px dashed rgba(255, 255, 255, 0.3);
    }
    .section:last-child {
        border-bottom: none;
    }

    .hero-text {
        font-size: 4rem;
        line-height: 1.1;
        margin-bottom: 40px;
        font-weight: 700;
    }
    .hero-text span.italic {
        font-style: italic;
        font-weight: 400;
    }
    .section-title {
        font-size: 2.8rem;
        font-style: italic;
        margin-bottom: 40px;
        font-weight: 700;
        line-height: 1.2;
    }
    .section-title .regular {
        font-style: normal;
    }
    .text-p {
        font-size: 1.5rem;
        font-weight: 700;
        margin-bottom: 15px;
    }

    /* Logo-Bereich */
    .logo-container {
        margin-top: 50px;
        margin-bottom: 20px;
        text-align: center;
        display: inline-block;
    }
    .logo-text {
        font-family: 'Titan One', sans-serif;
        font-size: 3.2rem;
        letter-spacing: -1px;
        line-height: 0.85;
        text-align: left;
    }
    .logo-subtext {
        font-size: 0.85rem;
        font-family: sans-serif;
        text-transform: uppercase;
        font-weight: 900;
        letter-spacing: 1.5px;
        margin-left: 140px; /* Versatz nach rechts */
        margin-top: 10px;   /* HIER: Weiter nach UNTEN gerückt */
        text-align: left;
        line-height: 1.2;
    }
    
    div.stButton > button {
        background-color: #ffffff;
        color: #f46d24;
        font-family: sans-serif;
        font-weight: bold;
        font-size: 1.2rem;
        border-radius: 50px;
        border: none;
        padding: 10px 30px;
        margin-top: 20px;
    }
    div.stButton > button:hover {
        background-color: #ffeee5;
        color: #f46d24;
    }

    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        justify-content: center;
    }
    .stTabs [data-baseweb="tab"] {
        background-color: rgba(255, 255, 255, 0.2);
        border-radius: 10px 10px 0 0;
        color: white;
        padding: 10px 20px;
    }
    .stTabs [aria-selected="true"] {
        background-color: white !important;
        color: #f46d24 !important;
    }
    .dummy-box {
        background-color: rgba(255,255,255,0.1);
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 15px;
        text-align: left;
    }
    .dummy-box h4 { margin-top: 0; margin-bottom: 5px; font-family: sans-serif;}
    .dummy-box p { font-size: 1rem; font-weight: normal; font-family: sans-serif; margin: 0;}
    </style>
""", unsafe_allow_html=True)

# 3. Haupt-Inhalt (Slides)
st.markdown("""
    <div class="section">
        <div class="hero-text">
            <span class="italic">kein bock</span><br>
            wieder <span class="italic">alleine</span><br>
            auf den<br>
            spieli?
        </div>
        <div class="logo-container">
            <div class="logo-text">moms of<br>hamburg</div>
            <div class="logo-subtext">built<br>your own<br>village ♥</div>
        </div>
    </div>

    <div class="section">
        <div class="section-title">was ist <span class="regular">moms of</span><br><span class="regular">hamburg?</span></div>
        <div class="text-p">eine community für mütter aus hamburg</div>
        <div class="text-p">für connection statt vergleichen</div>
        <div class="text-p">für echte menschen statt perfekte feeds</div>
        <div class="text-p">für alle, die sich manchmal zwischen<br>spielplatz, arbeit und alltag allein fühlen</div>
    </div>
""", unsafe_allow_html=True)

# 4. Community Dummy Bereich
st.markdown("<div class='section-title' style='margin-top: 60px;'>bald verfügbar:<br><span class='regular'>dein digitales village</span></div>", unsafe_allow_html=True)

tab1, tab2, tab3, tab4 = st.tabs(["📌 Pinnwand", "🧸 Tauschbörse", "📍 Dein Kiez", "💬 Real Talk"])

with tab1:
    st.markdown("### Spontane Treffen & Playdates")
    st.text_input("Schreib einen Aufruf:", placeholder="Z.B.: Bin ab 15 Uhr am Baakenhöft Spielplatz, jemand Lust?")
    st.button("Posten (Dummy)")
    st.markdown("""
        <div class="dummy-box">
            <h4>Lisa (Mama von Leo, 2)</h4>
            <p>Hilfe, mir fällt die Decke auf den Kopf. Geht jemand spontan in Planten un Blomen spazieren?</p>
        </div>
    """, unsafe_allow_html=True)

with tab2:
    st.markdown("### Geben, Nehmen, Leihen")
    st.selectbox("Kategorie wählen:", ["Kleidung", "Spielzeug", "Ausstattung"])
    st.markdown("""
        <div class="dummy-box">
            <h4>BIETE: Matschhose Gr. 92</h4>
            <p>Gut erhalten, in Altona abzuholen. Tausche gegen einen Hafer-Cappuccino.</p>
        </div>
    """, unsafe_allow_html=True)

with tab3:
    st.markdown("### Lokales Village")
    st.selectbox("Wähle deinen Bezirk:", ["Altona", "Eimsbüttel", "Winterhude", "Eppendorf", "Barmbek", "Bergedorf", "Harburg"])
    st.info("Lokale Gruppen entstehen demnächst.")

with tab4:
    st.markdown("### Real Talk (Anonym)")
    st.text_area("Was liegt dir auf dem Herzen?", placeholder="Kein Judgement, nur rauslassen...")
    st.button("Anonym senden")
    st.markdown("""
        <div class="dummy-box">
            <h4>Anonym</h4>
            <p>Ich liebe mein Kind, aber heute ist einfach ein Tag, an dem ich am liebsten kündigen würde. Muttersein ist anstrengend.</p>
            <p style="color: #f46d24; font-size: 0.8em; margin-top: 10px;">❤️ 12 Mamas fühlen das auch</p>
        </div>
    """, unsafe_allow_html=True)

# 5. Outro / Instagram
st.markdown("<div style='margin-top: 80px;'></div>", unsafe_allow_html=True)
cols = st.columns([1, 2, 1])
with cols[1]:
    # HIER DEINEN ECHTEN LINK EINTRAGEN
    st.link_button("Folge uns auf Instagram", "https://instagram.com/moms.of.hamburg", use_container_width=True)

st.markdown("""
    <div class="logo-container" style="margin-top: 80px; margin-bottom: 80px;">
        <div class="logo-text">moms of<br>hamburg</div>
        <div class="logo-subtext">built<br>your own<br>village ♥</div>
    </div>
""", unsafe_allow_html=True)
