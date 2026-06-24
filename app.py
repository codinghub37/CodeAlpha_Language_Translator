
import streamlit as st
from deep_translator import GoogleTranslator
from gtts import gTTS
import pyperclip
import io

# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="Language Translation Tool",
    page_icon="🌍",
    layout="wide"
)

# ---------------- CSS ---------------- #

st.markdown("""
<style>

.stApp{
    background: linear-gradient(135deg,#0f172a,#1e293b);
}

.main-header{
    text-align:center;
    padding:25px;
    border-radius:20px;
    background:linear-gradient(90deg,#667eea,#764ba2);
    color:white;
    margin-bottom:20px;
    box-shadow:0px 4px 15px rgba(0,0,0,0.3);
}

h1,h2,h3,h4,h5,h6,
p,span,label{
    color:white !important;
}

[data-testid="stMarkdownContainer"]{
    color:white !important;
}

.stTextArea textarea{
    border-radius:15px;
    border:2px solid #667eea;
    background:white;
    color:black !important;
    font-size:16px;
}

div.stButton > button{
    width:100%;
    height:55px;
    border-radius:12px;
    border:none;
    color:white !important;
    font-weight:bold;
    background:linear-gradient(90deg,#22c55e,#16a34a);
}

[data-testid="stSidebar"]{
    background:linear-gradient(180deg,#111827,#1f2937);
}

[data-testid="stSidebar"] *{
    color:white !important;
}

.result-box{
    background:white;
    color:black !important;
    padding:20px;
    border-radius:15px;
    font-size:18px;
    font-weight:500;
}

.footer{
    text-align:center;
    margin-top:20px;
}

.footer h4{
    color:white !important;
}

.footer p{
    color:#d1d5db !important;
}

</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ---------------- #

st.markdown("""
<div class="main-header">
<h1>🌍 AI Language Translation Tool</h1>
<p>Translate Text into 49+ Languages Instantly</p>
</div>
""", unsafe_allow_html=True)

# ---------------- LANGUAGES ---------------- #

languages = {
    "English":"en",
    "Urdu":"ur",
    "Hindi":"hi",
    "Arabic":"ar",
    "Spanish":"es",
    "French":"fr",
    "German":"de",
    "Italian":"it",
    "Portuguese":"pt",
    "Russian":"ru",
    "Chinese":"zh-CN",
    "Japanese":"ja",
    "Korean":"ko",
    "Turkish":"tr",
    "Dutch":"nl",
    "Greek":"el",
    "Hebrew":"iw",
    "Swedish":"sv",
    "Polish":"pl",
    "Bengali":"bn",
    "Persian":"fa",
    "Indonesian":"id",
    "Malay":"ms",
    "Thai":"th",
    "Vietnamese":"vi",
    "Nepali":"ne",
    "Tamil":"ta",
    "Gujarati":"gu",
    "Marathi":"mr",
    "Punjabi":"pa",
    "Telugu":"te",
    "Kannada":"kn",
    "Malayalam":"ml",
    "Sinhala":"si",
    "Czech":"cs",
    "Danish":"da",
    "Finnish":"fi",
    "Hungarian":"hu",
    "Norwegian":"no",
    "Romanian":"ro",
    "Slovak":"sk",
    "Ukrainian":"uk",
    "Filipino":"tl",
    "Croatian":"hr",
    "Serbian":"sr",
    "Bulgarian":"bg",
    "Estonian":"et",
    "Latvian":"lv",
    "Lithuanian":"lt"
}

# ---------------- SESSION ---------------- #

if "translated_text" not in st.session_state:
    st.session_state.translated_text = ""

# ---------------- SIDEBAR ---------------- #

st.sidebar.title("🌐 Translator Pro")

st.sidebar.success(
    f"🌍 Supported Languages: {len(languages)}+"
)

st.sidebar.markdown("""
### 🚀 Features

✅ Google Translate API

✅ 49+ Languages

✅ Copy Translation

✅ Text To Speech

✅ Modern UI
""")

# ---------------- INPUTS ---------------- #

col1, col2 = st.columns(2)

with col1:
    source_lang = st.selectbox(
        "Source Language",
        list(languages.keys())
    )

with col2:
    target_lang = st.selectbox(
        "Target Language",
        list(languages.keys()),
        index=1
    )

text = st.text_area(
    "Enter Text",
    height=200,
    placeholder="Type text here..."
)

# ---------------- BUTTONS ---------------- #

b1, b2, b3 = st.columns(3)

with b1:
    translate_btn = st.button("🔄 Translate", use_container_width=True)

with b2:
    copy_btn = st.button("📋 Copy", use_container_width=True)

with b3:
    voice_btn = st.button("🔊 Voice", use_container_width=True)

# ---------------- TRANSLATE ---------------- #

# Translation
if translate_btn:

    st.write("Source:", source_lang)
    st.write("Target:", target_lang)

    if text.strip() == "":
        st.warning("Please enter text")
    else:
        try:

            translated = GoogleTranslator(
                source=languages[source_lang],
                target=languages[target_lang]
            ).translate(text)

            st.write("Result:", translated)

            st.session_state.translated_text = translated

        except Exception as e:
            st.error(f"Error: {e}")
# ---------------- RESULT ---------------- #

if st.session_state.translated_text:

    st.markdown(
        "<h2 style='color:white;'>📄 Translated Text</h2>",
        unsafe_allow_html=True
    )

    st.markdown(
        f"""
        <div class="result-box">
        {st.session_state.translated_text}
        </div>
        """,
        unsafe_allow_html=True
    )

# ---------------- COPY ---------------- #

if copy_btn and st.session_state.translated_text:
    try:
        pyperclip.copy(st.session_state.translated_text)
        st.success("📋 Copied Successfully!")
    except:
        st.warning("Copy not supported.")

# ---------------- VOICE ---------------- #

# ---------------- VOICE ---------------- #

if voice_btn:

    if not st.session_state.translated_text:
        st.warning("Please translate text first.")

    else:
        try:

            voice_lang = languages[target_lang]

            tts = gTTS(
                text=st.session_state.translated_text,
                lang=voice_lang
            )

            audio_buffer = io.BytesIO()
            tts.write_to_fp(audio_buffer)
            audio_buffer.seek(0)

            import base64

            audio_base64 = base64.b64encode(
                audio_buffer.getvalue()
            ).decode()

            st.markdown(
                f"""
                <audio autoplay>
                    <source src="data:audio/mp3;base64,{audio_base64}" type="audio/mp3">
                </audio>
                """,
                unsafe_allow_html=True
            )

        except Exception as e:
            st.error(f"Voice Error: {e}")

# ---------------- FOOTER ---------------- #

st.markdown("""
<div class="footer">
<hr>
<h4>🌍 Language Translation Tool</h4>
<p>Powered by Google Translate API | Built with Streamlit</p>
</div>
""", unsafe_allow_html=True)

