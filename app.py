import google.generativeai as genai
import streamlit as st

# --- 1. CONFIGURATION ---
try:
    API_KEY = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=API_KEY)
except Exception:
    st.error("Missing API Key in Secrets!")

# --- 2. DECORATIVE UI (CUSTOM CSS) ---
st.set_page_config(page_title="ELI: Decipherer", page_icon="👶", layout="centered")

st.markdown("""
    <style>
    /* Main background and font */
    .main {
        background-color: #0e1117;
    }
    /* Stylizing the Title */
    .title-text {
        font-size: 50px !important;
        font-weight: 800;
        color: #FF4B4B;
        text-align: center;
        margin-bottom: 0px;
    }
    /* Subtitle styling */
    .subtitle-text {
        font-size: 20px;
        color: #FAFAFA;
        text-align: center;
        font-style: italic;
        margin-bottom: 30px;
    }
    /* Button styling */
    div.stButton > button:first-child {
        background-color: #FF4B4B;
        color: white;
        font-size: 20px;
        font-weight: bold;
        width: 100%;
        border-radius: 10px;
        border: none;
        height: 3em;
        transition: 0.3s;
    }
    div.stButton > button:first-child:hover {
        background-color: #ff3333;
        box-shadow: 0px 4px 15px rgba(255, 75, 75, 0.4);
        transform: scale(1.02);
    }
    /* Result Box */
    .stSuccess {
        background-color: rgba(46, 204, 113, 0.1) !important;
        border: 1px solid #2ecc71 !important;
        color: #2ecc71 !important;
        border-radius: 15px;
        padding: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. THE APP CONTENT ---
st.markdown('<p class="title-text">👶 ELI: Complexity Decipherer</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle-text">Turning jargon into simple stories for any audience.</p>', unsafe_allow_html=True)

# Layout using columns for the slider
st.write("---")
col1, col2 = st.columns([1, 2])

with col1:
    level = st.select_slider(
        "**Target Audience:**",
        options=["Child", "Student", "Expert"],
        value="Child"
    )

with col2:
    user_topic = st.text_input("**Enter a complex topic:**", placeholder="e.g. Backpropagation, Black Holes...")

st.write("") # Padding

if st.button("🚀 DECIPHER TOPIC"):
    if user_topic:
        with st.spinner(f"AI is thinking like a {level}..."):
            try:
                prompts = {
                    "Child": f"Explain {user_topic} to a 5-year-old using a simple analogy. No big words.",
                    "Student": f"Explain {user_topic} to a college student. Use technical terms but explain them clearly with examples.",
                    "Expert": f"Provide a high-level, technical summary of {user_topic} for a researcher. Focus on mechanics and efficiency."
                }

                # Bulletproof model scanner
                available_models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
                selected_model = next((m for m in available_models if '1.5-flash' in m), available_models[0])
                
                model = genai.GenerativeModel(selected_model)
                response = model.generate_content(prompts[level])
                
                st.markdown(f"### 💡 {level} Level Explanation")
                st.success(response.text)
                
            except Exception as e:
                st.error(f"Something went wrong: {e}")
    else:
        st.warning("Please enter a topic first!")

# --- 4. TEAM FOOTER (Decorative) ---
st.write("")
st.write("")
st.divider()
st.markdown("""
    <div style="text-align: center; color: #888;">
        <p><b>
