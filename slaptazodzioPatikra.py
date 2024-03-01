def valytiByla(byla):
    with open(byla, 'w') as f:
        pass

def rasytiIByla(byla, txt):
    with open(byla, 'a', encoding='utf-8') as f:
        f.write(txt + '\n')

def skaitytiByla(byla):
    bylosDuomenys = []
    with open(byla, 'r', encoding='utf-8') as f:
        while True:
            eilute = f.readline()
            if len(eilute) != 0:
                bylosDuomenys.append(eilute.replace('\n', ''))
            else:
                break
    return bylosDuomenys

def tikrintiIlgi(slaptazodis):
    ilgis = len(slaptazodis)
    if ilgis < 12:
        toliau = False
        rezultatas = f'Netinkamas. Slaptažodis per trumpas. Trūksta {12 - ilgis} simbolio(ų).'
    else:
        toliau = True
        rezultatas = 'Slaptažodis tinkamas.'
    return toliau, rezultatas

def tikrintiDidzRaides(slaptazodis):
    kiekis = 0
    for simbolis in slaptazodis:
        if simbolis.isupper():
            kiekis += 1
    if kiekis < 2:
        toliau = False
        rezultatas = f'Netinkamas. Trūksta {2 - kiekis} didžiosios(ųjų) raidės(ių).'
    else:
        toliau = True
        rezultatas = 'Slaptažodis tinkamas.'
    return toliau, rezultatas

def tikrintiMazRaides(slaptazodis):
    kiekis = 0
    for simbolis in slaptazodis:
        if simbolis.islower():
            kiekis += 1
    if kiekis < 2:
        toliau = False
        rezultatas = f'Netinkamas. Trūksta {2 - kiekis} mažosios(ųjų) raidės(ių).'
    else:
        toliau = True
        rezultatas = 'Slaptažodis tinkamas.'
    return toliau, rezultatas

def tikrintiSkaicius(slaptazodis):
    kiekis = 0
    for simbolis in slaptazodis:
        if simbolis.isalpha():
            kiekis += 1
    if kiekis < 2:
        toliau = False
        rezultatas = f'Netinkamas. Trūksta {2 - kiekis} skaičiaus(ų).'
    else:
        toliau = True
        rezultatas = 'Slaptažodis tinkamas.'
    return toliau, rezultatas

def tikrintiSpec(slaptazodis, spec):
    kiekis = 0
    for simbolis in slaptazodis:
        if simbolis in spec:
            kiekis += 1
    if kiekis < 2:
        toliau = False
        rezultatas = f'Netinkamas. Trūksta {2 - kiekis} spec. simbolio(ų).'
    else:
        toliau = True
        rezultatas = 'Slaptažodis tinkamas.'
    return toliau, rezultatas

##################################################################################

simboliai = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '+', '=']

valytiByla('rezultatai.txt')
pradDuomenys = skaitytiByla('duomenys.txt')

for slaptazodis in pradDuomenys:
    if tikrintiIlgi(slaptazodis)[0] == False:
        rasytiIByla('rezultatai.txt', f'{slaptazodis:<30}{tikrintiIlgi(slaptazodis)[1]}')
    elif tikrintiDidzRaides(slaptazodis)[0] == False:
        rasytiIByla('rezultatai.txt', f'{slaptazodis:<30}{tikrintiDidzRaides(slaptazodis)[1]}')
    elif tikrintiMazRaides(slaptazodis)[0] == False:
        rasytiIByla('rezultatai.txt', f'{slaptazodis:<30}{tikrintiMazRaides(slaptazodis)[1]}')
    elif tikrintiSkaicius(slaptazodis)[0] == False:
        rasytiIByla('rezultatai.txt', f'{slaptazodis:<30}{tikrintiSkaicius(slaptazodis)[1]}')
    elif tikrintiSpec(slaptazodis, simboliai)[0] == False:
        rasytiIByla('rezultatai.txt', f'{slaptazodis:<30}{tikrintiSpec(slaptazodis, simboliai)[1]}')
    else:
        rasytiIByla('rezultatai.txt', f'{slaptazodis:<30}Slaptažodis tinkamas.')