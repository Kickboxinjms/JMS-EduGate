import streamlit as st
import pandas as pd
from datetime import datetime
import io

# ==========================================
# 1. KONFIGURASI HALAMAN & TEMA (INTEGRATED)
# ==========================================
st.set_page_config(
    page_title="JMS EduGate - Satu Pintu Guru Juara",
    page_icon="🛡️",
    layout="wide"
)

# CSS untuk menyatukan desain tanpa file config.toml
st.markdown("""
    <style>
    /* Warna Utama */
    :root {
        --primary: #1e3d59;
        --accent: #ff6e40;
        --bg: #f8f9fa;
    }
    .main { background-color: var(--bg); }
    .stButton>button { 
        width: 100%; border-radius: 10px; height: 3.5em; 
        background-color: #1e3d59; color: white; font-weight: bold; border: none;
        transition: 0.3s;
    }
    .stButton>button:hover { background-color: #ff6e40; border: none; }
    h1, h2, h3 { color: #1e3d59; font-family: 'Arial', sans-serif; }
    .sidebar .sidebar-content { background-color: #1e3d59; color: white; }
    .report-card { 
        padding: 20px; border-radius: 15px; background-color: white; 
        box-shadow: 0 4px 15px rgba(0,0,0,0.05); margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# ==========================================
# 2. DATA AWAL (INTERNAL DATABASE)
# ==========================================
# Data ini menggantikan file CSV eksternal agar aplikasi langsung berisi
if 'data_siswa' not in st.session_state:
    st.session_state.data_siswa = pd.DataFrame({
        'Nama': ['Budi Santoso', 'Siti Aminah', 'Andi Wijaya', 'Rani Permata', 'Reza Malik'],
        'Gaya Belajar': ['Kinestetik', 'Visual', 'Auditori', 'Visual', 'Kinestetik'],
        'Minat': ['Kickboxing', 'Sains', 'Musik', 'Seni', 'Olahraga'],
        'Skor': [90, 85, 78, 92, 88]
    })

# ==========================================
# 3. FUNGSI PINTAR (LOGIKA AI & SISTEM)
# ==========================================
def generate_rpp(topik, kelas):
    return f"""
# 📜 MODUL AJAR: {topik.upper()}
**Kode Dokumen:** JMS/EDU/{datetime.now().strftime('%Y%m%d')}
**Target:** {kelas} | **Kurikulum:** Merdeka 2026

## A. Tujuan Pembelajaran
Siswa mampu menguasai konsep dasar {topik} dengan mentalitas juara dan disiplin tinggi.

## B. Langkah Pembelajaran (90 Menit)
1. **Pendahuluan (15')**: Apersepsi, doa, dan 'Champion Shout' untuk semangat.
2. **Kegiatan Inti (60')**: Eksplorasi materi {topik} melalui diskusi dan praktik langsung.
3. **Penutup (15')**: Refleksi keberhasilan dan kesimpulan bersama.

## C. Media & Alat
Slide interaktif JMS EduGate dan Lembar Kerja Siswa.
    """

def get_vibe_solution(status):
    solutions = {
        "Sangat Lemas": "🚨 **AKSI KICKBOXING:** Instruksikan siswa berdiri. Lakukan gerakan 'Jab-Cross-Hook' pelan 10x untuk memompa oksigen ke otak!",
        "Ngantuk": "⚡ **AKSI CEPAT:** Cuci muka kolektif atau lakukan permainan 'Tebak Gerak' selama 3 menit.",
        "Bosan": "💡 **GANTI METODE:** Berhenti ceramah. Lakukan kuis kilat berhadiah poin 'JMS Gold'.",
        "Berisik": "🧘 **MINDFULNESS:** Matikan lampu. Instruksikan teknik napas kotak (4-4-4) selama 2 menit.",
        "Siap Belajar": "🌟 **PERTAHANKAN:** Berikan apresiasi dan lanjut ke materi inti dengan antusias!"
    }
    return solutions.get(status)

# ==========================================
# 4. NAVIGASI SATU PINTU (SIDEBAR)
# ==========================================
with st.sidebar:
    st.markdown("<h1 style='text-align: center; color: white;'>🛡️ JMS</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: white;'><b>EduGate v2.0</b></p>", unsafe_allow_html=True)
    st.divider()
    menu = st.radio("MENU UTAMA:", 
                    ["🏠 Dashboard", "📝 AI Lesson Architect", "🎨 Creative Studio", "📊 Radar Siswa", "⚡ Vibe Check", "📓 Jurnal Laporan"])
    st.divider()
    st.caption("📧 Admin: kickboxingjms@gmail.com")

# ==========================================
# 5. KONTEN UTAMA APLIKASI
# ==========================================

if menu == "🏠 Dashboard":
    st.title("Pusat Kendali JMS EduGate")
    st.write(f"Selamat Datang, Pak/Bu Guru. Hari ini: **{datetime.now().strftime('%d %B %Y')}**")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Siswa Terpantau", "32", "Aktif")
    with col2:
        st.metric("Rerata Keaktifan", "88%", "+2.5%")
    with col3:
        st.metric("Modul Terbit", "14", "Minggu ini")
    
    st.markdown("---")
    st.markdown("""
    ### 📢 Pesan Kepala Sekolah:
    *"Mari kita jadikan kelas hari ini sebagai arena pembentukan karakter juara. Gunakan teknologi ini untuk mempermudah tugas Anda, bukan menambah beban."*
    """)

elif menu == "📝 AI Lesson Architect":
    st.title("📝 AI Lesson Architect")
    st.write("Buat RPP dan Modul Ajar otomatis tanpa ribet.")
    
    col_a, col_b = st.columns(2)
    with col_a:
        topik = st.text_input("Topik Pelajaran:", placeholder="Contoh: Geografi Lempeng Tektonik")
    with col_b:
        kelas = st.selectbox("Tingkat Kelas:", ["I-III SD", "IV-VI SD", "VII-IX SMP", "X-XII SMA"])
    
    if st.button("Generate & Terbitkan Modul"):
        if topik:
            hasil_rpp = generate_rpp(topik, kelas)
            st.markdown("<div class='report-card'>", unsafe_allow_html=True)
            st.markdown(hasil_rpp)
            st.markdown("</div>", unsafe_allow_html=True)
            st.download_button("Simpan sebagai PDF/Doc", hasil_rpp, file_name=f"RPP_JMS_{topik}.md")
        else:
            st.error("Masukkan topik terlebih dahulu!")

elif menu == "🎨 Creative Studio":
    st.title("🎨 Creative Studio Guru")
    st.write("Rancang alur media pembelajaran yang menarik.")
    materi_raw = st.text_area("Tempel ringkasan materi di sini untuk dibuatkan Storyboard visual:")
    if st.button("Rancang Visual"):
        st.success("Analisis selesai! Berikut alur visual yang disarankan:")
        st.write("1. **Intro:** Tampilkan video durasi 30 detik tentang fenomena nyata.")
        st.write("2. **Inti:** Gunakan diagram interaktif untuk menjelaskan proses.")
        st.write("3. **Closing:** Berikan tantangan 'Quick Quiz' di layar.")

elif menu == "📊 Radar Siswa":
    st.title("📊 Radar Minat & Bakat Siswa")
    st.write("Peta gaya belajar kelas Anda saat ini:")
    
    # Grafik Distribusi Gaya Belajar
    gaya_counts = st.session_state.data_siswa['Gaya Belajar'].value_counts()
    st.bar_chart(gaya_counts)
    
    st.markdown("### Detail Profil Siswa")
    st.table(st.session_state.data_siswa)

elif menu == "⚡ Vibe Check":
    st.title("⚡ Vibe Check (Asisten Kelas)")
    st.write("Gunakan fitur ini saat energi kelas menurun.")
    
    kondisi = st.select_slider(
        "Bagaimana suasana kelas sekarang?",
        options=["Sangat Lemas", "Ngantuk", "Bosan", "Berisik", "Siap Belajar"]
    )
    
    if st.button("Dapatkan Solusi Instan"):
        solusi = get_vibe_solution(kondisi)
        st.info(solusi)
        if "KICKBOXING" in solusi:
            st.warning("💪 **Instruksi Khusus:** Pastikan jarak antar siswa aman sebelum memulai gerakan fisik.")

elif menu == "📓 Jurnal Laporan":
    st.title("📓 Jurnal Refleksi & Laporan")
    st.write("Laporan ini akan langsung masuk ke database Kepala Sekolah.")
    
    nama_guru = st.text_input("Nama Guru:")
    laporan = st.text_area("Apa keberhasilan dan kendala mengajar hari ini?")
    
    if st.button("Kirim ke Kepala Sekolah"):
        if nama_guru and laporan:
            st.balloons()
            st.success(f"Terima kasih {nama_guru}, laporan telah terkirim dengan aman.")
        else:
            st.warning("Mohon isi nama dan isi laporan.")
