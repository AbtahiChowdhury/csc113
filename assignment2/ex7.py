person1={'first_name':'Arik','last_name':'Idrisy','age':19,'city':'New York City'}
person2={'first_name':'Mohammed','last_name':'Arif','age':19,'city':'New York City'}
person3={'first_name':'Abtahi','last_name':'Chowdhury','age':18,'city':'New York City'}
people=[person1,person2,person3]

for person in people:
    for k,v in person.items():
        print('{}: {}'.format(k,v))
    print('\n')