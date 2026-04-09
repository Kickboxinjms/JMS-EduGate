import streamlit as st
import pandas as pd
from datetime import datetime

# ==========================================
# 1. KONFIGURASI HALAMAN & TEMA
# ==========================================
st.set_page_config(
    page_title="JMS EduGate - SMAN 1 Muara Sugihan",
    page_icon="🛡️",
    layout="wide"
)

# CSS untuk tampilan premium dan profesional
st.markdown("""
    <style>
    .stApp { background-color: #f4f7f9; }
    .main-header { 
        background: linear-gradient(135deg, #1e3d59 0%, #2e5a88 100%); 
        padding: 30px; border-radius: 20px; color: white; text-align: center; 
        margin-bottom: 30px; box-shadow: 0 10px 20px rgba(0,0,0,0.1);
    }
    .module-card { 
        background: white; padding: 40px; border-radius: 25px; 
        border-top: 12px solid #ff6e40; box-shadow: 0 15px 35px rgba(0,0,0,0.05); 
    }
    .stButton>button { 
        background-color: #1e3d59; color: white; border-radius: 12px; 
        font-weight: bold; height: 3.8em; border: none; transition: 0.3s;
    }
    .stButton>button:hover { background-color: #ff6e40; transform: translateY(-2px); }
    </style>
    """, unsafe_allow_html=True)

# ==========================================
# 2. ENGINE GENERATOR (LOGIKA DEEP LEARNING)
# ==========================================
def generate_universal_module(mapel, topik, kelas, penyusun):
    """
    Menghasilkan modul ajar dengan pola Deep Learning sesuai referensi dokumen PJOK.
    """
    return f"""
# 🛡️ MODUL AJAR DEEP LEARNING: {mapel.upper()}
**INSTITUSI:** SMAN 1 MUARA SUGIHAN

---

## I. IDENTITAS MODUL [cite: 4-10]
* **Mata Pelajaran:** {mapel}
* **Topik Utama:** {topik}
* **Penyusun:** {penyusun}
* **Kelas / Fase / Semester:** {kelas} / F / Ganjil
* **Tahun Pelajaran:** 2025 / 2026

## II. IDENTIFIKASI KESIAPAN PESERTA DIDIK [cite: 11-17]
* **Kesiapan Kognitif:** Peserta didik memiliki tingkat pemahaman awal yang bervariasi mengenai {topik}[cite: 12].
* **Kebutuhan Belajar:** Diferensiasi instruksi diperlukan untuk menjembatani siswa pemula hingga tingkat lanjut [cite: 16-17].

## III. KARAKTERISTIK MATERI [cite: 18-23]
* **Jenis Pengetahuan:** Konseptual (Teori), Prosedural (Langkah kerja), dan Metakognitif (Refleksi diri)[cite: 19].
* **Relevansi Nyata:** Membangun kemandirian, nalar kritis, dan kolaborasi [cite: 26-30].

## IV. DESAIN PEMBELAJARAN (DEEP LEARNING FRAMEWORK) [cite: 59-63, 522-525]
* **Capaian Pembelajaran (CP):** Sesuai Keputusan Kepala BSKAP Nomor 032/H/KR/2024[cite: 32, 492].
* **Mindful Learning:** Fokus pada kesadaran diri dan konsentrasi siswa terhadap materi[cite: 523].
* **Meaningful Learning:** Menghubungkan {topik} dengan disiplin ilmu lain (Fisika/Biologi/Matematika) dan kehidupan nyata [cite: 38-41, 316-320, 524].
* **Joyful Learning:** Menciptakan suasana belajar yang menggembirakan melalui eksplorasi digital dan simulasi[cite: 525].

## V. LANGKAH PEMBELAJARAN BERDIFERENSIASI [cite: 78-106, 541-594]
### A. Kegiatan Pendahuluan (15 Menit) [cite: 80-86]
* Guru memulai dengan pertanyaan pemantik untuk memicu kesadaran (Mindful Learning) [cite: 81-82].
* Menayangkan media visual yang menginspirasi untuk membangkitkan antusiasme (Joyful Learning)[cite: 83].

### B. Kegiatan Inti (60 Menit) [cite: 87-100]
* **Diferensiasi Konten:** Menyediakan berbagai sumber belajar (Video, Artikel, atau Kartu Tugas) [cite: 88-90].
* **Diferensiasi Proses (Berdasarkan Kesiapan):** [cite: 368, 375-379]
    * *Kelompok Dasar:* Pendampingan intensif (scaffolding) pada teknik/konsep fundamental[cite: 94, 377].
    * *Kelompok Menengah:* Latihan variasi dan pengembangan pemahaman[cite: 378].
    * *Kelompok Mahir:* Tantangan analisis mandiri atau simulasi kompleks[cite: 95, 379].
* **Diferensiasi Produk:** Kebebasan memilih format laporan hasil belajar (Video/Poster/Jurnal) [cite: 98-100, 221-223].

### C. Kegiatan Penutup (15 Menit) [cite: 101-106]
* Refleksi bersama mengenai tantangan dan strategi pemecahan masalah [cite: 102-104].
* Pendinginan fisik/mental dan perencanaan pembelajaran mandiri selanjutnya [cite: 415-420].

## VI. ASESMEN PEMBELAJARAN [cite: 228-278, 595-636]
1. **Asesmen Diagnostik (Awal):** Mengidentifikasi pengetahuan awal dan minat [cite: 229-236, 596-602].
2. **Asesmen Formatif (Proses):** Observasi partisipasi, jurnal refleksi, dan peer-feedback [cite: 237-251, 603-612].
3. **Asesmen Sumatif (Akhir):** Penilaian kinerja proyek, analisis taktik/strategi, dan tes tertulis [cite: 252-278, 613-636].

---
**Mengetahui,** **Palembang, {datetime.now().strftime('%d %B %Y')}**
**Kepala Sekolah** **Guru Mata Pelajaran**

**(BUDIYONO S.Pd M.Pd)** **({penyusun})**
NIP. 196911042001121004                       NIP. [Input NIP Guru]
    """

