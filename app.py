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

    .logo-container {
        margin-top: 50px;
        margin-bottom: 20px;
    }
    .logo-text {
        font-family: 'Titan One', sans-serif;
        font-size: 3rem;
        letter-spacing: -1px;
        line-height: 0.9;
    }
    .logo-subtext {
        font-size: 0.8rem;
        font-family: sans-serif;
        text-transform: uppercase;
        font-weight: bold;
        letter-spacing: 1px;
        margin-left: 120px;
        margin-top: -15px;
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
    }
    div.stButton > button:hover {
        background-color: #ffeee5;
        color: #f46d24;
    }

    /* Styling für die Tabs und interaktiven Elemente */
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

# 3. Den bestehenden Inhalt rendern
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

# 4. Dummy Community Bereich
st.markdown("<div class='section-title' style='margin-top: 60px;'>bald verfügbar:<br><span class='regular'>dein digitales village</span></div>", unsafe_allow_html=True)

tab1, tab2, tab3, tab4 = st.tabs(["📌 Pinnwand", "🧸 Tauschbörse", "📍 Dein Kiez", "💬 Real Talk"])

with tab1:
    st.markdown("### Spontane Treffen & Playdates")
    st.markdown("Finde Mütter, die genau *jetzt* Zeit haben.")
    st.text_input("Schreib einen Aufruf:", placeholder="Z.B.: Bin ab 15 Uhr am Baakenhöft Spielplatz, jemand Lust?")
    st.button("Posten (Dummy)")
    
    st.markdown("""
        <div class="dummy-box">
            <h4>Lisa (Mama von Leo, 2)</h4>
            <p>Hilfe, mir fällt die Decke auf den Kopf. Geht jemand spontan in Planten un Blomen spazieren?</p>
        </div>
        <div class="dummy-box">
            <h4>Sarah (Schwanger)</h4>
            <p>Suche andere werdende Mamas aus Eimsbüttel für einen Kaffee am Wochenende!</p>
        </div>
    """, unsafe_allow_html=True)

with tab2:
    st.markdown("### Geben, Nehmen, Leihen")
    st.markdown("Kinder wachsen schnell. Ressourcen teilen auch.")
    st.selectbox("Kategorie wählen:", ["Kleidung (Baby)", "Kleidung (Kleinkind)", "Spielzeug", "Umstandsmode", "Ausstattung (Kinderwagen etc.)"])
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
            <div class="dummy-box">
                <h4>BIETE: Matschhose Gr. 92</h4>
                <p>Gut erhalten, in Altona abzuholen. Tausche gegen einen Hafer-Cappuccino.</p>
            </div>
        """, unsafe_allow_html=True)
    with col2:
         st.markdown("""
            <div class="dummy-box">
                <h4>SUCHE: Federwiege</h4>
                <p>Verzweifelte Grüße aus Winterhude. Hat jemand eine Federwiege für 2 Monate zu verleihen?</p>
            </div>
        """, unsafe_allow_html=True)

with tab3:
    st.markdown("### Finde dein lokales Village")
    st.markdown("Tausche dich mit Müttern direkt in deiner Nachbarschaft aus.")
    st.selectbox("Wähle deinen Bezirk:", ["Hamburg-Nord", "Altona", "Eimsbüttel", "Hamburg-Mitte", "Wandsbek", "Harburg", "Bergedorf"])
    st.info("Tritt der lokalen WhatsApp- oder Telegram-Gruppe bei, um dich lokal zu vernetzen. (Demnächst)")

with tab4:
    st.markdown("### Venting Space")
    st.markdown("Keine Ratschläge. Kein Judgement. Einfach mal rauslassen, was nervt.")
    st.text_area("Was liegt dir auf dem Herzen? (wird anonym gepostet)", placeholder="Mein Kind hat heute Nacht gefühlt null geschlafen und ich muss gleich arbeiten...")
    st.button("Anonym loswerden (Dummy)")
    st.markdown("""
        <div class="dummy-box">
            <h4>Anonym</h4>
            <p>Ich liebe mein Kind, aber heute ist einfach ein Tag, an dem ich am liebsten kündigen würde. Muttersein ist manchmal so unfassbar anstrengend.</p>
            <p style="color: #f46d24; font-size: 0.9em; margin-top: 5px;">❤️ 12 Mamas fühlen das auch</p>
        </div>
    """, unsafe_allow_html=True)

# 5. Outro / Instagram Link
st.markdown("<div style='margin-top: 80px;'></div>", unsafe_allow_html=True)
cols = st.columns([1, 2, 1])
with cols[1]:
    st.link_button("Folge uns auf Instagram", "https://instagram.com/deine-seite", use_container_width=True)

st.markdown("""
    <div class="logo-container" style="margin-top: 60px; margin-bottom: 60px;">
        <div class="logo-text">moms of<br>hamburg</div>
        <div class="logo-subtext">built<br>your own<br>village ♥</div>
    </div>
""", unsafe_allow_html=True)
