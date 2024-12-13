# recenica = "ova e recenica koja sodrzi brojka (6) i specijalen znak (%)"
# print("recenica_upper", recenica.upper())
# print("recenica_lower", recenica.lower())
# print("recenica_capitalize", recenica.capitalize())
# print("recenica_swapcase", recenica.swapcase())
# print("recenica_title", recenica.title())
# print("recenica_count", recenica.count("a"))
# print("recenica_endswith", recenica.endswith("s"))
# print("recenica_find", recenica.find("o"))
# print("recenica_index", recenica.index("a"))
# print("recenica_isalpha", recenica.isalpha())
# print("recenica_isdecimal", recenica.isdecimal())
# print("recenica_isdigit", recenica.isdigit())
# print("recenica_islower", recenica.islower())
# print("recenica_replace", recenica.replace("recenica", "slozena recenica"))
# print("recenica_isupper", recenica.isupper())
# print("recenica_strip", recenica.strip("ova e"))
# print("recenica_split", recenica.split("koja"))
from math import factorial
from turtledemo.paint import switchupdown


# broj  = 0
# while broj < 6:
#     broj += 1
#     if broj == 3:
#         continue
#     print(broj)

# i = 0
# word = "Hello"
# while i < len(word):
#     if word[i] == "e" or word[i] == "o":
#         i += 1
#         continue
#     print(f"bukvi {word[i]}")
#     i += 1



# Domasni vezbi od ciklusi

# 1

# lista_broevi = []
#
# while True:
#     a = input("Vnesi go prviot broj: ")
#     b = input("Vnesi go vtoriot broj: ")
#     c = input("Vnesi go delitelot: ")
#
#     if a.isnumeric() and b.isnumeric() and c.isnumeric():
#         a = int(a)
#         b = int(b)
#         c = int(c)
#         brojac = 0
#         pomal_broj = min(a, b)
#         pogolem_broj = max(a, b)
#
#         for x in range(pomal_broj, pogolem_broj + 1):
#             if x == 0:
#                 continue
#
#             if x % c == 0:
#                 brojac = brojac + 1
#                 lista_broevi.append(x)
#                 # brojac += 1
#
#         print(f"broevi dellivi so brojot {c} vo rangot od {pomal_broj} do {pogolem_broj} iznesuva {brojac}")
#         print(f"Tie broevi se: {lista_broevi}")
#         lista_broevi.clear()
#     else:
#         print("Vnesovte nevaliden vlez")
#
#     prodolzuva = input("Dali sakas da napravis nova proverka Da/Ne: ").upper().strip()
#
#     if prodolzuva != "DA":
#         break
#
# print("END")


# 2


# broj = 15
# fact = 1
# for num in range(1, broj+1):
#     fact = fact * num
# print(fact)




# 3

# broj = 30
# for br in range(1, broj+1):
#     if br > 1:
#         for i in range(2, br):
#             if br % i == 0:
#                 break
#             else:
#                 print(br)



# 4

# broj = int(input("Vnesete broj: "))
# for br in range(1, broj+1):
#     for i in range(1, br+1):
#          print(i, end='')
#     print()


# 5

# broj = int(input("Vnesete broj: "))
# for br in range(broj, 0, -1):
#     print((br))

# 6

# m = int(input("Vnesete broj: "))
# n = int(input("Vnesete broj: "))
#
# for br in range(m, n+1):
#     if br % 2 == 0:
#        print(br)



# 8

# n = int(input("Vnesete broj: "))
# for broj in range(1, n+1):
#     if broj % 3 == 0 and broj % 5 == 0:
#         print("TriPet")
#     elif broj % 5 == 0:
#         print("Pet")
#     elif broj % 3 == 0:
#         print("Tri")
#     else:
#         print(broj)



# 9

# lines=["aBcccbB" , "Ova e linija 2.", "Ova e TreTa linija."]
# for word in lines:
#     print(word.lower())


# 10
#  so funkcija

# string = input("Napisi nekoj string: ")
# def brojac (string):
#     bukvi = 0
#     broevi = 0
#     for karakter in string:
#         if karakter.isalpha():
#                bukvi += 1
#         elif karakter.isnumeric():
#                broevi += 1
#     print(f"bukvi: {bukvi}")
#     print(f"broevi: {broevi}")
# brojac(string)



