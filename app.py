import google.generativeai as genai
import streamlit as st

# --- 1. CONFIGURATION ---
try:
    API_KEY = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=API_KEY)
except Exception:
    st.error("Missing API Key in Secrets!")

# --- 2. DECORATIVE UI (CUSTOM CSS) ---
st.set_page_config(page_title="ELI5: Decipherer", page_icon="🥶", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .title-text {
        font-size: 45px !important;
        font-weight: 800;
        color: #FF4B4B;
        text-align: center;
        margin-top: -50px;
    }
    div.stButton > button:first-child {
        background-color: #FF4B4B;
        color: white;
        font-size: 18px;
        font-weight: bold;
        width: 100%;
        border-radius: 10px;
        height: 3em;
        transition: 0.3s;
    }
    div.stButton > button:first-child:hover {
        background-color: #ff3333;
        box-shadow: 0px 4px 15px rgba(255, 75, 75, 0.4);
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDEBAR (Scientists & Tech) ---
with st.sidebar:
    st.title("💡 Inspiration")
    # Image of famous scientists
    st.image("http://googleusercontent.com/image_collection/image_retrieval/13807817225450875576_0", caption="Great minds who simplified the universe.")
    st.divider()
    st.info("“If you can't explain it simply, you don't understand it well enough.” – Albert Einstein")
    st.divider()
    # Tech motif
    st.image("http://googleusercontent.com/image_collection/image_retrieval/2035985715402190220_0")

# --- 4. MAIN INTERFACE ---
# Top Header Image
st.image("http://googleusercontent.com/image_collection/image_retrieval/2035985715402190220_1", use_container_width=True)

st.markdown('<p class="title-text">👶 ELI: Complexity Decipherer</p>', unsafe_allow_html=True)

st.write("---")
col1, col2 = st.columns([1, 2])

with col1:
    level = st.select_slider(
        "**Target Audience:**",
        options=["Child", "Student", "Expert"],
        value="Child"
    )

with col2:
    user_topic = st.text_input("**Enter a complex topic:**", placeholder="e.g. Quantum Entanglement, Web3...")

if st.button("🚀 DECIPHER TOPIC"):
    if user_topic:
        with st.spinner(f"AI is deciphering for a {level}..."):
            try:
                prompts = {
                    "Child": f"Explain {user_topic} to a 5-year-old using a simple analogy. No big words.",
                    "Student": f"Explain {user_topic} to a college student. Use technical terms but explain them clearly with examples.",
                    "Expert": f"Provide a high-level, technical summary of {user_topic} for a researcher. Focus on mechanics and efficiency."
                }

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

# --- 5. FOOTER ---
st.divider()
st.markdown("""
    <div style="text-align: center; color: #888;">
        <p><b>Developed by:</b> Arjun & Team | Vishwanova Hackathon | SYCSE B 🚀</p>
    </div>
    """, unsafe_allow_html=True)
