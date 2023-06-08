import requests
from bs4 import BeautifulSoup
import PySimpleGUI as sg
from random import randint

url = 'http://quotes.toscrape.com'
r = requests.get(url)

soup = BeautifulSoup(r.text, "html.parser")

# citatos
quotes_spans = soup.select('.text')
quotes_list = [i.get_text() for i in quotes_spans]

# nuorodos
a_blocks = soup.find_all('a', attrs={'class': None})
hrefs = [i['href'] for i in a_blocks if i.get_text() == "(about)"]

# atsakymai
author_blocks = soup.find_all('small', class_='author')
answers = [i.get_text() for i in author_blocks]

# uzuominos1
hints1 = []
for i in answers:
    splitted = i.split()
    hint = ''
    for j in splitted:
        if '.' not in j:
            hint += f'{j[0]}.'
        else:
            hint += j
    hints1.append(hint)

# uzuominos2
def get_second_hint(i):
    r = requests.get(url + hrefs[i])
    soup = BeautifulSoup(r.text, "html.parser")
    text = soup.select('p')[1].get_text()
    return text

# GUI layout
layout = [
    [sg.Text(quotes_list[0], size=(80, 2), key='-QUOTE-')],
    [sg.InputText(size=(30, 1), key='-ANSWER-')],
    [sg.Output(size=(80, 10), key='-OUTPUT-')],
    [sg.Button('Submit'), sg.Button('Quit')]
]

# Create the window
window = sg.Window('Guess the Author', layout)

# Game loop
while True:
    event, values = window.read()
    
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break
    
    i = randint(0, 9)
    quote = quotes_list[i]
    answer1 = values['-ANSWER-']
    
    print('\n', quote)
    
    if answer1 == answers[i]:
        print(f"Correct! Answer is {answers[i]}")
    else:
        hint1 = hints1[i]
        print(hint1)
        window['-QUOTE-'].update(hint1)
        answer2 = window.read()[1]['-ANSWER-']
        
        if answer2 == answers[i]:
            print(f"Correct! Answer is {answers[i]}")
        else:
            hint2 = get_second_hint(i)
            print(hint2)
            window['-QUOTE-'].update(hint2)
            answer3 = window.read()[1]['-ANSWER-']
            
            if answer3 == answers[i]:
                print(f"Correct! Answer is {answers[i]}")
            else:
                print(f"Wrong! Correct answer is {answers[i]}")
    
    if_continue = sg.popup_yes_no('Continue?', grab_anywhere=True)
    
    if if_continue == 'No':
        break
    
    # Reset the game
    window['-QUOTE-'].update(quotes_list[0])
    window['-ANSWER-'].update('')
    window['-OUTPUT-'].update('')
    quotes_list = quotes_list[1:] + [quotes_list[0]]
    answers = answers[1:] + [answers[0]]
    hints1 = hints1[1:] + [hints1[0]]

# Close the window
window.close()
