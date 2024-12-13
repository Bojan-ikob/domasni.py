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
# from math import expm1
from array import array


#
# a = input()
# b = input()
# try:
#     print(int(a)/int(b))
# except:
#     print("Cannot divide a with b")


# try:
#     a = int(input())
#     b = int(input())
#     print(a / b)
# except ZeroDivisionError:
#     print("Ovoj kod ke se izvrsi samo dokolku imame delenje so 0")
#     print('Cannot divide with zero')
# except ValueError:
#     print("Ovoj kod ke se izvrsi samo dokolku imame neuspesno kastiranje vo int")
#     print("Vnesovte nesto sto ne e broj")
# except Exception:
#     print("Ovoj kod ke se izvrsi dokolku se sluci greska razlicna od ZeroDivisionError ili Value Error")
# else:
#     print("Ovoj kod ke izvrsi samo dokolku ne se sluci greska")
# finally:
#     print("Ovoj kod se izvrsvua nezavisno dali ima ili nema greska")
#     print("Ova print koj sto ke se izvrsi po try except bolokot")

#
# prv_broj = int(input("vnesi go prviot broj: "))
# vtor_broj = int(input("vnesi go vtoriot broj: "))
# operator = input("vnesi go operatorot: +,-,/,*")


# #  kalkulator
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









# def pozdrav(ime="", pozdrav="", prezime="hi"):
#     """
#
#     :param ime:
#     :param pozdrav:
#     :param prezime:
#     :return:
#     """
#     print(f"{pozdrav}, {ime} {prezime}")
# # pozdrav(pozdrav = "Zdravo", ime = "fr1")
# # pozdrav("Zdravo", "fr1")
# # pozdrav(prezime = "markovski", pozdrav = "zdravo", ime = "marko")
# pozdrav()

# def suma(a, b, *args):
#     suma_args = 0
#     for x in args:
#         suma_args += x
#     return a + b + suma_args
# print(suma(1, 3, 3,4,5,6,7))

# def opis_na_proizvod(ime, marka, cena, **kwargs):
#     print(ime)
#     print(marka)
#     print(cena)
#     for spec, opis in kwargs.items():
#         # print(f"{spec}: {opis}")
#         print((f"{spec.replace('_',' ')}: {opis}"))
#
# opis_na_proizvod("sam55", "sam", 100, kap_bat = 100, ekran = 5)
