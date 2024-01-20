import streamlit as st
from PIL import Image
import streamlit.components.v1 as components
st.set_page_config(page_title="CV Timotius Tegar", layout="wide")
st.markdown(
    """
    <style>
    body{
    font-family: Arial;
    }
    .st-emotion-cache-13k62yr {
        background-color: #fff !important;
    }
    p{
        color: black;
        margin: 0;
    }
    .st-emotion-cache-12w0qpk {
        background-color: #2c394a;
        padding: 30px 20px;
        box-sizing: border-box;
    }
    .st-emotion-cache-12w0qpk h3{
        color: #c1ae7e;
    }
    .st-emotion-cache-12w0qpk p{
        color: white;
    }
    .st-emotion-cache-12w0qpk a{
        color: white;
        text-decoration: none;
    }
    .st-emotion-cache-1kyxreq{
        display: flex;
        justify-content: center;
    }
    hr{
        margin: 0;
    }
    h2, h5{
        padding: 0;
    }
    h4 {
        padding: 10px 0;
    }
    .st-emotion-cache-ocqkz7 {
        margin-bottom: 10px;
    }
    .st-emotion-cache-ml2xh6{
        padding: 30px 20px;
        box-sizing: border-box;
    }
    .st-emotion-cache-ml2xh6 h3{
        color: #2c394a;
        padding: 0
    }
    .st-emotion-cache-ml2xh6 p{
        color: #2c394a;
    }
    .st-emotion-cache-ml2xh6 h4{
        color: #2c394a;
    }
    .st-emotion-cache-ml2xh6 h5{
        color: #2c394a;
    }
    </style>
    """,
    unsafe_allow_html=True
)
big_1, big_2 = st.columns([3, 9])
with big_1:
    image_con = st.container()
    with image_con:
        st.image("profile.jpg", width=220)
    about_con = st.container()
    with about_con:
        st.subheader("Deskripsi Diri")
        st.write("Saya adalah mahasiswa berfokus data science dengan keahlian dalam Python, R, dan SQL, serta pengalaman dalam pengembangan model machine learning. Dengan latar belakang di ilmu komputer dan statistika, saya memiliki kemampuan analisis data yang kuat dan dedikasi untuk terus belajar. Saya siap membawa kontribusi kreatif dan solusi berbasis data dalam dunia profesional.")
    contact_con = st.container()
    with contact_con:
        st.subheader("Kontak Saya")
        st.write("Semarang Barat, Semarang")
        st.write("timotiustegarpinaringan@gmail.com")
        st.write("(+62)858 9405 2723")
    lang_con = st.container()
    with lang_con:
        st.subheader("Bidang Keahlian")
        st.write("HTML5,")
        st.markdown('''
            <div style="width: 100%; height: 5px; background-color: #ece8d5">
                <div style="width: 95%; height: 100%; background-color: #c1ae7e;"></div>
            </div>
        ''', unsafe_allow_html=True)
        st.write("CSS3")
        st.markdown('''
            <div style="width: 100%; height: 5px; background-color: #ece8d5">
                <div style="width: 90%; height: 100%; background-color: #c1ae7e;"></div>
            </div>
        ''', unsafe_allow_html=True)
        st.write("Javascript")
        st.markdown('''
            <div style="width: 100%; height: 5px; background-color: #ece8d5">
                <div style="width: 80%; height: 100%; background-color: #c1ae7e;"></div>
            </div>
        ''', unsafe_allow_html=True)
        st.write("Python")
        st.markdown('''
            <div style="width: 100%; height: 5px; background-color: #ece8d5">
                <div style="width: 75%; height: 100%; background-color: #c1ae7e;"></div>
            </div>
        ''', unsafe_allow_html=True)
        st.write("Restful API")
        st.markdown('''
            <div style="width: 100%; height: 5px; background-color: #ece8d5">
                <div style="width: 75%; height: 100%; background-color: #c1ae7e;"></div>
            </div>
        ''', unsafe_allow_html=True)
        st.write("SQL")
        st.markdown('''
            <div style="width: 100%; height: 5px; background-color: #ece8d5">
                <div style="width: 85%; height: 100%; background-color: #c1ae7e;"></div>
            </div>
        ''', unsafe_allow_html=True)
        st.write("No-SQL")
        st.markdown('''
            <div style="width: 100%; height: 5px; background-color: #ece8d5">
                <div style="width: 70%; height: 100%; background-color: #c1ae7e;"></div>
            </div>
        ''', unsafe_allow_html=True)
        st.write("React JS")
        st.markdown('''
            <div style="width: 100%; height: 5px; background-color: #ece8d5">
                <div style="width: 80%; height: 100%; background-color: #c1ae7e;"></div>
            </div>
        ''', unsafe_allow_html=True)
