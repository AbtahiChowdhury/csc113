cities={'New York City':{'Country':'United States','Population':8000000,'Fact':'nicknamed the Big Apple'},'Sydney':{'Country':'Australia','Population':5000000,'Fact':'most populous city in Australia'},'Tokyo':{'Country':'Japan','Population':9000000,'Fact':'was formally named Edo'}}

for k,v in cities.items():
    print('{}:'.format(k))
    for i,j in v.items():
        print('{}: {}'.format(i,j))
    print('\n')