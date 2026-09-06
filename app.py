import streamlit as st
from google import genai

# 1. Inisialisasi API Key pakai library baru
API_KEY = st.secrets["GEMINI_API_KEY"]
client = genai.Client(api_key=API_KEY)

# 2. Pengaturan UI
st.set_page_config(page_title="CS Rumah Sakit", page_icon="🏥")
st.title("🏥 Layanan Pelanggan RS Sehat Selalu")
st.write("Halo! Saya asisten virtual RS Sehat Selalu. Ada yang bisa saya bantu?")

# 3. Memori Percakapan
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 4. Prompt System & Logika Chatbot
prompt_system = "Kamu adalah asisten customer service virtual untuk Rumah Sakit Sehat Selalu. Jawab dengan sopan, ramah, dan penuh empati. Fokus berikan informasi seputar pendaftaran, jadwal dokter, asuransi, dan fasilitas rumah sakit. Jangan berikan diagnosis medis."

if prompt := st.chat_input("Ketik pertanyaan Anda di sini..."):
    # Simpan chat user
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    full_prompt = f"{prompt_system}\n\nPertanyaan Pasien: {prompt}"

    # Panggil Gemini pakai syntax terbaru
    with st.chat_message("assistant"):
        with st.spinner("Sedang memproses..."):
            try:
                response = client.models.generate_content(
                    model='gemini-3.6-flash',
                    contents=full_prompt
                )
                st.markdown(response.text)
                st.session_state.messages.append({"role": "assistant", "content": response.text})
            except Exception as e:
                # Kalau masih error, error aslinya bakal muncul di layar
                st.error(f"Error dari sistem: {e}")