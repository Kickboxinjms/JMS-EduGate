import streamlit as st
import pandas as pd
from datetime import datetime

# --- KONFIGURASI HALAMAN ---
st.set_page_config(page_title="JMS EduGate - Deep Learning Engine", layout="wide", page_icon="🛡️")

# --- CUSTOM CSS (PROFESSIONAL & BOLD) ---
st.markdown("""
    <style>
    .stApp { background-color: #f8f9fa; }
    .main-header { background: linear-gradient(90deg, #1e3d59, #2e5a88); padding: 20px; border-radius: 15px; color: white; text-align: center; margin-bottom: 25px; }
    .module-box { background: white; padding: 30px; border-radius: 15px; border-left: 8px solid #ff6e40; box-shadow: 0 4px 12px rgba(0,0,0,0.1); margin-bottom: 20px; }
    .stButton>button { background-color: #1e3d59; color: white; border-radius: 10px; font-weight: bold; height: 3em; }
    .stButton>button:hover { background-color: #ff6e40; }
    </style>
    """, unsafe_allow_html=True)

# --- DATABASE STRUKTUR MODUL (BERDASARKAN DOKUMEN SOURCE) ---
def generate_deep_learning_module(topik, kelas, penyusun="ZULFADHLI ROMADHON, S.Pd.,Gr"):
    now = datetime.now()
    return f"""
# 🛡️ MODUL AJAR DEEP LEARNING (FASE F)
**MATA PELAJARAN:** Pendidikan Jasmani, Olahraga, & Kesehatan (PJOK)

---

## A. IDENTITAS MODUL
* **Nama Sekolah:** SMAN 1 MUARA SUGIHAN
* **Penyusun:** {penyusun}
* **Kelas / Fase:** {kelas} / F
* **Tahun Pelajaran:** 2025 / 2026
* **Alokasi Waktu:** 12 JP (4 Pertemuan)

## B. IDENTIFIKASI KESIAPAN PESERTA DIDIK
* Peserta didik memiliki tingkat kesiapan fisik dan pengetahuan awal yang bervariasi.
* Kebutuhan belajar mencakup pengenalan teknik bagi pemula dan penguatan taktik bagi yang mahir.
* Latar belakang sosial budaya mempengaruhi keakraban dengan aktivitas fisik.

## C. KARAKTERISTIK MATERI (DEEP LEARNING)
* **Pengetahuan:** Prosedural (langkah teknik), Konseptual (aturan), Metakognitif (analisis performa).
* **Relevansi Nyata:** Menumbuhkan kebugaran, kerja sama tim, sportivitas, dan kedisiplinan.
* **Nilai Karakter:** Pantang menyerah, tanggung jawab, dan saling menghargai.

## D. DIMENSI PROFIL LULUSAN
1. **Penalaran Kritis:** Mampu menganalisis situasi permainan dan membuat keputusan taktis.
2. **Kreativitas:** Mengaplikasikan variasi gerak untuk solusi dalam permainan.
3. **Kolaborasi:** Bekerja sama efektif dalam tim untuk tujuan bersama.
4. **Kemandirian:** Mampu mengelola diri dan berlatih secara inisiatif.
5. **Kesehatan:** Memahami pentingnya pola hidup sehat melalui olahraga.

## E. DESAIN PEMBELAJARAN (KERANGKA KERJA)
* **Model:** Teaching Games for Understanding (TGfU) / Discovery Learning.
* **Strategi:** Joyful Learning (pendekatan bermain), Meaningful Learning (simulasi nyata), Mindful Learning (refleksi).
* **Digital:** Google Classroom, YouTube Tutorial, dan Video Replay untuk Peer-Feedback.

## F. LANGKAH PEMBELAJARAN BERDIFERENSIASI
### 1. Kegiatan Pendahuluan (15 Menit)
* **Ritual Mindful:** Latihan pernapasan singkat untuk fokus.
* **Apersepsi Joyful:** Video cuplikan pertandingan inspiratif.
* **Pertanyaan Pemantik:** "Apa peran teknik ini dalam kemenangan sebuah tim?"

### 2. Kegiatan Inti (60 Menit)
* **Memahami:** Demonstrasi teknik dasar melalui video dan kartu tugas bergambar.
* **Mengaplikasi (Diferensiasi Proses):**
    * *Kelompok Dasar:* Fokus pada teknik statis dengan bantuan guru.
    * *Kelompok Menengah:* Latihan variasi jarak dan bergerak.
    * *Kelompok Mahir:* Simulasi tanding dengan tantangan taktik kompleks.
* **Merefleksi:** Peserta didik merekam performa teman dan memberikan masukan (Peer-Coaching).

### 3. Kegiatan Penutup (15 Menit)
* Pendinginan dan refleksi bersama tentang tantangan yang dihadapi.
* Guru memberikan apresiasi atas sportivitas dan usaha peserta didik.

## G. ASESMEN PEMBELAJARAN
### 1. Asesmen Diagnostik (Awal)
* Kuesioner minat dan tes praktik keterampilan dasar (misal: memantulkan bola 30 detik).

### 2. Asesmen Formatif (Proses)
* Lembar observasi sikap (disiplin, kerja sama) dan rubrik performa saat drill.

### 3. Asesmen Sumatif (Akhir)
* **Kinerja:** Pertandingan modifikasi (3v3 atau 5v5).
* **Proyek:** Laporan analisis taktik tim profesional dalam bentuk infografis/video.
* **Tertulis:** Evaluasi pemahaman aturan dan strategi permainan.

---
**Mengetahui,** **Guru Mata Pelajaran,**
Kepala Sekolah                                  {penyusun}
    """

