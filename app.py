import google.generativeai as genai
import streamlit as st

# --- 1. CONFIGURATION ---
# This looks for the name "GOOGLE_API_KEY" in your Streamlit Secrets
try:
    API_KEY = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=API_KEY)
except Exception as e:
    st.error("Secrets not found! Make sure GOOGLE_API_KEY is in Streamlit Settings.")

# --- 2. UI SETUP ---
st.set_page_config(page_title="ELI5 Decipherer", page_icon="👶")
st.title("👶 ELI5: Complexity Decipherer")
st.divider()

user_topic = st.text_input("Enter a complex topic:", placeholder="e.g. Black Holes...")

if st.button("Explain Like I'm 5", type="primary"):
    if user_topic:
        with st.spinner("Finding a model and deciphering..."):
            try:
                # We use the universal name that worked earlier
                model = genai.GenerativeModel('gemini-1.5-flash')
                response = model.generate_content(f"Explain {user_topic} to a 5-year-old using a simple analogy.")
                st.subheader("The Simple Version:")
                st.success(response.text)
            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("Please enter a topic first!")

# --- 3. TEAM FOOTER ---
st.divider()
st.markdown("""
**Developed by:** Arjun Sharma & Team  
**Program:** AIDS (SYCSE B) | Pune 🚀
""")
