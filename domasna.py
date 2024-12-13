# 1

# vnesen_broj = int(input("Vnesi broj: "))
# if vnesen_broj % 2 == 0:
#     print(f"Vneseniot broj {vnesen_broj} e paren broj")
# else:
#     print(f"Vneseniot broj {vnesen_broj} e neparen broj")
#
# print(vnesen_broj)



# 2


# vnesen_broj = int(input("Vnesi broj: "))
# if vnesen_broj >= 1000:
#     print("preterano pozitiven")
# elif vnesen_broj > 99 and vnesen_broj < 999:
#     print("mnogu pozitiven")
# elif vnesen_broj > 0 and vnesen_broj < 100:
#     print("pozitiven")
# elif vnesen_broj == 0:
#     print("nula")
# elif vnesen_broj < 0 and vnesen_broj > -100:
#     print("negativen")
# elif vnesen_broj < -100 and vnesen_broj > -1000:
#     print("mnogu negativen")
# elif vnesen_broj <= -1000:
#     print("preterano negativen")
# else: print("brojot e nadvor od rangot")



# 3

# vnesi_poeni = int(input("Vnesi gi poenite: "))
# if vnesi_poeni >= 0 and vnesi_poeni < 61:
#     print("Ocenka 1")
# elif vnesi_poeni > 60 and vnesi_poeni < 71:
#     print("Ocenka 2")
# elif vnesi_poeni > 70 and vnesi_poeni < 81:
#     print("Ocenka 3")
# elif vnesi_poeni > 80 and vnesi_poeni < 91:
#     print("Ocenka 4")
# elif vnesi_poeni > 90 and vnesi_poeni < 101:
#     print("Ocenka 5")
# else:
#     print("Greska pri vnesuvanje poeni")




# 4


# prv_broj = int(input("vnesi cel broj: "))
# operacija = input("vnesi ednostavna matematicka operacia (+, -, *, / : ")
# vtor_broj = int(input("vnesi vtor broj: "))
#
# if operacija == "+":
#     rezultat = prv_broj + vtor_broj
# elif operacija == "-":
#     rezultat = prv_broj - vtor_broj
# elif operacija == "*":
#     rezultat = prv_broj * vtor_broj
# elif operacija == "/":
#     if vtor_broj != 0:
#         rezultat = prv_broj / vtor_broj
#     else:
#         rezultat = "Delenje so 0 e nevozmozno"
# else:
#     rezultat = "nevazecka operacija"
# print(f"Rezultatot iznesuva:  {rezultat}")



# 5

#       1 nacin

# broj_na_mesec = int(input("vnesi go brojot na mesecot(1-12): "))
# meseci = {1:31, 2:28/29, 3:31, 4:30, 5:31, 6:30, 7:31, 8:30, 9:30, 10:31, 11:30, 12:31}
# if broj_na_mesec > 0 and broj_na_mesec < 12 :
#     print(f"{broj_na_mesec} mecec ima {meseci[broj_na_mesec]}")
# else:
#     print(f"{broj_na_mesec} ne postoi, vnesete pomegu 1-12")


#     2 nacin

# broj_na_mesec = int(input("vnesi go brojot na mesecot(1-12): "))
# if broj_na_mesec > 0 and broj_na_mesec < 12:
#    if (broj_na_mesec == 1
#       or broj_na_mesec == 3
#       or broj_na_mesec == 5
#       or broj_na_mesec == 7
#       or broj_na_mesec == 9
#       or broj_na_mesec == 11):
#          print(f"{broj_na_mesec} mesec ima 30 denovi")
#    elif broj_na_mesec == 2:
#          print(f"{broj_na_mesec} ima 28/29 denovi")
#    else: print(f"{broj_na_mesec} mesec ima 31 denovi")
# else:
#     print(f"{broj_na_mesec} mecec ne postoi, vnesete pomegu 1 - 12")



# 6

# 1 nacin

# broj_na_den = int(input("vnesi broj na den(1-7)"))
# denovi = {1: "Ponedelnik", 2: "Vtornik", 3: "Sreda", 4: "Cetvrtok", 5: "Petok", 6: "Sabota", 7: "Nedela"}
# if broj_na_den > 0 and broj_na_den < 8:
#     print(f"{denovi[broj_na_den]}")
# else:
#     print(f"{broj_na_den} ne postoi, vnesete od 1-7")


#     2 nacin

