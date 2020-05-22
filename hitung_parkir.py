import rekap_data_parkir as rekap

master_dir = "C:\\Users\\Asus\\Desktop\\Kumpulan Tugas\\Semester 1\\Sesi 2\\Alprog 1 (Python)\\uas\\"

f = open(master_dir + "data_member.txt", 'r+', encoding='utf-8').read()
data_member = eval(f)

def hitung_biaya_parkir(nomor_plat):
    member_parkir = False
    for noplat_db, info_plat_db  in data_member.items(): #iterate dict untuk cari plat itu ada atau tidak.
        if noplat_db == nomor_plat:
            member_parkir = True    #terdaftar pada member
            break

    if member_parkir == False: #jika BUKAN peserta member parkir
        parkir_non_member(nomor_plat)

    else: #jika member parkir
        parkir_member(nomor_plat)

############################################################################################

def parkir_non_member(nomor_plat):
    while True:
        jenis_kend = input("Silahkan masukkan jenis kendaraan Anda (motor/mobil): ")

        jenis_kend = jenis_kend.lower()
        if jenis_kend == "motor" or jenis_kend == "mobil":
            break
    
    while True:
        merk_kendaraan = input("Merk kendaraan Anda (cth: Kawasaki): ")
        if merk_kendaraan.isdigit() == False:
            break

    while True:
        model_kendaraan = input("Nama Tipe / Model Kendaraan Anda (cth: Ninja 250r): ")
        if model_kendaraan.isdigit() == False:
            break
    
    while True:
        lama_parkir = input("Lama waktu parkir Anda (dalam menit): ")
        if lama_parkir.isdigit():
            lama_parkir = int(lama_parkir)
            break
    
    biaya_parkir = perhitungan_biaya_parkir(jenis_kend, lama_parkir)
    

    biaya_parkir = int(biaya_parkir) #menghilangkan desimal
    print("Biaya parkir Anda: " + str(biaya_parkir))
    rekap.insert_data_parkir(plat_nomor=nomor_plat.lower(), membership='non-member', jenis_kd=jenis_kend.lower(), merk_kd=merk_kendaraan.lower(),\
        model_kd=model_kendaraan.lower(), lama_pkr=lama_parkir, biaya_pkr=biaya_parkir)

def perhitungan_biaya_parkir(jenis_kend, lama_parkir):
    if jenis_kend == "mobil":
        based_price = 7000 #biaya perjam
    else:
        based_price = 3000
    
    selisih_menit = 0
    if lama_parkir >= 60: #lama parkir lebih atau sama dengan sejam
        selisih_menit = lama_parkir % 60 #mencari selisih parkir untuk diroundup
        lama_parkir = lama_parkir - selisih_menit

        biaya_parkir = (lama_parkir / 60) * based_price
    else: #jika parkir belum sejam
        biaya_parkir = based_price #round up ke tarif sejam

    if selisih_menit > 0: #sisa menit parkir yang belum sejam dibulatkan keroundup
        biaya_parkir = biaya_parkir + based_price
    
    return biaya_parkir

############################################################################################

def parkir_member(nomor_plat):
    while True:
        lama_parkir = input("Lama waktu parkir Anda (dalam menit): ")
        if lama_parkir.isdigit():
            lama_parkir = int(lama_parkir)
            break

    nama_pemilik = str(data_member[nomor_plat]['nama']).title()
    jenis_kend = str(data_member[nomor_plat]['jenis_kendaraan']).upper()
    merk_kend = str(data_member[nomor_plat]['merk']).title()
    model_kend = str(data_member[nomor_plat]['model']).title()

    print("\nSelamat datang " + nama_pemilik + "! Anda tergabung sebagai member parkir kami dengan detail: \
        \nJenis Kendaraan: " + jenis_kend + "\nModel Kendaraan: " + merk_kend + " " + model_kend)
    print("Lama parkir Anda: " + str(lama_parkir) + " Menit")

    basedprice = 0
    if jenis_kend.lower() == "motor":  # memilah tarif berdasarkan jenis kendaraan
        basedprice = 150000
    else:  # jika mobil
        basedprice = 500000

    print("Tarif parkir bulanan anda Rp " + f'{basedprice:,}' + ",-")
    rekap.insert_data_parkir(plat_nomor=nomor_plat.lower(), membership='member', jenis_kd=jenis_kend.lower(), merk_kd=merk_kend.lower(),\
        model_kd=model_kend.lower(), lama_pkr=lama_parkir)