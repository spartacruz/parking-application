import hitung_parkir as hp
import rekap_data_parkir as rdp

def aplikasi_hitung_parkir():
    while True:
        
        trig = False
        print("\n--Hitung Biaya Parkir--")
        nomor_plat = input("Silahkan masukkan nomor plat kendaraan Anda (min 3 character): ").lower()
        if len(nomor_plat) >= 3:
            hp.hitung_biaya_parkir(nomor_plat)
            trig = True
        
        while trig:
            ulang_lagi = input("\nApakah ingin input biaya parkir lagi (y/n)? ")
            if ulang_lagi.lower() == "y" or ulang_lagi.lower() == "n":
                trig = False
        

        if len(nomor_plat) >= 3 and ulang_lagi.lower() == "n":
            break
    print("\nKembali ke menu utama....\n")
    pilih_menu()

def aplikasi_rekap_data_parkir(): 
    while True:
        print("\n--Rekap Data Parkir--")
        print("1. Total Pengunjung (Berdasarkan Struk Parkir)")
        print("2. Daftar Peserta Member")
        print("3. Statistik Data Parkir")
        print("4. Kembali ke Menu Utama")
        check_input = input("Silahkan pilih menu berikut (1 - 4): ")

        if check_input.isdigit():
            if check_input == "1":
                print("\n")
                rdp.present_data(1)
                print("\n")
                input("Tekan Enter Untuk Melanjutkan...")
            elif check_input == "2":
                print("\n")
                rdp.present_data(2)
                print("\n")
                input("Tekan Enter Untuk Melanjutkan...")
            elif check_input == "3":
                print("\n")
                rdp.present_data(3)
                print("\n")
                input("Tekan Enter Untuk Melanjutkan...")
            elif check_input == "4":
                break
            else:
                pass

    print("\nKembali ke menu utama....\n")
    pilih_menu()


def pilih_menu():
    print("------Aplikasi Parkir Paramadina------\n")
    print("1. Input Parkir Masuk")
    print("2. Rekap Data Parkir")
    # print("3. Keluar / Exit Program")
    
    while True: 
        check_input = input("Silahkan pilih menu berikut (1 - 2): ")

        if check_input.isdigit():
            if check_input == "1":
                aplikasi_hitung_parkir()
            elif check_input == "2":
                aplikasi_rekap_data_parkir()
            # elif check_input == "3":
            #     break
    
    print("\nProgram Selesai...")
    print("Yuri Iskandia - Copyright 2020")

pilih_menu()
