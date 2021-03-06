#!/usr/bin/python
import random
import sys
map1 = ['Zharki','Georgopol','Hospital','Gatka','Quarry','Primorsk',
        'Ferry Pier','Pochinki','Ruins','Rozhok','School','School Apartments',
        'Shooting Range','Severny','Stalbar','Yasnaya Polyana','Mansion','Shelter',
        'Prison','Mylta','Farm','Mylta Power','Lipovka','Kameshki','Novorepnoye',
        'Sosnovka Military Base']
map2 = ['Campo Militar','Tierra Bronca','El Azahar','Impala','Puerto Paraiso',
        'North Island','South Island','Tiny Island','Los Leones','La Bendita',
        'Junkyard','Minas Generales','Graveyard','Hacienda del Patron','Cruz del Valle',
        'Torre Ahumada','Water Treatment','San Martin','Power Grid','Pecado','Chumacera',
        'Minas del Valle','Los Higos','Prison','Minas del Sur','Valle del Var',
        'Monte Nuevo','Ladrillera','El Pozo','Trailer Park','Ruins','La Cobrereia',
        'Crater Fields']
map3 = ['Manufacturing','Bootcamp Alpha','Swamp Temple','River Town','Logging Camp West','Commerce',
        'Bootcamp Charlie','Beach','Coastal','Logging Camp East','Coconut Farm','Abandoned Resort',
        'Training Center','Bootcamp Bravo','Banyan Grove','Rice Farming Town','Dock']
map1size = len(map1) - 1
map2size = len(map2) - 1
map3size = len(map3) - 1
def pubgmap(number):
    drop = None
    if number is 1:
        rando = random.randint(0,map1size)
        drop =  map1[rando]
    elif number is 2:
        rando = random.randint(0,map2size)
        drop = map2[rando]
    elif number is 3:
        rando = random.randint(0,map3size)
        drop = map3[rando]
    return drop