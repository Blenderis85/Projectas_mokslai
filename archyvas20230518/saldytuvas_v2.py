import json
import os

class Saldytuvas:
    def __init__(self):
        self.produktai_saldytuve = {}
        self.filename = 'code_data.json'
        self.load_data()

    def load_data(self):
        try:
            with open(self.filename, 'r') as f:
                self.produktai_saldytuve = json.load(f)
        except FileNotFoundError:
            print("Klaida: nurodytas failas nebuvo rastas.")

    def save_data(self):
        with open(self.filename, 'w') as f:
            json.dump(self.produktai_saldytuve, f)

    def prideti_produktus(self):
        os.system("cls")
        print("\x1b[36mProduktu sarasas: \x1b[0m" + str(self.produktai_saldytuve) + "\n")
        print("\x1b[32mIdeti\x1b[0m" + "\n")

        produkto_pavadinimas = input("Iveskite produkto pavadinima: ")
        kiekis = float(input("Iveskite produkto kieki: "))

        if produkto_pavadinimas in self.produktai_saldytuve:
            self.produktai_saldytuve[produkto_pavadinimas] += kiekis
        else:
            self.produktai_saldytuve[produkto_pavadinimas] = kiekis

    def isimti_produktus(self):
        os.system("cls")
        print("\x1b[36mProduktu sarasas: \x1b[0m" + str(self.produktai_saldytuve) + "\n")
        print("\x1b[35mIsimti\x1b[0m" + "\n")

        produktas_pavadinimas = input("Iveskite produkto pavadinima: ")
        kiekis = float(input("Iveskite produkto kieki: "))

        if produktas_pavadinimas in self.produktai_saldytuve:
            self.produktai_saldytuve[produktas_pavadinimas] -= kiekis
            if self.produktai_saldytuve[produktas_pavadinimas] <= 0:
                del self.produktai_saldytuve[produktas_pavadinimas]
        else:
            self.produktai_saldytuve[produktas_pavadinimas] = kiekis

    def perziureti_sarasa(self):
        os.system("cls")
        print("\x1b[36mProduktu sarasas: \x1b[0m" + str(self.produktai_saldytuve) + "\n")
        input("Spauskite \x1b[35mENTER\x1b[0m, kad grizti i \x1b[32mMENIU\x1b[0m")

    def run(self):
        while True:
            os.system("cls")

            print("**** Programa saldytuvas ****\n")
            print("\x1b[32m" + "    ----=== Meniu ===----" + "\x1b[0m")
            print("\x1b[34m" + "1:" + "\x1b[0m" + " Prideti produktus i saldytuva")
            print("\x1b[34m" + "2:" + "\x1b[0m" + " Isimti produktus is saldytuvo")
            print("\x1b[34m" + "3:" + "\x1b[0m" + " Perziureti saldytuvo produktu sarasa" "\n")
            print("\x1b[31m" + "0:" + "\x1b[0m" + " Uzdaryti saldytuva")

            choice = input("Pasirinkite veiksma (0-3): ")
            
            if choice == "1":
                self.prideti_produktus()
            elif choice == "2":
                self.isimti_produktus()
            elif choice == "3":
                self.perziureti_sarasa()
            elif choice == "0":
                break