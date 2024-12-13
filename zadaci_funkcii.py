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

#  ||
# def max_od_tri(a, b, c, *args):
#     return max(a,b,c)
# print(max_od_tri(1,3,5))



#   3


# broj = input("Vnesi broj za koj sakas da se presmeta faktoriel: ")
#
# def faktoriel(broj):
#     try:
#         broj = int(broj)
#         if broj < 0:
#             raise ValueError("Vnesovte negativen broj.")
#         elif broj == 0 or broj == 1:
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
# def delivi_so_sumata_od_cifri():
#     rezultat = []
#     for broj in range(100, 1000):
#         cifri = [int(cifra) for cifra in str(broj)]
#         suma_na_cifri = sum(cifri)
#
#         if broj % suma_na_cifri == 0:
#             rezultat.append(broj)
#
#     return rezultat
# print(delivi_so_sumata_od_cifri())

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
# def show_employee(ime, plata = 9000):
#     if not ime.isalpha():
#         print("Imeto ne smee da sodrzi brojki i specijalni karakteri")
#         return
#     if  int(plata) < 9000:
#         print("minimalnata plata iznesuva 9000")
#         return
#
#     print(ime, plata)
# show_employee("jsjs", 9200)
# show_employee("jsj4s", 900)
# show_employee("js1js", 9200)

#  10

def zbir_razlika ():
    while True:
        try:
            br1 = int(input("Vnesi broj: "))
            br2 = int(input("Vnesi broj: "))
            break
        except ValueError:
            print("Vnesovte pogresni vrednosti ...Vnesete broj: ")

    zbir = br1 + br2
    razlika =  br1 - br2
    return zbir, razlika

zbir, razlika = zbir_razlika()
print(f"zbir:{zbir}")
print(f"razlika:{razlika}")



#  12

# broj = input("Vnesi go brojot: ")
# od_broj = input("Vo rang od: ")
# do_broj = input("Vo rang do: ")
#
# def pripaga_vo_rang(broj, od_broj, do_broj):
#     if broj.isnumeric() and od_broj.isnumeric() and do_broj.isnumeric():
#         pomal_broj = min(od_broj, do_broj)
#         pogolem_broj = max(od_broj, do_broj)
#
#         if pomal_broj <= broj <= pogolem_broj:
#             print(f"Brojot {broj} pripaga vo rangot od {pomal_broj} do {pogolem_broj}")
#         else:
#             print(f"Brojot {broj} ne pripaga vo rangot od {pomal_broj} do {pogolem_broj}")
#     else:
#         print("vnesovte pogresni vrednosti")
# pripaga_vo_rang(broj, od_broj, do_broj)




#  15

#
# def check_anagram(n):
#     return lambda data: len(data) == n


# def filter_letters(data: str):
#     data = data.lower()
#     letters = list(filter(lambda x: x.isalpha(), data))
#     print(letters)
#
#     letters_map = dict.fromkeys(letters, 0)
#     print(letters_map)
#
#     for letter in letters:
#         if letters_map.get(letter) == 0:
#             letters_map[letter] = letters.count(letter)
#
#     print(letters_map)
#     return letters_map
#
#
# recenica = input("Vnesete edna recenica: ")
# letters = filter_letters(recenica)
#
# check_anagram_en = check_anagram(26)
# check_anagram_mk = check_anagram(31)
#
# if check_anagram_en(letters):
#     print("PANAGRAM!")
#
# if check_anagram_mk(letters):
#     print("PANAGRAM!")



# 16

# def broj_soglaski_samoglaski(entry):
#
#     samograski = ('a', 'i', 'e', 'o', 'u', 'r')
#     samoglaski_broj = 0
#     soglaski_broj = 0
#
#     for bukva in entry:
#         if bukva in samograski:
#             samoglaski_broj += 1
#         else:
#             if not bukva.isalpha():
#                 continue
#             else:
#                 soglaski_broj += 1
#
#     return soglaski_broj, samoglaski_broj
#
# recenica = input("Vnesi edna recenica: ")
# samoglaski, soglaski = broj_soglaski_samoglaski(recenica)
#
# print(f"recenicata ima {samoglaski} samoglaski i {soglaski} soglaski")
#
#
#
# # 16.1
#
# def get_data_by_word(data):
#     data_dict = {}
#     for zbor in data.split():
#         zbor = zbor.strip()
#         if data_dict.get(zbor) is None:
#             soglaski, samograski = broj_soglaski_samoglaski(zbor)
#             data_dict[zbor] = f"soglaski: {soglaski}, samoglaski: {samograski}"
#
#     return data_dict
#
# soglaski_samoglaski_po_zbor = get_data_by_word(recenica)
# print(soglaski_samoglaski_po_zbor)