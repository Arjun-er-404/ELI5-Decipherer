import google.generativeai as genai
import streamlit as st
import os

# --- 1. CONFIGURATION ---
# We ask for the NAME we gave the secret in the settings
API_KEY = st.secrets["AIzaSyB3lC2JKr-Ow3wCBKdliIpgaXsX-wi5Mac"]
genai.configure(api_key=API_KEY)

# --- 2. UI SETUP ---
st.set_page_config(page_title="ELI5 Decipherer", page_icon="👶")
st.title("👶 ELI5: Complexity Decipherer")

user_topic = st.text_input("Enter a complex topic:", placeholder="e.g. Black Holes...")

if st.button("Explain Like I'm 5", type="primary"):
    if user_topic:
        with st.spinner("Scanning for available models..."):
            try:
                # STEP 1: Find what models YOUR key actually has access to
                available_models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
                
                # STEP 2: Pick the best one (Flash if available, else Pro)
                selected_model = None
                for m in available_models:
                    if 'gemini-1.5-flash' in m:
                        selected_model = m
                        break
                
                if not selected_model:
                    selected_model = available_models[0] # Just grab the first working one

                # STEP 3: Run the explanation
                model = genai.GenerativeModel(selected_model)
                response = model.generate_content(f"Explain {user_topic} to a 5-year-old using a simple analogy.")
                
                st.subheader("The Simple Version:")
                st.success(response.text)
                
            except Exception as e:
                st.error(f"Total Failure: {e}")
                st.write("Available models found for your key:", available_models)
    else:
        st.warning("Please enter a topic first!")
        # --- 5. DEVELOPER FOOTER ---
st.divider()
col1, col2 = st.columns([3, 1])

with col1:
    st.markdown("""
    **Developed by:** Arjun Sharma and his team (Bhushan Thite, Eisa Khan & Shreyash Suryawanshi)\n 
    **Program:** AIDS (Second Year Computer Science & Engineering)  
    **Specialization:** AI & Data Science (AIDS)  
    *Built for the 2026 Vishwanova Hackathon*
    """)

with col2:
    # A little boxing glove icon because we know you're a fan!
    st.markdown("### 🥊 💻")

st.caption("© 2026 | Complexity Decipherer v1.0")
