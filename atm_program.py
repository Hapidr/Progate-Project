import random
import datetime
from customer import Customer

atm = Customer(id)

while True:
    id = int(input("Masukkan pin Anda: "))
    trial = 0
    while (id != int(atm.checkPin()) and trial < 3):
        id = int(input("Pin Anda salah. Silahkan masukkan lagi: "))
        trial += 1

        if trial == 3:
            print("Error silahkan ambil kartu dan coba lagi")
            exit()
    while True:
        print("selamat Datang!")
        print("\n 1 - Cek Saldo \n 2 - Debet \n 3 - Simpan \n 4 - Ganti Pin \n 5 - Keluar")
        menu_dipilih = int(input("\n Silahkan pilih menu: "))
        if menu_dipilih == 1:
            print("\n Jumlah saldo Anda sekarang adalah " + str(atm.checkBalance()) + "\n ")

        elif menu_dipilih == 2:
            nominal = float(input("Masukkan nominal Saldo: "))
            konfirmasi_withdraw = input("Konfirmasi Anda akan melakukan debet dengan nominal berikut? y/n " + str(nominal) + " ")
            if konfirmasi_withdraw == "y":
                print("Saldo awal Anda adalah: Rp. " + str(atm.checkBalance()) + " ")

            else:
                break

            if nominal < atm.checkBalance():
                atm.withdrawBalance(nominal)
                print("Transaksi debet berhasil")
                print("Saldo sisa sekarang: Rp. " + str(atm.checkBalance()) + " ")

            else:
                    print("Maaf Saldo Anda tidak cukup untuk melakukan debet")
                    print("Silahkan lakukan penambahan nominal saldo")

        elif menu_dipilih == 3:
            nominal = float(input("MAasukkan nominal saldo: "))
            konfirmasi_deposit = input("Konfirmasi Anda akan melakukan penyimpanan dengan nominal berikut? y/n" + str(nominal) + " ")

            if konfirmasi_deposit == "y":
                atm.depositBalance(nominal)
                print("Saldo Anda sekarang adalah: Rp." + str(atm.checkBalance()) + "\n")

            else:
                break


        elif menu_dipilih == 4:
            konfirmasi_pin = int(input("Masukkan pin Anda: "))

            while konfirmasi_pin != int(atm.checkPin()):
                print("Pin Anda salah, silahkan masukkan pin: ")

            pin_baru = int(input("Silahkan masukkan pin baru: "))
            print("Pin Anda berhasil diganti")

            konfirmasi_pin_baru = int(input("Coba masukkan pin baru: "))

            if konfirmasi_pin_baru == pin_baru:
                print('Pin baru Anda sukses!')

            else:
                print("Maaf Pin Anda salah")

        elif menu_dipilih == 5:
            print("Resi tercetak otomatis saat Anda keluar. \n Harap simpan tanda terima ini \n sebagai bukti transaksi Anda")
            print("No. Rekord: " + str(random.randint(100000, 1000000)))
            print("Tanggal: " + str(datetime.datetime.now()))
            print("Saldo akhir: " + str(atm.checkBalance()))
            print("Terima Kasih telah menggunakan ATM Progate!")
            exit()

        else:
            print("ERROR maaf menu tidak tersedia")



        



