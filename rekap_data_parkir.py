master_dir = "C:\\Users\\Asus\\Desktop\\Kumpulan Tugas\\Semester 1\\Sesi 2\\Alprog 1 (Python)\\uas\\"

# f = open(master_dir + "data_member.txt", 'r+', encoding='utf-8').read()
# data_member = eval(f)

#rekapan parkir masuk
data_rekap = {}
try:
    #membaca data awal - bentuk data dictionary
    f = open(master_dir + "data_rekap_parkir.txt", 'r+', encoding='utf-8').read()
    data_rekap = eval(f)
except SyntaxError: #jika file kosong, maka akan diinisialisasi sebagai dictionary kosong
    data_rekap = {}

#list member anggota
data_member = {} 
try:
    #membaca data awal - bentuk data dictionary
    f = open(master_dir + "data_member.txt", 'r+', encoding='utf-8').read()
    data_member = eval(f)
except SyntaxError: #jika file kosong, maka akan diinisialisasi sebagai dictionary kosong
    data_member = {}

#input data ke text
def insert_data_parkir(plat_nomor, membership, jenis_kd, merk_kd, model_kd, lama_pkr, biaya_pkr = 0):
    
    #generate dan checking kode struk
    for i in range(1, 1000): 
        urutan = f"{i:04}" 
        kode_struk = "PKR-" + str(urutan)

        if str(data_rekap.get(kode_struk)).lower() == "none":
            break #selesai. ga generate kode lagi

    data_rekap.update({
    kode_struk: {
	    'plat_nomor': plat_nomor, 
	    'jenis_keanggotaan': membership,
	    'jenis_kendaraan': jenis_kd, 
	    'merk_kend': merk_kd,
        'model_kend': model_kd,
        'lama_parkir' : lama_pkr,
        'biaya_parkir' : biaya_pkr,
	}})

    #menulis data pengunjung ke txt dalam bentuk dictionary
    with open(master_dir + 'data_rekap_parkir.txt', 'w+') as file: 
        file.write(str(data_rekap)) 

#generate list seluruh pengunjung 
def list_pengunjung_parkir(): 
    for nostruk_db, info_struk_db  in data_rekap.items():
        print(nostruk_db + " " + str(data_rekap[nostruk_db]['plat_nomor']) + " " + str(data_rekap[nostruk_db]['jenis_keanggotaan'])+ \
            " " + str(data_rekap[nostruk_db]['jenis_kendaraan']) + " " + str(data_rekap[nostruk_db]['biaya_parkir']))

#total pengunjung berdasarkan struk parkir
def total_pengunjung_parkir(): 
    return (len(data_rekap))

#jumlah pesereta member
def total_member(): 
    return (len(data_member))

#total pendapatan parkir masuk (Non-member)
def income_parkir_masuk_non_member(): 
    hitung = 0
    for nostruk_db, info_struk_db  in data_rekap.items():
        hitung = hitung + data_rekap[nostruk_db]['biaya_parkir']
    return hitung

#total pendapatan parkir masuk (member - bulanan)
def income_parkir_masuk_member(): 
    jumlah = 0
    for nomor_plat, no_plat_info  in data_member.items():
        iterate = data_member[nomor_plat]['jenis_kendaraan']

        if iterate == "motor":
            jumlah = jumlah + 150000
        else:
            jumlah = jumlah + 500000

    return jumlah

#jumlah pengunjung berdasarkan jenis kendaraaan - output dictionary
def pengunjung_jenis_kend():
    pengunjung_jenis_kend = {}
    jumlah_motor = 0
    jumlah_mobil = 0

    for nostruk_db, info_struk_db  in data_rekap.items():
        iterate = data_rekap[nostruk_db]['jenis_kendaraan']

        if iterate == "motor":
            jumlah_motor = jumlah_motor + 1
        else:
            jumlah_mobil = jumlah_mobil + 1

    pengunjung_jenis_kend.update({'jumlah_motor': jumlah_motor,'jumlah_mobil': jumlah_mobil})

    return pengunjung_jenis_kend #return dictionary {'jumlah_motor': jumlah_motor,'jumlah_mobil': jumlah_mobil}

#generate list seluruh peserta member
def list_peserta_member(): 
    for noplat_db, info_plat_db  in data_member.items(): #iterate dict untuk cari plat itu ada atau tidak.
        print(noplat_db + " - " + str(data_member[noplat_db]['nama']).title() + " - " + str(data_member[noplat_db]['jenis_kendaraan']).title()+ \
            " - " + str(data_member[noplat_db]['merk']) + " - " + str(data_member[noplat_db]['model']))

def avg_menit_parkir():
    hitung = 0
    avg_hitung = 0
    for nostruk_db, info_struk_db  in data_rekap.items():
        hitung = int(hitung) + int(data_rekap[nostruk_db]['lama_parkir'])
    orang = len(data_rekap)

    avg_hitung = hitung / orang
    avg_hitung = '%.1f'%(avg_hitung) #pembulatan 1 desimal belakang koma

    return avg_hitung