# --- SIDEBAR NAVIGATION ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3429/3429433.png", width=80)
    st.title("JMS EduGate")
    menu = st.radio("MODUL SISTEM:", ["Dashboard", "AI Module Generator", "Rubrik Asesmen", "Database Siswa", "Vibe Check"])
    st.divider()
    st.write("Logged in as: kickboxingjms@gmail.com")

# --- LOGIC PER MENU ---
if menu == "Dashboard":
    st.markdown("<div class='main-header'><h1>Pusat Kendali Guru Juara</h1><p>Sistem Operasi Deep Learning SMAN 1 Muara Sugihan</p></div>", unsafe_allow_html=True)
    st.info("Aplikasi ini telah disinkronkan dengan Modul Ajar PJOK 2025/2026.")
    
elif menu == "AI Module Generator":
    st.title("📝 AI Deep Learning Generator")
    st.write("Hasilkan Modul Ajar Lengkap berdasarkan Struktur Deep Learning.")
    
    col1, col2 = st.columns(2)
    with col1:
        topik = st.selectbox("Pilih Unit Olahraga:", 
                            ["Bola Basket", "Bola Voli", "Sofbol", "Pencak Silat", "Lompat Jangkit", "Lempar Cakram", "Senam Irama", "Kebugaran", "HIV/AIDS"])
    with col2:
        kelas = st.selectbox("Pilih Kelas:", ["XII", "XI", "X"])
        
    if st.button("Generate Modul Lengkap"):
        modul = generate_deep_learning_module(topik, kelas)
        st.markdown("<div class='module-box'>", unsafe_allow_html=True)
        st.markdown(modul)
        st.markdown("</div>", unsafe_allow_html=True)
        st.download_button("Download Modul (MD)", modul, file_name=f"Modul_JMS_{topik}.md")

elif menu == "Rubrik Asesmen":
    st.title("📊 Rubrik Asesmen Komprehensif")
    st.write("Detail kriteria penilaian untuk aspek Keterampilan, Taktik, dan Sikap.")
    
    st.subheader("1. Rubrik Penilaian Kinerja (Permainan)")
    st.table(pd.DataFrame({
        "Aspek": ["Teknik Dasar", "Taktik", "Kerja Sama", "Sportivitas"],
        "Kriteria Baik (4)": ["Gerak akurat & konsisten", "Keputusan taktis tepat", "Komunikasi aktif", "Menghargai lawan & aturan"],
        "Kriteria Cukup (2)": ["Gerak cukup tapi belum stabil", "Sering salah posisi", "Kurang komunikasi", "Kadang emosional"]
    }))

elif menu == "Vibe Check":
    st.title("⚡ Vibe Check (Instruksi Real-Time)")
    mood = st.select_slider("Kondisi Kelas?", ["Ngantuk", "Bosan", "Berisik", "Siap"])
    if st.button("Dapatkan Solusi"):
        if mood == "Ngantuk":
            st.error("🔥 **SOLUSI:** Gerakan 'Double Jab - Cross' Kickboxing 10 set untuk memacu adrenalin!")
        elif mood == "Berisik":
            st.warning("🧘 **SOLUSI:** Mindful Breathing (4-4-4) untuk menenangkan saraf.")
        else:
            st.success("🌟 **SOLUSI:** Lanjutkan materi inti dengan tantangan kompetisi kecil.")
