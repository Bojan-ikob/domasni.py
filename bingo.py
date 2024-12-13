import random

def igraci():
    lista_igraci = []
    while True:
        try:
            ime = input("Vnesete go vaseto ime: ").strip()
            broevi = list(map(int, input("Vnesete gi vasite sedum bingo broevi oddeleni so zapirka: ").split(',')))

            if len(broevi) != 7 or len(broevi) != len(set(broevi)) or not all(1 <= broj <= 26 for broj in broevi):
                print("Nemate vneseno tocno sedum broevi ili nekoi od broevite vi se povtoruvaat!!!")
                continue
            lista_igraci.append({"ime": ime, "broevi": broevi})

            dodadi_nov_igrac = input("Nov igrac: da/ne ").strip().lower()
            if dodadi_nov_igrac not in ["da", "ne"]:
                print("Vnesete 'da' za dodavanje nov igrac ili 'ne' za kraj.")
            elif dodadi_nov_igrac == "ne":
                break

        except ValueError:
            print("Nemate vneseno validni broevi!!!")
    return lista_igraci

def bingo_broevi():
    site_broevi = list(range(1, 26))
    izvleceni_bingo_broevi = random.sample(site_broevi, k=7)
    return izvleceni_bingo_broevi

def bingo_rezultati(lista_igraci, izvleceni_broevi):
    rezultati = []
    for igrac in lista_igraci:
        pogodeni = len(set(igrac['broevi']).intersection(izvleceni_broevi))
        rezultati.append({"ime": igrac["ime"], "pogodoci": pogodeni})
    return rezultati

igraci_lista = igraci()
print("Lista na igraci:", igraci_lista)

izvleceni_broevi = bingo_broevi()
print(f"Bingo broevi: {izvleceni_broevi}")

rezultati = bingo_rezultati(igraci_lista, izvleceni_broevi)
print("\nRezultati")
for pogodok in rezultati:
    print(f"Igrac: {pogodok['ime']}, Pogodoci: {pogodok['pogodoci']}")
