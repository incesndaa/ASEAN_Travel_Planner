import streamlit as st, locale
from streamlit_option_menu import option_menu
from logic import *
from geopy.distance import geodesic
locale.setlocale(locale.LC_ALL, 'id_ID.UTF-8')
# st.set_page_config(page_title="Konversi", page_icon="💰", layout="wide")
st.set_page_config(page_title="ASEAN Travel Planner", page_icon="🌏", layout="wide")

with st.sidebar:
    select = option_menu('FourCoders', 
                         ['Home', 
                          'Konversi Mata Uang', 
                          'Penghitung Jarak',
                          'Anggaran Perjalanan',
                          'Tabungan Perjalanan',
                          'Konsultasi Visa',
                          'Tentang Kami'],
                          icons=['house', 'currency-dollar', 'geo-alt', 'airplane', 'tags', 'plus', 'info-circle',],  
                          default_index=0,
                          styles={"container": {"background-color": "#f8f9fa"},
                                 "icon": {"color": "black", "font-size": "15px"},
                                 "nav-link": {"font-size": "16px", "text-align": "left"}})

if select == 'Home':
    st.title("🌏 **ASEAN Travel Planner** 🌏")
    st.markdown("""
        **Selamat datang di ASEAN Travel Planner!**  
        Aplikasi ini dirancang untuk membantu Anda merencanakan perjalanan ke negara-negara ASEAN dengan mudah dan praktis.  
        Dengan fitur-fitur seperti konversi mata uang, penghitung jarak antar negara, perhitungan anggaran perjalanan, dan simulasi tabungan, perjalanan Anda akan lebih terencana dengan baik.

        ### Fitur Aplikasi:
        - **Konversi Mata Uang**: Mengonversi mata uang antar negara-negara ASEAN.
        - **Penghitung Jarak Antar Negara**: Menghitung jarak antar negara di ASEAN.
        - **Anggaran Perjalanan**: Menghitung anggaran yang diperlukan untuk perjalanan Anda.
        - **Simulasi Tabungan**: Simulasi berapa lama waktu yang dibutuhkan untuk menabung.

        🚀 **Mudah dan Cepat!** 
    """)

elif select == 'Konversi Mata Uang':
    st.title('KONVERSI MATA UANG')

    col1, col2 = st.columns([1, 1])  

    with col1:
        mataUangAsal = st.selectbox("Pilih Mata Uang Asal", ["IDR", "MYR", "SGD", "THB", "PHP", "BND", "VND", "KHR", "LAK", "MMK"])
        benderaAsal = {
            "IDR": "https://upload.wikimedia.org/wikipedia/commons/9/9f/Flag_of_Indonesia.svg",
            "MYR": "https://upload.wikimedia.org/wikipedia/commons/6/66/Flag_of_Malaysia.svg",
            "SGD": "https://upload.wikimedia.org/wikipedia/commons/4/48/Flag_of_Singapore.svg",
            "THB": "https://upload.wikimedia.org/wikipedia/commons/a/a9/Flag_of_Thailand.svg",
            "PHP": "https://upload.wikimedia.org/wikipedia/commons/9/99/Flag_of_the_Philippines.svg",
            "BND": "https://upload.wikimedia.org/wikipedia/commons/9/9c/Flag_of_Brunei.svg",
            "VND": "https://upload.wikimedia.org/wikipedia/commons/2/21/Flag_of_Vietnam.svg",
            "KHR": "https://upload.wikimedia.org/wikipedia/commons/8/83/Flag_of_Cambodia.svg",
            "LAK": "https://upload.wikimedia.org/wikipedia/commons/5/56/Flag_of_Laos.svg",
            "MMK": "https://upload.wikimedia.org/wikipedia/commons/8/8c/Flag_of_Myanmar.svg"
        }[mataUangAsal]
        st.image(benderaAsal, width=50)

    with col2:
        mataUangTujuan = st.selectbox("Pilih Mata Uang Tujuan", ["IDR", "MYR", "SGD", "THB", "PHP", "BND", "VND", "KHR", "LAK", "MMK"])
        benderaTujuan = {
            "IDR": "https://upload.wikimedia.org/wikipedia/commons/9/9f/Flag_of_Indonesia.svg",
            "MYR": "https://upload.wikimedia.org/wikipedia/commons/6/66/Flag_of_Malaysia.svg",
            "SGD": "https://upload.wikimedia.org/wikipedia/commons/4/48/Flag_of_Singapore.svg",
            "THB": "https://upload.wikimedia.org/wikipedia/commons/a/a9/Flag_of_Thailand.svg",
            "PHP": "https://upload.wikimedia.org/wikipedia/commons/9/99/Flag_of_the_Philippines.svg",
            "BND": "https://upload.wikimedia.org/wikipedia/commons/9/9c/Flag_of_Brunei.svg",
            "VND": "https://upload.wikimedia.org/wikipedia/commons/2/21/Flag_of_Vietnam.svg",
            "KHR": "https://upload.wikimedia.org/wikipedia/commons/8/83/Flag_of_Cambodia.svg",
            "LAK": "https://upload.wikimedia.org/wikipedia/commons/5/56/Flag_of_Laos.svg",
            "MMK": "https://upload.wikimedia.org/wikipedia/commons/8/8c/Flag_of_Myanmar.svg"
        }[mataUangTujuan]
        st.image(benderaTujuan, width=50)

    jumlah = st.number_input(f"Masukkan jumlah {mataUangAsal} yang ingin dikonversi:")
    
    if st.button('Hitung'):
        if mataUangAsal != mataUangTujuan:
            konversi_objek = MataUang(mataUangAsal, mataUangTujuan, jumlah)
            hasil = konversi_objek.konversi()
            # hasil_formatted = "{:.2f}".format(hasil)
            st.success(f'{jumlah} {mataUangAsal} = {locale.currency(hasil, grouping=True, symbol=False)} {mataUangTujuan}')
        else:
            st.error("Mata uang asal dan tujuan tidak boleh sama!")