def present_data(pilihan):
    if pilihan == 1:
        print("--Daftar Pengunjung Parkir--")
        #list pengunjung berdasarkan struk parkir & jumlahnya
        list_pengunjung_parkir()
        print("\nTotal Pengunjung Parkir: " + str(total_pengunjung_parkir()) + " " + "Struk")
    
    elif pilihan == 2:
        print("--Daftar Peserta Member--")
        #list member yang tergabung & jumlahnya
        list_peserta_member()
        print("\nTotal Peserta Member Parkir: " + str(total_member()) + " " + "Orang")
    
    else:
    #statistik data parkir

        print("--Statistik Data Parkir--")
        #total pendapatan parkir masuk (non-member)
        print("Total Pendapatan Parkir Masuk (non-member): Rp " + f'{income_parkir_masuk_non_member():,}' + ",-")

        #total pendapatan parkir masuk (member - bulanan)
        print("Total Pendapatan Parkir Masuk (member - bulanan): Rp " + f'{income_parkir_masuk_member():,}' + ",-")
        
        #total pengunjung berdasarkan jenis kendaraan
        data_jenis = pengunjung_jenis_kend()
        print("Total Pengunjung berdasarkan Jenis Kendaraan >>> " + str(data_jenis['jumlah_mobil']) + " Mobil & " + str(data_jenis['jumlah_motor']) + " Motor")

        #rata rata menit parkir
        print("Rata-Rata Durasi Pengunjung Parkir: " + avg_menit_parkir() + " Menit")


def development():
    pass

    # def daftar_member_baru(plat_nomor, nama ,jenis_kd, merk_kd, model_kd):
    # data_member.update({
    # plat_nomor.lower(): {
    #     'nama': nama, 
    #     'jenis_kendaraan': jenis_kd, 
    #     'merk': merk_kd,
    #     'model': model_kd,
    # }})

    # #menulis data pengunjung ke txt dalam bentuk dictionary
    # with open(master_dir + 'data_member.txt', 'w+') as file: 
    #     file.write(str(data_member)) 

    # def check_daftar_member_baru(plat_nomor):
    
    # if str(data_member.get(plat_nomor)).lower() == "none": #jika plat nomor tsb belum didaftarkan..
    #     belum_ada = True
    # else:
    #     belum_ada = False
    
    # return belum_ada

    # def olah_member_baru():
    #     while True:
    #         plat_nomor = input("Silahkan masukkan plat nomor Anda (min 3 char): ")

    #         if len(plat_nomor) > 3: #kalo input lebih dari 3 char
    #             if check_daftar_member_baru(plat_nomor) == True: #jika bisa didaftarkan
                    
    #                 daftar = True #lanjut ke sesi berikutnya
    #                 break #keluar loop while plat nomor

    #             else: #duplikat. tidak bisa di daftarkan
    #                 print("\nMaaf! Plat nomor tersebut sudah terdaftar pada sistem kami")

    #                 while True:
    #                     check = input("Apakah Anda ingin mendaftarkan plat nomor lain (y/n)? ")
    #                     if check.lower() == "y" or check.lower() == "n":
    #                         if check.lower() == "y": #user kekeh mau daftar
    #                             break #keluar loop check, masuk loop while plat nomor

    #                         else: #user nyerah - gamau daftar lagi

    #                             daftar = False #trigger untuk skip pendaftaran selanjutnya
    #                             break #keluar loop check, masuk loop while plat nomor

    #         else: #kalo input kurang dari 3 char
    #             daftar = True
    #             pass #loop while plat nomor
            
    #         if daftar == False: #kalo user nyerah
    #             break #keluar loop while plat nomor
        
    #     if daftar == True: #user mau lanjutin pendafataran
    #         while True:
    #             nama_member = input("Silahkan masukkan nama Anda (min 3 char): ")
    #             if len(nama_member) >= 3:
    #                 break
            
    #         while True:
    #             jenis_kend = input("\nSilahkan masukkan jenis kendaraan Anda (mobil/motor): ")
    #             if jenis_kend.lower() == "mobil" or jenis_kend.lower() == "motor":
    #                 break
            
    #         while True:
    #             merk_kend = input("\nSilahkan masukkan merk kendaraan Anda (cth: Toyota): ")
    #             if len(merk_kend) > 2:
    #                 break

    #         while True:  
    #             model_kend = input("\nSilahkan masukkan model kendaraan Anda (cth: Avanza Veloz): ")
    #             if len(model_kend) > 3:
    #                 break
            
    #         print("\nData yang Anda masukkan: ")
    #         print("No Plat: " + plat_nomor)
    #         print("Nama: " + nama_member)
    #         print("Jenis Kendaraan: " + jenis_kend)
    #         print("Merk Kendaraan: " + merk_kend)
    #         print("Model Kendaraan: " + model_kend + "\n")

    #         while True:
    #             check = input("Apakah data diatas sudah benar (y/n) ? ")
    #             if check.lower() == "y" or check.lower() == "n":
    #                 if check.lower() == "y":
    #                     print("\nme-register ke database...")
    #                     #rdp.daftar_member_baru(plat_nomor, nama_member, jenis_kend, merk_kend, model_kend)
                        
    #                     print("Sukses! Anda telah terdaftar sebagai member parkir kami!")

    #                     print("\nKembali ke menu utama")
    #                     uas_master.pilih_menu()
    #                     break
    #                 else:
    #                     break

    #     else: #user mau batalin pendaftaran
    #         uas_master.pilih_menu()

    # olah_member_baru()