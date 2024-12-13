
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

# broj = int(input("vnesi broj: "))
# print(len(str(broj)))


# 17

# 18

# 19

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


