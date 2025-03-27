import streamlit as st
import google.generativeai as genai

API_KEY = st.secrets["GEMINI_API_KEY"]
genai.configure(api_key=API_KEY)

# Inisialisasi model Gemini
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="tunedModels/tumbuhsehatfinetunellm-cwr8817ckikt",
  generation_config=generation_config,
)

def get_gemini_response(user_input):
    response = model.generate_content(user_input)
    return response.text if response else "Maaf, terjadi kesalahan."

# Streamlit UI
st.title("TumbuhSehat Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = []
    # Kirim pesan "Halo" secara otomatis saat pertama kali dibuka
    first_message = "Halo"
    first_response = get_gemini_response(first_message)
    st.session_state.messages.append({"role": "user", "content": first_message})
    st.session_state.messages.append({"role": "bot", "content": first_response})

for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.chat_message("user").markdown(msg["content"])
    else:
        st.chat_message("assistant").markdown(msg["content"])

user_input = st.chat_input("Ketik pesan...")
if user_input:
    st.chat_message("user").markdown(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    response = get_gemini_response(user_input)
    st.chat_message("assistant").markdown(response)
    st.session_state.messages.append({"role": "bot", "content": response})
