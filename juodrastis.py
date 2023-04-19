## UZDUOTYS:
## Pirma:
## Sukurti naują klasę Darbuotojas, turinčią savybes vardas, pavardė, pareigos ir atlyginimas (su numatyta minimalia alga)
## Sukurti naują objektą darbuotojas
## Atspausdinkite darbuotojo pareigas ir atlyginimą.
## Pakeisti darbuotojo atlyginimą.
## Atspausdinkite pilną darbuotojo informaciją.

class Darbuotojas:
    def __init__(self, vardas, pavarde, pareigos, atlyginimas=800):
        self.vardas = vardas
        self.pavarde = pavarde
        self.pareigos = pareigos
        self.atlyginimas = atlyginimas

    def __str__(self):
        return f'{self.vardas} {self.pavarde}, pareigos: {self.pareigos}, atlyginimas: {self.atlyginimas}'

darbuotojas = Darbuotojas('Andrius', 'Gedvilas', 'Programuotojas', 800)

print('Darbuotojo pareigos:', darbuotojas.pareigos)
print('Darbuotojo atlyginimas:', darbuotojas.atlyginimas)

darbuotojas.atlyginimas = 1200

print('Darbuotojas:', darbuotojas)