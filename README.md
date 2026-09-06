#  AI-Powered Customer Service Chatbot for Hospital

Aplikasi *Customer Service* Chatbot berbasis Large Language Model (LLM) yang terintegrasi dengan Google Gemini API dan dibangun menggunakan framework Streamlit. Proyek ini dibuat sebagai pemenuhan **Final Project** untuk program pelatihan *LLM-Based Tools and Gemini API Integration for Data Scientists* yang diselenggarakan oleh Hacktiv8.

## 🚀 Live Demo
Aplikasi dapat diakses secara langsung melalui tautan berikut:
👉 [Streamlit App Link](https://chatbot-customer-service-rumah-sakit-vu5fcvlra6mw94henmtsrv.streamlit.app/)

---

##  Fitur & Karakteristik Utama
* **AI-Driven Customer Service:** Menggunakan model Google Gemini (`gemini-1.5-flash`) untuk memahami dan merespons pertanyaan pasien secara alami.
* **Parameter Kreatif (System Prompting):** Dikonfigurasi secara khusus agar memiliki kepribadian yang sopan, ramah, dan berempati layaknya petugas *customer service* rumah sakit profesional (fokus pada informasi pendaftaran, jadwal dokter, dan fasilitas, serta menghindari diagnosis medis).
* **Interactive UI:** Dibangun menggunakan **Streamlit**, menyediakan antarmuka obrolan (*chat interface*) yang interaktif dan mudah digunakan.
* **Conversational Memory:** Memiliki fitur manajemen sesi percakapan (*session state*) sehingga riwayat *chat* tetap tersimpan dengan baik selama sesi aktif.

---

##  Tech Stack
* **Python** (Bahasa pemrograman utama)
* **Streamlit** (Frontend & Web Framework)
* **Google Generative AI SDK** (`google-generativeai`)
* **Google Gemini API** (LLM Engine)

---

##  Cara Menjalankan Proyek secara Lokal

1. **Clone repository ini:**
   ```bash
   git clone https://github.com/bayurahmatt/Chatbot-Customer-Service-Rumah-Sakit.git
   cd Chatbot-Customer-Service-Rumah-Sakit
   Install dependencies yang dibutuhkan:

  ```Bash
  pip install -r requirements.txt
  ```Konfigurasi API Key:
     Buat folder .streamlit dan file secrets.toml di dalam direktori proyek, lalu masukkan API Key Anda:
      Ini, TOML
      GEMINI_API_KEY = "masukkan_api_key_gemini_anda_di_sini"
Jalankan aplikasi Streamlit:
Bash
streamlit run app.py


dan jika mau berjalan di lokal 
npm install localtunnel
!streamlit run app.py & npx localtunnel --port 8501
