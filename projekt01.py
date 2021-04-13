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
in modern oceans. Other fish such as paddlefish
garpike and stingray are also present.'''
         ]

users = {
        'bob': '123',
        'ann': 'pass123',
        'mike': 'password123',
        'liz': 'pass123'
        }
ODD = '-' * 40

while True:
    jmeno = input('Username: ')
    heslo = input('Password: ')
    if jmeno.lower() in users and heslo == users[jmeno.lower()]:
        print(
             ODD, f'Welcome to the app, {jmeno}',
             'We have 3 texts to be analyzed', ODD, sep='\n'
             )
        break
    else:
        print("Incorrect username or password.")

while True:
    try:
        vyber = int(input('Enter a number btw. 1 and 3 to select: '))
        if 0 < vyber <= 3:
            vyber = vyber - 1
            break
        else:
            print('Between 1 and 3.')
    except ValueError:
        print('Input numbers only.')

TEXT = TEXTS[vyber]
cisty_text = []

for x in TEXT.split():
    ciste_slovo = x.strip('.,:').replace('\\n', "")
    cisty_text.append(ciste_slovo)

pocet_cisel = 0
suma_cisel = 0
velka_pismena = 0
mala_pismena = 0
vse_velkym = 0
alphanumeric = 0

for x in cisty_text:
    if x.isdecimal():
        pocet_cisel = pocet_cisel + 1
        suma_cisel = suma_cisel + int(x)
    elif x.isalpha():
        if x.islower():
            mala_pismena = mala_pismena + 1
        elif x.isupper():
            vse_velkym = vse_velkym + 1
            velka_pismena = velka_pismena + 1
        else:
            velka_pismena = velka_pismena + 1
    elif x.isalnum():
        alphanumeric = alphanumeric + 1

print(
      ODD, f'There are {len(TEXT.split())} words in the selected text.',
      f'There are {velka_pismena} titlecase words.', sep='\n'
     )

if vse_velkym == 0:
    print(f'There is not any uppercase word')
elif vse_velkym == 1:
    print(f'There is {vse_velkym} uppercase word')
else:
    print(f'There are {vse_velkym} uppercase words.')

print(f'There are {mala_pismena} lowercase words.')

if alphanumeric > 0:
    print(f'There is {alphanumeric} alphanumeric string.')
else:
    print(f'There is not any alphanumeric string.')

if pocet_cisel == 1:
    print(f'There is {pocet_cisel} numeric string.')
elif pocet_cisel == 0:
    print(f'There is not any numeric string.')
else:
    print(f'There are {pocet_cisel} numeric strings.')

print(
     f'The sum of all numbers is {suma_cisel}.',
     ODD, 'LEN|  OCCURENCES  |NR.', ODD, sep='\n'
     )

delka_slov = {}

for x in cisty_text:
    if len(list(x)) in delka_slov:
        delka_slov[len(list(x))] = delka_slov[len(list(x))] + 1
    else:
        delka_slov[len(list(x))] = 1

for x, y in sorted(delka_slov.items()):
    print(f'{x: ^2} |', y * '*', y)
