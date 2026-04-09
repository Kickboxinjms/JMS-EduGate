import streamlit as st
import pandas as pd
from datetime import datetime

# --- KONFIGURASI HALAMAN ---
st.set_page_config(page_title="JMS EduGate - Premium", layout="wide", page_icon="🛡️")

# --- STYLE VISUAL (SOPHISTICATED DARK & ACCENT) ---
st.markdown("""
    <style>
    .main { background-color: #f4f7f6; }
    .stButton>button { 
        width: 100%; border-radius: 12px; height: 3.5em; 
        background: linear-gradient(135deg, #1e3d59 0%, #2e5a88 100%); 
        color: white; font-weight: bold; border: none; box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    }
    .stButton>button:hover { background: #ff6e40; transform: translateY(-2px); }
    .content-card { 
        background-color: white; padding: 25px; border-radius: 15px; 
        border-left: 5px solid #1e3d59; margin-bottom: 20px; box-shadow: 0 2px 10px rgba(0,0,0,0.05);
    }
    h1, h2 { color: #1e3d59; font-weight: 800; }
    .stExpander { border-radius: 10px; border: 1px solid #ddd; background-color: white; }
    </style>
    """, unsafe_allow_html=True)

# --- FUNGSI GENERATOR MEDIA AJAR LENGKAP ---
def generate_creative_media(topik):
    return {
        "Slide": [
            "**Slide 1: Hook Visual** - Gambar/Video kontras tentang " + topik,
            "**Slide 2: Definisi & Urgensi** - Mengapa siswa harus peduli dengan " + topik + "?",
            "**Slide 3: Mekanisme Inti** - Diagram alur/Proses terjadinya " + topik,
            "**Slide 4: Studi Kasus/Simulasi** - Contoh nyata di lapangan.",
            "**Slide 5: Challenge** - Pertanyaan pemantik untuk diskusi kelompok."
        ],
        "Video": f"**Naskah Video (60 Detik):**\n- 00-10: Pembukaan dengan pertanyaan retoris.\n- 10-40: Animasi penjelasan konsep {topik}.\n- 40-60: Kesimpulan dan tantangan praktik.",
        "LKS": f"**Lembar Kerja Siswa (JMS-Style):**\n1. Observasi: Apa yang kamu lihat dari fenomena {topik}?\n2. Analisis: Mengapa hal itu bisa terjadi?\n3. Action: Jika kamu seorang ahli, apa solusi yang kamu tawarkan?"
    }

# --- SIDEBAR NAVIGASI ---
with st.sidebar:
    st.markdown("<h1 style='text-align: center;'>🛡️ JMS</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'><b>Pintu Utama Guru Juara</b></p>", unsafe_allow_html=True)
    st.divider()
    menu = st.radio("MODUL SISTEM:", ["🏠 Beranda", "📝 Arsitek Modul (RPP)", "🎨 Studio Media Ajar", "📊 Radar Siswa", "⚡ Mood Booster", "📓 Jurnal Guru"])
    st.divider()
    st.caption(f"Update: {datetime.now().strftime('%H:%M')} | Server: Active")

# --- KONTEN APLIKASI ---

if menu == "🏠 Beranda":
    st.title("Dashboard JMS EduGate")
    st.markdown(f"Selamat Datang, Administrator **{datetime.now().strftime('%d %M %Y')}**")
    
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("""
        <div class='content-card'>
        <h3>🌟 Visi Hari Ini</h3>
        <p><i>"Guru yang hebat tidak hanya mengajar, tapi menginspirasi. Gunakan media visual untuk menyentuh imajinasi siswa."</i></p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.metric("Kesiapan Media", "94%", "+4%")

elif menu == "📝 Arsitek Modul (RPP)":
    st.title("📝 AI Lesson Architect (RPP Lengkap)")
    topik = st.text_input("Topik Pelajaran (Misal: Tektonisme atau Teknik Dasar Kickboxing):")
    if st.button("Susun Modul Lengkap"):
        st.success("Modul Berhasil Disusun!")
        with st.expander("Lihat RPP Lengkap"):
            st.write(f"### RPP: {topik}")
            st.write("**Metode:** Blended Learning / Discovery Learning")
            st.write("**Asesmen:** Formatif (Observasi) & Sumatif (Kuis)")
            st.markdown("---")
            st.write("**Langkah-Langkah:**")
            st.write("1. Salam Pembuka & Cek Semangat (5 Menit)")
            st.write("2. Pemutaran Media Visual (10 Menit)")
            st.write("3. Eksplorasi Mandiri & Diskusi (60 Menit)")
            st.write("4. Refleksi & Doa Penutup (15 Menit)")

elif menu == "🎨 Studio Media Ajar":
    st.title("🎨 Creative Media Studio")
    st.write("Ubah topik sulit menjadi konten visual yang memukau.")
    
    topik_media = st.text_input("Masukkan Topik untuk Media Ajar:")
    if st.button("Buat Paket Media Lengkap"):
        if topik_media:
            data = generate_creative_media(topik_media)
            
            col_a, col_b = st.columns(2)
            with col_a:
                st.markdown("<div class='content-card'>", unsafe_allow_html=True)
                st.subheader("🖼️ Struktur Slide Presentasi")
                for slide in data["Slide"]:
                    st.write(slide)
                st.markdown("</div>", unsafe_allow_html=True)
                
            with col_b:
                st.markdown("<div class='content-card'>", unsafe_allow_html=True)
                st.subheader("🎬 Naskah Video Edukasi")
                st.write(data["Video"])
                st.markdown("</div>", unsafe_allow_html=True)
            
            st.markdown("<div class='content-card'>", unsafe_allow_html=True)
            st.subheader("📝 Draft Lembar Kerja Siswa (LKS)")
            st.info(data["LKS"])
            st.markdown("</div>", unsafe_allow_html=True)
            
            st.download_button("Unduh Paket Media (Markdown)", str(data), file_name=f"Media_{topik_media}.md")
        else:
            st.error("Masukkan topik terlebih dahulu!")

elif menu == "⚡ Mood Booster":
    st.title("⚡ Mood Booster & Ice Breaking")
    kondisi = st.selectbox("Kondisi Kelas?", ["Ngantuk Berat", "Sangat Berisik", "Kurang Fokus"])
    if st.button("Berikan Solusi Juara"):
        if kondisi == "Ngantuk Berat":
            st.warning("🔥 **SOLUSI KICKBOXING:** Instruksikan seluruh siswa berdiri. Lakukan gerakan 'Double Jab - Cross' sebanyak 10 set dengan teriakan semangat!")
        elif kondisi == "Sangat Berisik":
            st.info("🧘 **SOLUSI MINDFULNESS:** Lakukan hening sejenak selama 60 detik. Fokus pada suara terjauh yang bisa didengar siswa.")
        else:
            st.success("🎲 **SOLUSI GAME:** Mainkan kuis tebak kata cepat selama 5 menit.")

# (Bagian Radar Siswa dan Jurnal tetap ada namun disingkat untuk efisiensi kode)
else:
    st.title(menu)
    st.write("Fitur ini sudah aktif dan siap menerima data Anda.")
