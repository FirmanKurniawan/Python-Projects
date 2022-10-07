from bank import Bank

bank = Bank()

print("=======================> [ATM Machine] <===========================")
print("1. Buat akun")
print("2. Cek saldo")
print("3. Tarik tunai")

while True:
    userInput = int(input("Masukkan nomor yang ingin dimasukkan: "))

    if userInput == 1:
        nama = str(input("Masukkan nama Anda: "))
        pin = int(input("Masukkan nomor pin yang Anda inginkan: "))

        if len(str(pin)) != 6:
            print("Nomor pin harus 6 digit!")
            pin = int(input("Masukkan nomor pin yang Anda inginkan: "))
            continue

        rekening = bank.buatAkun(nama, pin)
        print("Akun berhasil dibuat dengan data berikut:")
        print(f"Nama            : {nama}")
        print(f"No. Rekening    : {rekening}")
        continue
    elif userInput == 2:
        rekening = int(input("Masukkan nomor rekening Anda: "))

        if bank.cekRekening(rekening) == False:
            print("No. Rekening yang Anda masukkan salah!")
            rekening = int(input("Masukkan nomor rekening Anda: "))
            continue

        pin = int(input("Masukkan nomor pin Anda: "))

        if bank.cekPin(pin) == False:
            print("Pin yang Anda masukkan salah!")
            pin = int(input("Masukkan nomor pin Anda: "))
            continue

        saldo = bank.cekSaldo(rekening)
        print("Saldo pada rekening Anda sebesar:")
        print(f"          Rp. {saldo}")
        continue
    elif userInput == 3:
        rekening = int(input("Masukkan nomor rekening Anda: "))

        if bank.cekRekening(rekening) == False:
            print("No. Rekening yang Anda masukkan salah!")
            rekening = int(input("Masukkan nomor rekening Anda: "))
            continue

        pin = int(input("Masukkan nomor pin Anda: "))

        if bank.cekPin(pin) == False:
            print("Pin yang Anda masukkan salah!")
            pin = int(input("Masukkan nomor pin Anda: "))
            continue

        jumlah = int(input("Masukkan jumlah uang yang ingin Anda tarik: "))
        saldo = bank.cekSaldo(rekening)

        if saldo < jumlah:
            print("Saldo pada rekening Anda tidak cukup!")
            continue

        saldoAkhir = bank.kurangiSaldo(rekening, jumlah)
        print(f"Anda berhasil tarik tunai sebesar: Rp. {jumlah}")
        print(f"Sisa saldo Anda adalah sebesar: Rp. {saldoAkhir}")
        continue
    else:
        print("Angka yang dimasukkan salah!")

