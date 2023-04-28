import os

os.system("cls")

produktai_saldytuve = {}

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

    # Meniu pasirinkimas - 1

    if m_pasirinkimas == "1":
        os.system("cls")

        print("\x1b[36m" + "Produktų sąrašas: " + "\x1b[0m" + str(produktai_saldytuve) + "\n")
        print("\x1b[32m" + "Įdėti" + "\x1b[0m" + "\n")

        produktas = input("Produktas: ")
        kiekis_str = input("Kiekis: ")
        kiekis = float(kiekis_str[:-2])

        if kiekis_str[-2:] == "kg":
            kiekis = str(kiekis) + "kg"
        else:
            kiekis = str(kiekis)

        if produktas in produktai_saldytuve:
           produktai_saldytuve[produktas] += kiekis
        else:
           produktai_saldytuve[produktas] = kiekis

    # Meniu_pasirinkimas - 2

    if m_pasirinkimas == "2":
        os.system("cls")

        print("\x1b[36m" + "Produktų sąrašas: " + "\x1b[0m" + str(produktai_saldytuve) + "\n")
        print("\x1b[32m" + "Įdėti" + "\x1b[0m" + "\n")

        produktas = input("Produktas: ")
        kiekis_str = input("Kiekis: ")
        kiekis = float(kiekis_str[:-2])

        if kiekis_str[-2:] == "kg":
            kiekis = str(kiekis) + "kg"
        else:
            kiekis = str(kiekis)

        if produktas in produktai_saldytuve:
           produktai_saldytuve[produktas] -= kiekis
        else:
           produktai_saldytuve[produktas] = kiekis
        if produktas in produktai_saldytuve:
           produktai_saldytuve[produktas] -= kiekis
           if produktai_saldytuve[produktas] <= 0:
                del produktai_saldytuve[produktas]

    # Meniu_pasirinkimas - 3 
    
    elif m_pasirinkimas == "3":
        os.system("cls")
        print(f"\x1b[36m" + "Produktu sarasas: " + "\x1b[0m" + str(produktai_saldytuve) + "\n")
        input("Spauskite " + "\x1b[35m" + "ENTER" + "\x1b[0m" + " , kad grizti i " 
              + "\x1b[32m" + "MENIU " + "\x1b[0m")

    # Meniu_pasirinkimas - 0 
    elif m_pasirinkimas == "0":
        os.system("cls")
        print("-------" + "\x1b[33m" + " Gražios dienos! " + "\x1b[0m" + "-------")
        break
    
    ## Nauja uzduotis: iterpti kilogramus, litrus, vienetus.