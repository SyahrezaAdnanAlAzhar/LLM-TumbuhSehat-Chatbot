import streamlit as st
import google.generativeai as genai

# Konfigurasi API Key (Ganti dengan API key-mu)
API_KEY = st.secrets["GEMINI_API_KEY"]
genai.configure(api_key=API_KEY)

# Inisialisasi model Gemini
model = genai.GenerativeModel("gemini-2.0-flash")

# Fungsi untuk mendapatkan respons dari Gemini
def get_gemini_response(user_input):
    response = model.generate_content(user_input)
    return response.text if response else "Maaf, terjadi kesalahan."

# Streamlit UI
st.title("Chatbot Gemini dengan Streamlit")

# Inisialisasi sesi
if "messages" not in st.session_state:
    st.session_state.messages = []
    # Kirim pesan "Halo" secara otomatis saat pertama kali dibuka
    first_message = "Halo"
    first_response = get_gemini_response(first_message)
    st.session_state.messages.append({"role": "user", "content": first_message})
    st.session_state.messages.append({"role": "bot", "content": first_response})

# Tampilkan semua pesan
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.chat_message("user").markdown(msg["content"])
    else:
        st.chat_message("assistant").markdown(msg["content"])

# Input pengguna
user_input = st.chat_input("Ketik pesan...")
if user_input:
    # Tampilkan pesan pengguna
    st.chat_message("user").markdown(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    # Dapatkan respons dari Gemini
    response = get_gemini_response(user_input)
    st.chat_message("assistant").markdown(response)
    st.session_state.messages.append({"role": "bot", "content": response})