# ==========================================
# 3. ANTARMUKA PENGGUNA (UI)
# ==========================================

# Sidebar Navigasi
with st.sidebar:
    st.markdown("<h2 style='text-align: center;'>🛡️ JMS EduGate</h2>", unsafe_allow_html=True)
    st.caption("Pusat Kendali Deep Learning SMAN 1 Muara Sugihan")
    st.divider()
    menu = st.radio("SISTEM NAVIGASI:", 
                    ["🏠 Dashboard Utama", "📝 Generator Modul (Semua Mapel)", "📊 Bank Rubrik Asesmen", "⚡ Vibe Check Kelas"])
    st.divider()
    nama_guru = st.text_input("Nama Penyusun:", "ZULFADHLI ROMADHON, S.Pd.,Gr")
    st.info("Email Admin: kickboxingjms@gmail.com")

# Halaman Dashboard
if menu == "🏠 Dashboard Utama":
    st.markdown("<div class='main-header'><h1>Selamat Datang di JMS EduGate</h1><p>Mewujudkan Generasi Juara Melalui Deep Learning</p></div>", unsafe_allow_html=True)
    
    c1, c2, c3 = st.columns(3)
    c1.metric("Standar Kualitas", "Deep Learning", "Standardized")
    c2.metric("Referensi Kurikulum", "CP No. 32 Thn 2024", "Updated")
    c3.metric("Status Sistem", "Universal", "All Subjects")

    st.markdown("---")
    st.markdown("""
    ### 🛡️ Filosofi Pembelajaran SMAN 1 Muara Sugihan
    Aplikasi ini mengintegrasikan kerangka **Deep Learning** ke dalam setiap mata pelajaran [cite: 62, 522-525]:
    * **Mindful Learning:** Menanamkan kesadaran penuh dalam setiap proses belajar[cite: 523].
    * **Meaningful Learning:** Menghubungkan setiap materi dengan realitas kehidupan[cite: 524].
    * **Joyful Learning:** Memastikan proses belajar berlangsung secara menyenangkan dan antusias[cite: 525].
    """)

