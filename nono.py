from bisect import insort

produkti = ["leb", "sok", "brasno", "zejtin", "domaten sos"]
kupeni_produkti = []
nekupeni_produkti = produkti.copy()
while True:
    produkt = input("Vnesi KRAJ za kraj ili vnesi go produktot: ").strip().lower()
    if produkt == "kraj":
        break
    else:
        if produkt in produkti:
            if produkt not in kupeni_produkti:
                kupeni_produkti.append(produkt)
                nekupeni_produkti.remove(produkt)
                f = open("nekupeni_produkti.txt", "w")
                f.write("Nekupeni proizvodi\n\n")
                for nekupen_proizvod in nekupeni_produkti:
                    f.write(f"{nekupeni_produkti.index(nekupen_proizvod)+1}. {nekupen_proizvod}\n")
        if produkt not in produkti:
            kupeni_produkti.append(produkt + ' ' + "*")
            kupeni_produkti = list(dict.fromkeys(kupeni_produkti))
            f = open("kupeni_produkti.txt", "w")
            f.write("Kupeni proizvodi\n\n")
            for kupen_proizvod in kupeni_produkti:
                f.write(f"{kupeni_produkti.index(kupen_proizvod) + 1}. {kupen_proizvod}\n")

    print(f"Produkti {produkti}")
    print(f"Kupeni produkti: {kupeni_produkti}")
    print(f"Nekupeni produkti: {nekupeni_produkti}")

print("KRAJ")


import pandas