# string = input("Napisi nekoj string: ")
# print(string)
# bukvi = 0
# broevi = 0
# for karakter in string:
#     if karakter.isalpha():
#            bukvi += 1
#     elif karakter.isnumeric():
#            broevi += 1
# print(bukvi)
# print(broevi)


# 11

# broj = int(input("vnesete broj: "))
# for br in range(1, 11):
#     print(f"{broj} * {br} = {broj*br}")


# 12

# for broj in range(1, 21):
#     print(broj*broj)

# 13

# string = input("Napisi string: ")
# for i in range(len(string)):
#    if i % 2 == 0:
#       print(string[i], end="")

# 13.1
# string = input("Napisi string: ")
# print("neparni: ")
# for i in range(len(string)):
#    if i % 2 == 0:
#      print(string[i], end="")
# print("\nParni: ")
# for i in range(len(string)):
#    if i % 2 != 0:
#      print(string[i], end="")

# 14

# recenica = "Ivan ima 25 godini. Ivan raboti kako Python Developer. Programiranje so Python ima naucheno na kurs vo Semos edukacija. Ivan mnogu si ja saka rabotata."
# zbor = input("Vnesi zbor: ")
# broj_na_povtoruvanja = recenica.split().count(zbor)
# print(f"Zborot {zbor} se povtoruva {broj_na_povtoruvanja} pati")

# 15




# 16
# so funkcija
# broj = int(input("vnesi broj: "))
# def brojac_na_cifri (broj):
#    print(len(str(broj)))
# brojac_na_cifri(broj)


# broj = int(input("vnesi broj: "))
# print(len(str(broj)))


# 17

# 18

# 19
# so funkcija

# broj = int(input("vnesi broj: "))
# def zbir_na_cifri (broj):
#     zbir = 0
#     for cifra in str(broj):
#         zbir += int(cifra)
#     print(zbir)
# zbir_na_cifri(broj)



# broj = int(input("vnesi broj: "))
# zbir = 0
# for broevi in str(broj):
#     zbir += int(broevi)
# print(zbir)

# 20
# broj = int(input("vnesi broj: "))
# blag_broj = []
# for blagi_broevi in str(broj):
#     if int(blagi_broevi) % 2 == 0 or int(blagi_broevi) == 0:
#         blag_broj.append(blagi_broevi)
# for br in range(len(blag_broj)):
#     blag_broj[br] = int(blag_broj[br])
# najmal = sorted(blag_broj)
# print(blag_broj)
# print(najmal)
# print(najmal[0])
# if najmal:
#     print(najmal[0])
# else:
#     print("Ne")





# domasna - produkti za kupuvanje

# produkti = ["leb", "sok", "brasno", "zejtin", "domaten sos"]
# kupeni_produkti = []
# nekupeni_produkti = produkti.copy()
# while True:
#     produkt = input("Vnesi KRAJ za kraj ili vnesi go produktot: ").strip().lower()
#     if produkt == "kraj":
#         break
#     else:
#         if produkt in produkti:
#             if produkt not in kupeni_produkti:
#                 kupeni_produkti.append(produkt)
#                 nekupeni_produkti.remove(produkt)
#         else:
#                 kupeni_produkti.append(produkt + ' ' + "*")
#                 kupeni_produkti = list(dict.fromkeys(kupeni_produkti))
#     f = open("nekupeni_produkti.txt", "w")
#     f.write("Nekupeni proizvodi\n\n")
#     for nekupen_proizvod in nekupeni_produkti:
#         f.write(f"{nekupeni_produkti.index(nekupen_proizvod) + 1}. {nekupen_proizvod}\n")
#
#     f = open("kupeni_produkti.txt", "w")
#     f.write("Kupeni proizvodi\n\n")
#     for kupen_proizvod in kupeni_produkti:
#         f.write(f"{kupeni_produkti.index(kupen_proizvod) + 1}. {kupen_proizvod}\n")
#
#     print(f"Produkti {produkti}")
#     print(f"Kupeni produkti: {kupeni_produkti}")
#     print(f"Nekupeni produkti: {nekupeni_produkti}")
#
# print("KRAJ")