elif select == 'Penghitung Jarak':
    negaraAsean = {
        "Indonesia": (-6.1751, 106.8650),  # Jakarta
        "Malaysia": (3.1390, 101.6869),  # Kuala Lumpur
        "Thailand": (13.7563, 100.5018),  # Bangkok
        "Singapura": (1.3521, 103.8198),  # Singapura
        "Vietnam": (21.0285, 105.8542),  # Hanoi
        "Filipina": (14.5995, 120.9842),  # Manila
        "Brunei": (4.9031, 114.9398),  # Bandar Seri Begawan
        "Laos": (17.9757, 102.6331),  # Vientiane
        "Myanmar": (16.8409, 96.1735),  # Naypyidaw
        "Kamboja": (11.5564, 104.9282)  # Phnom Penh
    }

    st.title("Penghitung Jarak Antar Negara ASEAN")

    asal = st.selectbox("Pilih Negara Asal", list(negaraAsean.keys()))
    tujuan = st.selectbox("Pilih Negara Tujuan", list(negaraAsean.keys()))

    if st.button("Cek Jarak"):
        if asal and tujuan:
            koordinatAsal = negaraAsean[asal]
            koordinatTujuan = negaraAsean[tujuan]

            jarak = geodesic(koordinatAsal, koordinatTujuan).kilometers
            st.success(f"Jarak antara {asal} dan {tujuan} adalah {jarak:.2f} km.")

    st.write("\n**Catatan:** Jarak dihitung berdasarkan posisi koordinat ibu kota masing-masing negara.")


