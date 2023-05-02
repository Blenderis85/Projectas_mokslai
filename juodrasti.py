import PySimpleGUI as sg

layout = [
    (sg.Text("Kaip sekasi?"), ),
    (sg.Input(), ),
    (sg.Button("Atsakyti"), ),
]

window = sg.Window("Nuotaikos tikrinimas", layout)
event, values = window.read()
print(f"Supratom, kad jums sekasi {values[0]}")
window.close()