# broj_na_den = int(input("vnesi broj na den(1-7)"))
# if broj_na_den > 0 and broj_na_den < 8:
#     if broj_na_den == 1:
#         print("Ponedelnik")
#     elif broj_na_den == 2:
#         print("Vtornik")
#     elif broj_na_den == 3:
#         print("Sreda")
#     elif broj_na_den == 4:
#         print("Cetvrtok")
#     elif broj_na_den == 5:
#         print("Petok")
#     elif broj_na_den == 6:
#         print("Sabota")
#     elif broj_na_den == 7:
#         print("Nedela")
# else : print(f"{broj_na_den} ne postoi, vnesete od 1-7")




# 7

# ime_na_ucenik = input("vnesi go imeto na ucenikot: ")
# ocenki = []
# predmeti = ["matematika", "makedonski", "geografija", "istorija", "informatika"]
# for predmet in predmeti :
#     ocenka = int(input(f"Vnesi ocenka za {predmet}: "))
#     ocenki.append(ocenka)
# vkupen_zbir_na_ocenki = sum(ocenki)
# prosecna_ocenka = vkupen_zbir_na_ocenki / len(ocenki)
#
# if prosecna_ocenka >= 4.5:
#     prosek = "odlicen"
# elif prosecna_ocenka >= 3.5:
#     prosek = "mnogu dobar"
# elif prosecna_ocenka >= 2.5:
#     prosek = "dobar"
# elif prosecna_ocenka >= 1.5:
#     prosek = "dovolen"
# else: prosek = "nedovolen"
#
# print(f"Ime na ucenik: {ime_na_ucenik}")
# for predmet, ocenka in zip(predmeti, ocenki):
#     print(f"Ocenka po {predmet}: {ocenka}")
# print(f"Vkupen zbir: {vkupen_zbir_na_ocenki}")
# print(f"Prosecna ocenka: {prosecna_ocenka}")
# print(f"Uvenikot e {prosek}")




# 9

# godina = int(input("Vnesete godina: "))
# if godina % 4 ==0 or (godina % 100 == 0 and godina % 400 == 0):
#     print(f"{godina} e prestapna godina")
# else:
#     print(f"{godina} ne e prestapna godina")



# 10

# import datetime
# today = datetime.date.today()
# year = today.year
# godina_na_raganje = int(input("Vnesete ja vasata godina na raganje: "))
# if year - godina_na_raganje >= 18 :
#     print("Korisnikot ima pravo na licna karta")
# else:
#     print("Potrebna e soglasnost od roditel: da/ne")




# 12

# karakter = input("Vnesete bilo kakov karakter: ")
# if len(karakter) != 1:
#     print("Vnesete karakter: ")
# elif karakter.isalpha():
#     print(f"Vneseniot karakter {karakter} e bukva")
# elif karakter.isnumeric():
#     print(f"Vneseniot karakter {karakter} e broj")
# else:
#     print(f"Vneseniot karakter {karakter} e specijalen znak")





# 13

# triagolnik = ["agol1", "agol2", "agol3"]
# agli = []
# for agol in triagolnik:
#     agol = int(input("Vnesi go stepenot na agolot: "))
#     agli.append(agol)
# vkupen_zbir_na_alli = sum(agli)
# if vkupen_zbir_na_alli == 180:
#     print("Od vnesenite stepeni na agli moze da se formira triagolnik")
# else:
#     print("Od vnesenite stepeni na agli ne moze da se formira triagolnik")




# 14

# ceni_na_letovi = {
# "Dortmund": 4480,
# "Frankfurt": 7128,
# "Budapest": 2595,
# "Berlin": 8910,
# "Paris": 3537,
# "Venice": 2668,
# "London": 2595,
# "Milan": 2595,
# "Rome": 5658,
# "Malta": 5578
# }
# grad = input("Vnesi go gradot: ").capitalize()
# if grad in ceni_na_letovi:
#     print(f"{ceni_na_letovi[grad]}")
# else:
#     ceni_na_letovi[grad] = "ne postoi"
#     print(f"Nema cena za {grad}")



# 15
# broevi = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
# broevi = ["1"]
# bukvi = ["a", "b", "v"]
# bukvi = ["a", "b"]
# merged_list = list(set(broevi + bukvi))
# merged_list.sort()
#
# if len(merged_list) < 4 :
#     merged_list.extend([0] * (4 - len(merged_list)))
#
# merged_list = merged_list[:10]
# print(merged_list)





