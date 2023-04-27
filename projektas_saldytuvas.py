import os

os.system("cls")

produktai_saldytuve = {}

while True:
    os.system("cls")

    # Pagrindinis meniu:

    # Čia yra keletas dažniausiai naudojamų spalvų kodų: "ANSI escape sequence"

      # Black: \x1b[30m
      # Red: \x1b[31m
      # Green: \x1b[32m
      # Yellow: \x1b[33m
      # Blue: \x1b[34m
      # Magenta: \x1b[35m
      # Cyan: \x1b[36m
      # Grzina i pradine spalva: \x1b[0m 

    print("**** Programa saldytuvas ****\n")
    print("\x1b[32m" + "    ----=== Meniu ===----" + "\x1b[0m")
    print("\x1b[34m" + "1:" + "\x1b[0m" + " Prideti produktus i saldytuva")
    print("\x1b[34m" + "2:" + "\x1b[0m" + " Isimti produktus is saldytuvo")
    print("\x1b[34m" + "3:" + "\x1b[0m" + " Perziureti saldytuvo produktu sarasa" "\n")
    print("\x1b[31m" + "0:" + "\x1b[0m" + " Uzdaryti saldytuva")

    m_pasirinkimas = input("\nPasirinkite is " + "\x1b[32m" + "Meniu" + "\x1b[0m" 
                           + " (" + "\x1b[31m" + "0" + "\x1b[0m" + "-" + "\x1b[34m" 
                           + "3" + "\x1b[0m" + "): ")

    # Meniu_pasirinkimas - 1 
    if m_pasirinkimas == "1":
        os.system("cls")
        print(f"\x1b[36m" + "Produktu sarasas: " + "\x1b[0m" + str(produktai_saldytuve) + "\n")
        print("\x1b[32m" + "Ideti" + "\x1b[0m" + "\n")
        produktas = str(input("Produktas: "))
        kiekis = float(input("Kiekis: "))
        if produktas in produktai_saldytuve:
           produktai_saldytuve[produktas] += kiekis
        else:
           produktai_saldytuve[produktas] = kiekis

    # Meniu_pasirinkimas - 2
    elif m_pasirinkimas == "2":
        os.system("cls")
        print(f"\x1b[36m" + "Produktu sarasas: " + "\x1b[0m" + str(produktai_saldytuve) + "\n")
        print("\x1b[31m" + "Isimti" + "\x1b[0m" + "\n")
        produktas = str(input("Produktas: "))
        kiekis = float(input("Kiekis: "))
        
        if produktas in produktai_saldytuve:
           produktai_saldytuve[produktas] -= kiekis
        else:
           produktai_saldytuve[produktas] = kiekis    

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