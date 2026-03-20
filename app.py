import google.generativeai as genai
import streamlit as st

# --- 1. CONFIGURATION ---
try:
    # Use the Secret name you set in Streamlit Settings
    API_KEY = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=API_KEY)
except Exception as e:
    st.error("Missing API Key! Add GOOGLE_API_KEY to your Streamlit Secrets.")

# --- 2. UI SETUP ---
st.set_page_config(page_title="ELI5 Decipherer", page_icon="👶")
st.title("👶 ELI5: Complexity Decipherer")
st.markdown("### *Turning jargon into simple stories*")
st.divider()

user_topic = st.text_input("Enter a complex topic:", placeholder="e.g. Black Holes, Neural Networks...")

if st.button("Explain Like I'm 5", type="primary"):
    if user_topic:
        with st.spinner("Finding best AI model..."):
            try:
                # DYNAMIC MODEL SELECTION: This prevents the 404 error
                # It asks Google: "What models do you have for me?"
                available_models = [m.name for m in genai.list_models() 
                                   if 'generateContent' in m.supported_generation_methods]
                
                # Pick the newest one available (2.5 or 1.5)
                # If neither found, it picks the first one in the list
                selected_model = next((m for m in available_models if '2.5' in m), 
                                     next((m for m in available_models if '1.5-flash' in m), 
                                          available_models[0]))

                model = genai.GenerativeModel(selected_model)
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
