Ilia={'Kind of pet':'cat','Owner':'Cupido'}
Chloe={'Kind of pet':'dog','Owner':'Zoi'}
Laima={'Kind of pet':'turtle','Owner':'Sjors'}
Mercédesz={'Kind of pet':'bird','Owner':'Athanasios'}
pets=[Ilia,Chloe,Laima,Mercédesz]

for pet in pets:
    for k,v in pet.items():
        print('{}: {}'.format(k,v))
    print('\n')