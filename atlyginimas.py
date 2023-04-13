atlyginimas = input("Įveskite savo atlyginimą: ")
mokescio_procentas = input("Įveskite taikomą mokesčio procentą: ")
neto_atlyginimas = int(atlyginimas) * (1 - int(mokescio_procentas) / 100)
print(f"Jūsų atlyginimas į rankas yra: {neto_atlyginimas:.2f} EUR")