elif select == 'Anggaran Perjalanan':
    st.title('ANGGARAN PERJALANAN')

    col1, col2 = st.columns([1, 1])  

    with col1:
        mataUangAsal = st.selectbox("Pilih Mata Uang Asal", ["IDR", "MYR", "SGD", "THB", "PHP", "BND", "VND", "KHR", "LAK", "MMK"])
        benderaAsal = {
            "IDR": "https://upload.wikimedia.org/wikipedia/commons/9/9f/Flag_of_Indonesia.svg",
            "MYR": "https://upload.wikimedia.org/wikipedia/commons/6/66/Flag_of_Malaysia.svg",
            "SGD": "https://upload.wikimedia.org/wikipedia/commons/4/48/Flag_of_Singapore.svg",
            "THB": "https://upload.wikimedia.org/wikipedia/commons/a/a9/Flag_of_Thailand.svg",
            "PHP": "https://upload.wikimedia.org/wikipedia/commons/9/99/Flag_of_the_Philippines.svg",
            "BND": "https://upload.wikimedia.org/wikipedia/commons/9/9c/Flag_of_Brunei.svg",
            "VND": "https://upload.wikimedia.org/wikipedia/commons/2/21/Flag_of_Vietnam.svg",
            "KHR": "https://upload.wikimedia.org/wikipedia/commons/8/83/Flag_of_Cambodia.svg",
            "LAK": "https://upload.wikimedia.org/wikipedia/commons/5/56/Flag_of_Laos.svg",
            "MMK": "https://upload.wikimedia.org/wikipedia/commons/8/8c/Flag_of_Myanmar.svg"
        }[mataUangAsal]
        st.image(benderaAsal, width=50)

    with col2:
        mataUangTujuan = st.selectbox("Pilih Mata Uang Tujuan", ["IDR", "MYR", "SGD", "THB", "PHP", "BND", "VND", "KHR", "LAK", "MMK"])
        benderaTujuan = {
            "IDR": "https://upload.wikimedia.org/wikipedia/commons/9/9f/Flag_of_Indonesia.svg",
            "MYR": "https://upload.wikimedia.org/wikipedia/commons/6/66/Flag_of_Malaysia.svg",
            "SGD": "https://upload.wikimedia.org/wikipedia/commons/4/48/Flag_of_Singapore.svg",
            "THB": "https://upload.wikimedia.org/wikipedia/commons/a/a9/Flag_of_Thailand.svg",
            "PHP": "https://upload.wikimedia.org/wikipedia/commons/9/99/Flag_of_the_Philippines.svg",
            "BND": "https://upload.wikimedia.org/wikipedia/commons/9/9c/Flag_of_Brunei.svg",
            "VND": "https://upload.wikimedia.org/wikipedia/commons/2/21/Flag_of_Vietnam.svg",
            "KHR": "https://upload.wikimedia.org/wikipedia/commons/8/83/Flag_of_Cambodia.svg",
            "LAK": "https://upload.wikimedia.org/wikipedia/commons/5/56/Flag_of_Laos.svg",
            "MMK": "https://upload.wikimedia.org/wikipedia/commons/8/8c/Flag_of_Myanmar.svg"
        }[mataUangTujuan]
        st.image(benderaTujuan, width=50)

    biayaTransportasi = st.number_input("Masukkan biaya transportasi (per hari):", min_value=0.0)
    biayaAkomodasi = st.number_input("Masukkan biaya akomodasi (per hari):", min_value=0.0)
    biayaMakanan = st.number_input("Masukkan biaya makanan (per hari):", min_value=0.0)
    durasiPerjalanan = st.number_input("Masukkan durasi perjalanan (hari):", min_value=1)

    if st.button("Hitung Anggaran"):
        anggaranObjek = AnggaranPerjalanan(biayaTransportasi, biayaAkomodasi, biayaMakanan, durasiPerjalanan)
        totalAnggaran = anggaranObjek.hitungAnggaran()
        if mataUangAsal != mataUangTujuan:
            konversiAnggaran = MataUang(mataUangAsal, mataUangTujuan, totalAnggaran)
            hasilAnggaran = konversiAnggaran.konversi()
            st.success(f'Total Anggaran anda = {locale.currency(totalAnggaran, grouping=True, symbol=False)} {mataUangAsal}')
            st.success(f'Jika dikonversi ke negara tujuan anda = {locale.currency(hasilAnggaran, grouping=True, symbol=False)} {mataUangTujuan}')
        else:
            st.error("Mata uang asal dan tujuan tidak boleh sama!")