#  kalkulator
#
# prv_broj = input("vnesi go prviot broj: ")
# operator = input("vnesi go operatorot: +,-,/,*")
# vtor_broj = input("vnesi go vtoriot broj: ")
#
# def kalkulator (prv_broj, operator, vtor_broj):
#     try:
#         if operator == "+":
#             rezultat = int(prv_broj) + int(vtor_broj)
#         elif operator == "-":
#             rezultat = int(prv_broj) - int(vtor_broj)
#         elif operator == "*":
#             rezultat = int(prv_broj) * int(vtor_broj)
#         elif operator == "/":
#             rezultat = int(prv_broj) / int(vtor_broj)
#
#     except ZeroDivisionError:
#         print("se obiduvate da delite so nula")
#     except ValueError:
#         print("nevalidni vrednosti ili operatori")
#     else:
#         return rezultat
#
#
# rezultat = kalkulator(prv_broj, operator, vtor_broj)
# print(f"{prv_broj}{operator}{vtor_broj}={rezultat}")


#  drug nacin

# def kalkulator (prv_broj, operator, vtor_broj):
#     try:
#         if operator == "+":
#             rezultat = int(prv_broj) + int(vtor_broj)
#         elif operator == "-":
#             rezultat = int(prv_broj) - int(vtor_broj)
#         elif operator == "*":
#             rezultat = int(prv_broj) * int(vtor_broj)
#         elif operator == "/":
#             rezultat = int(prv_broj) / int(vtor_broj)
#
#     except ZeroDivisionError:
#         print("se obiduvate da delite so nula")
#     except ValueError:
#         print("nevalidni vrednosti ili operatori")
#     else:
#         return rezultat
# print((kalkulator(3, "+" ,9)))
# print((kalkulator(8, "*" ,9)))




#  zadaci od funkcii

#  1

# lista1 = [1,2,3,4,5,6,7]
# lista2 = [10,11,12,13,14,15]
#
# def zbir_od_lista (lista):
#     suma = 0
#     for n in lista:
#         suma += n
#     return suma
# print(zbir_od_lista(lista1))
# print(zbir_od_lista(lista2))

#  2

# def najgolem_broj(prv, vtor, tret):
#     if prv >= vtor and prv >= tret:
#         return prv
#     elif vtor >= prv and vtor >= tret:
#         return vtor
#     else: return tret
# print(najgolem_broj(1, 2, 3))
# print(najgolem_broj(6, 5, 4))
# print(najgolem_broj(2, 8, 4))
# print(najgolem_broj(2, 2, 1))


#   3

# broj = input("Vnesi broj za koj sakas da se presmeta faktoriel: ")
#
# def faktoriel(broj):
#     try:
#         broj = int(broj)
#         if broj < 0:
#             raise ValueError("Vnesovte negativen broj.")
#         elif broj == 0:
#             return 1
#         else:
#             rezultat = 1
#             for i in range(1, broj + 1):
#                 rezultat *= i
#             return rezultat
#     except ValueError as e:
#         return f"Greska: {e}"
#
# print(f"Faktoriel od brojot {broj} iznesuva {faktoriel(broj)}")


#   4

#  7
# radius = input("vnesi radius: ")
# def dijametar(radius):
#     try:
#         if radius.isnumeric() and radius > 0:
#             return radius * 2
#     except ValueError:
#         print("vnesovte nesto sto ne e broj")
# print(f"dijametarot na krug so radius od {radius} iznesuva {dijametar(radius)}")
# def perimetar(radius):
#     try:
#         if radius.isnumeric() and radius > 0:
#             return radius*2*3.14159
#     except ValueError:
#         print("vnesovte nesto sto ne e broj")
# print(f"perimetarot na krug so radius {radius} iznesuva {perimetar(radius)}")
# def plostina(radius):
#     try:
#         if radius.isnumeric() and radius > 0:
#             return 3.14159*(radius * radius)
#     except ValueError:
#         print("vnesovte nesto sto ne e broj")
# print(f"plostina na krug so radius {radius} iznesuva {plostina(radius)}")


#   9
# ime = input("Vnesete ime na vraboteniot: ")
# plata = input("Vnesete plata za vraboteniot: ")
def show_employee(ime, plata = 9000):
    if not ime.isalpha():
        print("Imeto ne smee da sodrzi brojki i specijalni karakteri")
        return
    if  int(plata) < 9000:
        print("minimalnata plata iznesuva 9000")
        return

    print(ime, plata)
show_employee("jsjs", 9200)
show_employee("jsj4s", 900)
show_employee("js1js", 9200)

