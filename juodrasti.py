import json
import os

os.system("cls")

produktai_saldytuve = {}
filename = 'code_data.json'

try:
    with open('code_data.json', 'r') as f:
        for line in f:
            produktai_saldytuve = json.loads(line)
except FileNotFoundError:
    print("Klaida: nurodytas failas nebuvo rastas.")

while True:
    os.system("cls") 

    print("**** Programa saldytuvas ****\n")
    print("\x1b[32m" + "    ----=== Meniu ===----" + "\x1b[0m")
    print("\x1b[34m" + "1:" + "\x1b[0m" + " Prideti produktus i saldytuva")
    print("\x1b[34m" + "2:" + "\x1b[0m" + " Isimti produktus is saldytuvo")
    print("\x1b[34m" + "3:" + "\x1b[0m" + " Perziureti saldytuvo produktu sarasa" "\n")
    print("\x1b[31m" + "0:" + "\x1b[0m" + " Uzdaryti saldytuva")

    m_pasirinkimas = input("\nPasirinkite is " + "\x1b[32m" + "Meniu" + "\x1b[0m" 
                           + " (" + "\x1b[31m" + "0" + "\x1b[0m" + "-" + "\x1b[34m" 
                           + "3" + "\x1b[0m" + "): ")
    
    if m_pasirinkimas not in ["0", "1", "2", "3"]:
        print("\x1b[31m" + "Klaida" + "\x1b[0m" + ": Pasirinkite skaiciu nuo 0 iki 3" + "\n")
        input("Spauskite " + "\x1b[35m" + "ENTER" + "\x1b[0m" + " , kad grizti i " 
            + "\x1b[32m" + "MENIU " + "\x1b[0m")
    

    if m_pasirinkimas == "1":
        os.system("cls")

        print("\x1b[36m" + "Produktu sarasas: " + "\x1b[0m" + str(produktai_saldytuve) + "\n")
        print("\x1b[32m" + "Ideti" + "\x1b[0m" + "\n")

        produkto_pavadinimas = input("Iveskite produkto pavadinima: ")
        kiekis = float(input("Iveskite produkto kieki: "))

        if produkto_pavadinimas in produktai_saldytuve:
            produktai_saldytuve[produkto_pavadinimas] += kiekis
        else:
            produktai_saldytuve[produkto_pavadinimas] = kiekis

    if m_pasirinkimas == "2":
        os.system("cls")

        print("\x1b[36m" + "Produktu sarasas: " + "\x1b[0m" + str(produktai_saldytuve) + "\n")
        print("\x1b[35m" + "Isimti" + "\x1b[0m" + "\n")

        produktas_pavadinimas = input("Iveskite produkto pavadinima: ")
        kiekis = float(input("Iveskite produkto kieki: "))

        if produktas_pavadinimas in produktai_saldytuve:
           produktai_saldytuve[produktas_pavadinimas] -= kiekis
           if produktai_saldytuve[produktas_pavadinimas] <= 0:
              del produktai_saldytuve[produktas_pavadinimas]
        else:
           produktai_saldytuve[produktas_pavadinimas] = kiekis 

    elif m_pasirinkimas == "3":
        os.system("cls")
        print(f"\x1b[36m" + "Produktu sarasas: " + "\x1b[0m" + str(produktai_saldytuve) + "\n")
        input("Spauskite " + "\x1b[35m" + "ENTER" + "\x1b[0m" + " , kad grizti i " 
            + "\x1b[32m" + "MENIU " + "\x1b[0m")
 
    elif m_pasirinkimas == "0":
        os.system("cls")
        print("-------" + "\x1b[33m" + " Gražios dienos! " + "\x1b[0m" + "-------")
        break

with open(filename, 'w') as f:
    json.dump(produktai_saldytuve, f)
f.close()