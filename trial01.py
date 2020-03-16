print ("hy selamat datang di system saya")
print ("silahkan masukkan identitas anda")

nama = raw_input("masukkan nama anda: ")
umur = input("masukkan umur anda: ")

print "selamat datang",nama,"berusia",umur,"tahun"
print ("dalam system Kalkulator")

print (" --MENU KALKULATOR--")
print ("1.Penjumlahan")
print ("2.Pengurangan")
print ("3.Perkalian")
print ("4.Pembagian")

def penjumlahan():

  angka1 = input("masukkan angka ke-1: ")
  angka2 = input("masukkan angka ke-2: ")

  hasil = angka1 + angka2
  print "jawabannya adalah",hasil

def pengurangan():
  angka1 = input("masukkan angka ke-1: ")
  angka2 = input("masukkan angka ke-2: ")

  hasil = angka1 - angka2
  print "jawaban",hasil

def perkalian():
  angka1 = input("masukkan angka ke-1; ")
  angka2 = input("masukkan angka ke-2: ")

  hasil = angka1 * angka2
  print "jawabanya",hasil

def pembagian():
  angka1 = input("masukkan angka ke-1: ")
  angka2 = input("masukkan angka ke-2: ")

  hasil = angka1 / angka2
  print "jawabanya",hasil


menu = input("masukkan pilihan anda: ")

if menu == 1:
  penjumlahan()
elif menu == 2:
  pengurangan()
elif menu == 3:
  perkalian()
elif menu == 4:
  pembagian()

else:
  print ("menu tak di temukan")

 