elif select == 'Tabungan Perjalanan':
    st.title('TABUNGAN PERJALANAN')

    mataUangAnggaran = st.selectbox("Pilih Mata Uang untuk Anggaran Perjalanan", ["IDR", "MYR", "SGD", "THB", "PHP", "BND", "VND", "KHR", "LAK", "MMK"])
    
    anggaranPerjalanan = st.number_input(f"Masukkan anggaran perjalanan (dalam {mataUangAnggaran}):", min_value=0.0)
    durasiTabungan = st.number_input("Masukkan durasi tabungan (bulan):", min_value=1)
    jumlahYangSudahDitabung = st.number_input("Masukkan jumlah uang yang sudah ditabung:", min_value=0.0)

    if st.button("Hitung Simulasi Tabungan"):
    
        if anggaranPerjalanan > jumlahYangSudahDitabung:
            tabungan = Tabungan(anggaranPerjalanan, durasiTabungan, jumlahYangSudahDitabung)
            jumlahYangPerluDitabung = tabungan.hitungTabungan()

            if jumlahYangPerluDitabung > 0:
                st.success(f"Anda perlu menabung {locale.currency(jumlahYangPerluDitabung, grouping=True, symbol=True)} {mataUangAnggaran} per bulan selama {durasiTabungan} bulan.")
            else:
                st.success("Tabungan anda sudah mencukupi.")
        else:
            st.error("Jumlah yang sudah ditabung lebih besar atau sama dengan anggaran perjalanan. Tidak perlu menabung lagi.")

elif select == 'Konsultasi Visa':
    st.subheader("Konsultasi melalui WhatsApp")
    whatsapp_button = st.button("Hubungi Kami di WhatsApp")
    
    if whatsapp_button:
        whatsapp_url = "https://wa.me/6285697679103" 
        st.markdown(f"Klik [di sini untuk chat WhatsApp]( {whatsapp_url} )", unsafe_allow_html=True)

    st.subheader("Download Panduan Visa")
    pdf_path = "file/panduan.pdf" 

    with open(pdf_path, "rb") as pdf_file:
        st.download_button(
            label="Unduh Panduan Visa", 
            data=pdf_file,              
            file_name="panduan_visa.pdf",  
            mime="application/pdf"    
        )

elif select == 'Tentang Kami':
    st.title("Tentang Kami")
    st.markdown("<hr>", unsafe_allow_html=True)
    
    st.markdown("""
        **ASEAN Travel Planner** adalah aplikasi yang dibuat oleh sekelompok mahasiswa Teknik Informatika untuk mempermudah perjalanan ke negara-negara ASEAN. 
        Aplikasi ini dirancang untuk membantu para wisatawan merencanakan perjalanan mereka dengan lebih mudah dan efisien.
    """, unsafe_allow_html=True)
    
    st.markdown("""
        **Visi Kami** adalah menciptakan aplikasi yang tidak hanya bermanfaat untuk para pelancong, tetapi juga untuk siapa saja yang membutuhkan informasi seputar perjalanan internasional, terutama ke negara-negara ASEAN. Kami berfokus untuk memberikan kemudahan dalam konversi mata uang, perhitungan anggaran, penghitung jarak antar negara ASEAN, serta perencanaan tabungan.
    """, unsafe_allow_html=True)

    st.markdown("<hr>", unsafe_allow_html=True)


    st.header("Our Team")
    team_members = [
        {"name": "Adinda Angesti Chandra", "nim": "0110224052", "photo": "images/dinda.JPG"},
        {"name": "Intan Ayu Lestari", "nim": "0110224118", "photo": "images/intan.jpeg"},
        {"name": "Muhamad Farhan Apriliansyah", "nim": "0110224069", "photo": "images/farhan.jpg"},
        {"name": "Ferdy Rahman", "nim": "0110224244", "photo": "images/ferdi.jpeg"}
    ]

    for member in team_members:
        col1, col2 = st.columns([1, 3])  
        with col1:
            st.image(member["photo"], width=100) 
        with col2:
            st.subheader(member["name"])  
            st.write(f"**Nim**: {member['nim']}")  

    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown("""
        Terima kasih telah mengunjungi halaman kami. Kami berharap aplikasi ini dapat membantu perjalanan Anda ke negara-negara ASEAN dengan lebih mudah dan menyenangkan!
    """)
