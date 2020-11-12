print("===================================================================")
print("                   SELAMAT DATANG DI GADGET STORE                  ")
print("===================================================================")

print("SPESIFIKASI HANDPHONE") 
handphone=[]

merk = input("merk HP : ") 
handphone.append(merk)

ram = int(input("RAM HP : ")) 
handphone.append(ram)

rom = int(input("Memory HP : ")) 
handphone.append(rom)

camera = int(input("Camera HP : ")) 
handphone.append(camera)

battery = int(input("Battery HP : ")) 
handphone.append(ram)

size = int(input("size HP : ")) 
handphone.append(size)

warna = input("warna HP : ")  
handphone.append(warna)

harga = float(input("harga HP : "))  
handphone.append(harga)

jumlah = int(input("jumlah HP yang di beli : ")) 
handphone.append(jumlah)

print("-------------------------------------------------------------------")

print("Merk HP adalah : ",merk, )
print("RAM HP adalah : ",ram, "GB" )
print("Memory HP adalah : ",rom, "GB" )
print("Camera HP adalah : ",camera, "Mega Pixels" )
print("Battery HP adalah : ",battery, "mAh" )
print("Size HP adalah : ",size, "inch")
print("Warna HP adalah : ",warna, )
print("Harga HP adalah : Rp.  ",harga, )
print("Jumlah HP yang dibeli : ",jumlah,"Unit")

print("-------------------------------------------------------------------")

print(handphone)

print("===================================================================")
print("            TERIMA KASIH TELAH BERBELANJA DI TOKO KAMI             ")
print("===================================================================")