import random

auswahl = ['s','p','sch']

auswahl_bedeutung ={
    's': 'Stein',
    'p': 'Papier',
    'sch': 'Schere',
}

benutzer_punktzahl = 0
ai_punktzahl = 0

i = 0

while i < 5 :
    user_input = input('Wählen Sie von Stein, Papier, Schere (s, p, sch):')

    ai_auswahl = random.choice(auswahl)
    
    if user_input in auswahl:
        print(f'Ihre auswahl ist {auswahl_bedeutung[user_input]}. AI auswahl ist {auswahl_bedeutung[ai_auswahl]}.')
        if user_input == ai_auswahl:
            print('Gleich')
        elif user_input == 's' and ai_auswahl == 'sch':
            print('benutzer + 1!')
            benutzer_punktzahl += 1
        elif user_input == 'p' and ai_auswahl == 's':
            print('benutzer + 1!')
            benutzer_punktzahl += 1
        elif user_input == 'sch' and ai_auswahl == 'p':
            print('benutzer + 1!')
            benutzer_punktzahl += 1
        else:
            print('AI + 1!')
            ai_punktzahl += 1
    else:
        print('Nicht Korrekt')
        i -= 1
        
    print(f'Benutzer punktzahl: {benutzer_punktzahl} / AI punktzahl: {ai_punktzahl}')    
    print('\n','-'*15)  
    i += 1  
    
if benutzer_punktzahl > ai_punktzahl:
    print(f'Benutzer mit {benutzer_punktzahl} gewonnen.')
elif benutzer_punktzahl < ai_punktzahl:
    print(f'AI mit {ai_punktzahl} gewonnen.')
else:
    print(f'Splie würed Gleich mit {ai_punktzahl} Punkte beendet.')
