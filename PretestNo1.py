print("===================================================================")
print("             SELAMAT DATANG DI PROGRAM KONVERSI SUHU               ")
print("===================================================================")

ulang = "y"
while ulang =="y":
  suhu_celcius =float(input("Masukan Nilai Suhu Celcius : "))
  suhu_celcius_ke_fahrenheit = (9./5)* suhu_celcius + 32
  suhu_celcius_ke_reamur = (4./5)* suhu_celcius
  suhu_celcius_ke_kelvin = suhu_celcius + 273.15
  print("\n")        

  print ("Hasil Nilai Konversi Suhu : ")
  print ("Suhu dalam Celcius    : %f" %(suhu_celcius))
  print ("Suhu dalam Fahrenheit : %2f" %(suhu_celcius_ke_fahrenheit))
  print ("Suhu dalam Reamur     : %f" %(suhu_celcius_ke_reamur))
  print ("Suhu dalam Kelvin     : %f" % (suhu_celcius_ke_kelvin))
  print("\n")

  ulang = input("Konversi Suhu lagi? y/t : ").lower()
  if (ulang == "t") :
    print("===================================================================")
    print("                    TERIMA KASIH TELAH BERKUNJUNG                  ")
    print("===================================================================")