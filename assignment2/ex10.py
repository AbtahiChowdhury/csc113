favorite_numbers={'Arif':[7,4,2],'Arik':[4,8,19],'Abu':[52,76,1],'Kazi':[19,20,61],'Jim':[65,81,95]}
for k,v in favorite_numbers.items():
    print('{}\'s favorite numbers are:'.format(k))
    for number in v:
        print(number,end=' ',flush=True)
    print('\n')