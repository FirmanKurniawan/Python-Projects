w=1
while w<=10:
    
    #INPUT DATA MAHASISWA
    print ("\n-----PROGRAM PEMINJAMAN PERPUSTAKAAN-----")
    Nama = input("Masukan Nama                  : ")
    NPM = int(input("Masukan NPM                : "))
    a = int(input("Masukan tanggal pinjam       : "))
    b = int(input("Masukan tanggal pengembalian : "))
    x = b-a
    z = x-12
    denda = z*1500
    print ("-----------------------------------------")
    
    #OUTPUT DATA
    print ("Nama Peminjam   : ",Nama)
    print ("NPM Peminjam    : ",NPM)
    print ("Lama peminjaman : ",x)
    
    #PROSES LOGIKA
    if x<12:
        print ("Denda : Rp.0")
    elif x>12:
        print ("Denda : Rp.",denda)
    else:
        print ("Silahkan hitung kembali")
    w=w+1
    
    print ("\n---TERIMAKASIH SUDAH MENGEMBALIKAN BUKU---")
