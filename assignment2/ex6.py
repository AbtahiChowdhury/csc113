x={'Jen':'Python','Sarah':'C','Arif':'NONE','Arik':'C++'}

for k,v in x.items():
    if v=='NONE':
        print('{} you should take the poll'.format(k))
    else:
        print('{}, thank you for taking the poll'.format(k))    