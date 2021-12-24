'''
author =
'''
TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',

'''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

'''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''
]
oddelovac = 20 * '|*|'
mezera = '''
'''
registrovani = {'bob':'123',
                'ann':'pass123',
                'mike':'password123',
                'liz':'pass123'}
print(oddelovac)
print('Vítejte v aplikaci pro textový analyzátor.')
print(oddelovac)
jmeno = input('Sekce přihlášení.'
              '\n''Zadejte uživatelské jméno:')
heslo = input('Zadej heslo:')
if registrovani.get(jmeno) == heslo:
    print('Přihlášení v pořádku, pokračuji..')
    print(oddelovac)
else:
    print('Špatné heslo! Ukončuji')
    exit()
#získat od uživatele výběr ze 3 možnostíW
# a při textu nebo špatném výběru ho upozornit

vyber = input('Zadejte výběr 1-3')
if vyber.isalpha():
    print('Neplatná volba, ukončuji')
    exit()
elif vyber.isalnum() and int(vyber) <=3 and int(vyber) > 0:
    print(TEXTS[int(vyber)-1])
else:
    print('Neplatná volba, ukončuji!')
    exit()

#Počátadlo na text
print(oddelovac)
print(mezera)
list = []
celkem_slov = 0
for slovo in TEXTS[int(vyber) - 1].split():
    list.append(slovo.strip('.,: '))
for slovo in list:
    celkem_slov += 1


#- počet slov začínajících velkým písmenem,
#- počet slov psaných velkými písmeny,
#- počet slov psaných malými písmeny,

zac_velke_pismena = 0
full_velke = 0
male_pismena = 0
pocet_jedno_cisel = 0
for slovo in list:
    if slovo.istitle():
        zac_velke_pismena += 1
    elif slovo.isupper():
        full_velke += 1
    elif slovo.islower():
        male_pismena += 1

#- počet čísel (ne cifer),
for cislo in list:
    if cislo.isnumeric():
        pocet_jedno_cisel += 1

#- sumu všech čísel (ne cifer) v textu.
list_cisel = []
for cislo in list:
    if cislo.isnumeric():
        list_cisel.append(int(cislo))
vysledek = sum(list_cisel)
#Vypsání všech hodnot v textu
print(f'Celkem je ve vybraném textu {celkem_slov} slov.')
print(f'Z toho {zac_velke_pismena} je slov začínající s velkým písmenem.')
print(f'Slova psaná velkým písmenem je v textu {full_velke}.')
print(f'Slov jen s malými písmeny je {male_pismena}.')
print(f'Počet číslit obsažené v textu je {pocet_jedno_cisel}.')
print(f'Součet všech čísel v textu je {vysledek}.')
print(oddelovac)
#Program zobrazí jednoduchý sloupcový graf, který bude reprezentovat četnost různých délek slov v textu. Například takto:
seznam = []
knihovna = {}
for delka in list:
    d = len(delka)
    seznam.append(d)
seznam.sort()
for cisla in seznam:
    if cisla not in knihovna:
        knihovna.setdefault(cisla, 1)
    else:
        knihovna[cisla] += 1
#znazornit ze slovníku grafem počty slov
graf = []
print('DELKA | GRAF| POČET')
for klice in knihovna.items():
    delka = klice[0]
    pocet = klice[1]
    graf_1 = pocet * '*'
    print(delka, graf_1 ,'|',pocet)
print(oddelovac)
print('Konec programu. Ukončuji!')