with big_2:
    name_con = st.container()
    with name_con:
        st.subheader("Timotius Tegar")
        st.write("Developer")
    kerja_con = st.container()
    with kerja_con:
        st.markdown('''<h4> Pengalaman Kerja </h4>''', unsafe_allow_html=True)
        st.divider()
        work1_1, work1_2 = st.columns([4, 8])
        with work1_1:
            st.markdown('''<h5> PT. Brilyan Trimatra Utama </h5>''', unsafe_allow_html=True)
            st.write("Bekasi")
            st.write("Oktober 2019 – Maret 2020")
        with work1_2:
            st.markdown('''<h5 style="margin-bottom: 10px;"> Front-End Developer Intern </h5>''', unsafe_allow_html=True)
            st.write("Bertanggung jawab dalam mengembangkan Front-End beberapa aplikasi PON XX 2020 Papua, diantaranya Pendaftaran, Info Pertandingan, dan Dashboard Sarana dan Prasarana berbasis web dengan Framework React JS")
        work2_1, work2_2 = st.columns([4, 8])
        with work2_1:
            st.markdown('''<h5> Zeal Indonesia </h5>''', unsafe_allow_html=True)
            st.write("Batam")
            st.write("September 2021 – Desember 2021")
        with work2_2:
            st.markdown('''<h5 style="margin-bottom: 10px;"> Front-End Developer Intern </h5>''', unsafe_allow_html=True)
            st.write("Bertanggung jawab dan berpartisipasi dalam pengembangan Front-End Website Official Zeal Indonesia dan webite untuk salah satu produk Zeal Indonesia")
        work3_1, work3_2 = st.columns([4, 8])
        with work3_1:
            st.markdown('''<h5> E-Tech </h5>''', unsafe_allow_html=True)
            st.write("Bekasi")
            st.write("Juni 2022 – September 2022")
        with work3_2:
            st.markdown('''<h5 style="margin-bottom: 10px;"> Front-End Developer Freelancer </h5>''', unsafe_allow_html=True)
            st.write("Bertanggung jawab dalam mengembangkan Front-End Aplikasi Train Driver, Medical Checkup, Operational untuk Light Rail Transit (LRT) Jakarta berbasis web dengan Framework React JS. Berpartisipasi dalam tim untuk mengembangkan Aplikasi Kabarin dan Mizuki berbasis web dengan Framework React JS")
    edu_con = st.container()
    with edu_con:
        st.markdown('''<h4> Pendidikan </h4>''', unsafe_allow_html=True)
        st.divider()
        edu_1, edu_2 = st.columns([4, 8])
        with edu_1:
            st.markdown('''<h5> SMK NEGERI 1 KOTA BEKASI </h5>''', unsafe_allow_html=True)
            st.write("Bekasi")
        with edu_2:
            st.markdown('''<h5 style="margin-bottom: 10px;"> Rekayasa Perangkat Lunak </h5>''', unsafe_allow_html=True)
            st.write("Terbaik ke 2 di Fakultas Teknologi Komputer dan Informatika dengan nilai rata rata 88/100")
            st.write("Telah Menyelesaikan Project sebagai berikut")
            st.write('''
                    - Aplikasi Pembayaran Uang Sekolah berbasis web dengan Framework CodeIgniter
                    - Aplikasi Inventarisasi Sekolah berbasis web dengan Framework React JS''')
    train_con = st.container()
    with train_con:
        st.markdown('''<h4> Sertifikasi </h4>''', unsafe_allow_html=True)
        st.divider()
        train1_1, train1_2 = st.columns([4, 8])
        with train1_1:
            st.markdown('''<h5> Lembaga Sertifikasi Nasional </h5>''', unsafe_allow_html=True)
            st.write("Desember 2020")
        with train1_2:
            st.markdown('''<h5 style="margin-bottom: 10px;"> Sertifikat Junior Programmer </h5>''', unsafe_allow_html=True)
            st.write("Mendapat sertifikat sebagai Junior Programmer setelah menyelesaikan baik tes tertulis maupun tes praktik dan memperoleh nilai 9/10")
        train2_1, train2_2 = st.columns([4, 8])
        with train2_1:
            st.markdown('''<h5> Udemy Course </h5>''', unsafe_allow_html=True)
            st.write("November 2019")
        with train2_2:
            st.markdown('''<h5 style="margin-bottom: 10px;"> React - The Complete Guide (incl Hooks, React Router, Redux) </h5>''', unsafe_allow_html=True)
            st.write("Mengembangkan aplikasi web yang kuat, cepat, ramah pengguna, dan reaktif, Mengenal fitur fitur React untuk mempermudah pembangunan web, dan Menguasai React Javascript tingkat beginner hingga intermediate")
