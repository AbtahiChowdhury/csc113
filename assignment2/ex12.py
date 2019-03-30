x={}
while True:
    name=input('Enter your name:\t')
    number=input('What is your favorite number:\t')
    x[name]=number
    contin=input('Continue? [y/n]')
    if contin.lower()=='n':
        break

for k,v in x.items():
    print('{}: {}'.format(k,v))