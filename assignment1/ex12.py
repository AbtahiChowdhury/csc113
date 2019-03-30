my_pizzas=['Jalapeno Pizza','Mushroom Pizza','Deep Dish Pizza']
friend_pizzas=my_pizzas[:]
my_pizzas.append('Grilled Chicken Pizza')
friend_pizzas.append('Plain Pizza')

print('My favorite pizzas are:')
for i in my_pizzas:
    print (i,end=', ',flush=True)

print('\nMy friend\'s favorite pizzas are:')
for j in friend_pizzas:
    print (j,end=', ',flush=True)
print('\n')