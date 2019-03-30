favorite_places={'Abu':['Gym','Home'],'Kazi':['Park'],'Arif':['Pool','Home','Gym']}
for k,v in favorite_places.items():
    print('{}\'s favorite places are:'.format(k))
    for place in v:
        print('\t'+place)