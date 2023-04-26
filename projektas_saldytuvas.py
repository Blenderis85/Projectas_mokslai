import os

os.system("cls")

produktai = {}

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
        print(f"\x1b[36m" + "Produktu sarasas: " + "\x1b[0m" + str(produktai) + "\n")
        print("Iveskite produkta: ")            
        produktas = input(">: ")
        print("\n" + "Iveskite kieki: ")
        kiekis = input(">: ")
        produktai[produktas] = kiekis

    # Meniu_pasirinkimas - 2 
    elif m_pasirinkimas == "2":
        os.system("cls")
        print(f"\x1b[36m" + "Produktu sarasas: " + "\x1b[0m" + str(produktai) + "\n")
        print('Iveskite produkta: ')
        produktas = input(">: ")
        del produktai[produktas]

    # Meniu_pasirinkimas - 3 
    elif m_pasirinkimas == "3":
        os.system("cls")
        print(f"\x1b[36m" + "Produktu sarasas: " + "\x1b[0m" + str(produktai) + "\n")
        input("Spauskite " + "\x1b[35m" + "ENTER" + "\x1b[0m" + ", kad grizti i " 
              + "\x1b[32m" + "MENIU " + "\x1b[0m")

    # Meniu_pasirinkimas - 0 
    elif m_pasirinkimas == "0":
        os.system("cls")
        print("-------" + "\x1b[33m" + "Gražios dienos!" + "\x1b[0m" + "-------")
        break