# Halaman Generator
elif menu == "📝 Generator Modul (Semua Mapel)":
    st.title("📝 Universal AI Module Generator")
    st.write("Buat Modul Ajar berstandar Deep Learning untuk mata pelajaran apa pun.")
    
    with st.container():
        col_left, col_right = st.columns(2)
        with col_left:
            mapel = st.selectbox("Pilih Mata Pelajaran:", 
                                ["Matematika", "Fisika", "Biologi", "Kimia", "Geografi", "Sejarah", 
                                 "Bahasa Indonesia", "Bahasa Inggris", "Seni Budaya", "PJOK", "PAI", "PKn"])
        with col_right:
            topik = st.text_input("Input Topik Spesifik:", placeholder="Misal: Lempeng Tektonik atau Statistika")
        
        tingkat = st.select_slider("Tingkat Kelas:", options=["X", "XI", "XII"])
        
        if st.button("Generate & Terbitkan Modul"):
            if topik:
                with st.spinner("Sedang memproses modul sesuai standar SMAN 1 Muara Sugihan..."):
                    hasil_modul = generate_universal_module(mapel, topik, tingkat, nama_guru)
                    st.markdown("<div class='module-card'>", unsafe_allow_html=True)
                    st.markdown(hasil_modul)
                    st.markdown("</div>", unsafe_allow_html=True)
                    st.download_button("Unduh Modul (.md)", hasil_modul, file_name=f"Modul_{mapel}_{topik}.md")
            else:
                st.error("Mohon masukkan topik pelajaran terlebih dahulu.")

# Halaman Rubrik Asesmen
elif menu == "📊 Bank Rubrik Asesmen":
    st.title("📊 Bank Rubrik Standar Deep Learning")
    st.write("Kriteria penilaian ini diadopsi dari standar instrumen penilaian PJOK [cite: 258-271, 619-627].")
    
    rubrik = {
        "Kriteria": ["Pemahaman Konsep", "Aplikasi Teknik/Strategi", "Kolaborasi & Komunikasi", "Penalaran Kritis & Kreativitas"],
        "Sangat Baik (4)": ["Analisis mendalam, akurat & relevan", "Penerapan lancar tanpa kesalahan teknis", "Aktif, suportif & koordinasi tim yang kuat", "Menyajikan solusi/variasi gerak yang inovatif"],
        "Cukup (2)": ["Pemahaman dasar/hanya hafal definisi", "Cukup lancar dengan bantuan/koreksi", "Bekerja secara individu, kurang interaksi", "Hanya mengikuti instruksi standar"]
    }
    st.table(pd.DataFrame(rubrik))
    st.caption("Gunakan rubrik ini untuk penilaian Asesmen Sumatif (Kinerja & Proyek).")

# Halaman Vibe Check
elif menu == "⚡ Vibe Check Kelas":
    st.title("⚡ Vibe Check (Manajemen Kelas Real-Time)")
    st.write("Tingkatkan energi kelas dalam sekejap dengan instruksi berbasis kondisi psikologis.")
    
    status = st.selectbox("Bagaimana kondisi kelas saat ini?", ["Ngantuk Berat", "Sangat Berisik", "Kurang Fokus", "Siap Belajar"])
    if st.button("Dapatkan Solusi!"):
        if status == "Ngantuk Berat":
            st.error("🚨 **SOLUSI KICKBOXING:** Instruksikan siswa berdiri. Lakukan gerakan 'Double Jab - Cross' sebanyak 10 set. Teriakkan 'JUARA!' di akhir gerakan!")
        elif status == "Sangat Berisik":
            st.warning("🤫 **SOLUSI MINDFULNESS:** Hening sejenak selama 2 menit. Lakukan teknik napas kotak (4 detik tarik, 4 tahan, 4 buang).")
        elif status == "Kurang Fokus":
            st.info("🎮 **SOLUSI GAME:** Lakukan kuis kilat 3 pertanyaan interaktif berhadiah poin apresiasi.")
        else:
            st.success("🌟 **PERTAHANKAN:** Berikan apresiasi dan lanjut ke inti materi dengan antusiasme tinggi!")
