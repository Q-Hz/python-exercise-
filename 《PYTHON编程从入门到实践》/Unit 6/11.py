cities={
    'wuhan':{
        'country':'china',
        'population':'1200w',
        'fact':'aaa',
    },
    'gd':{
        'country':'china',
        'population':'1700w',
        'fact':'bbb',
    },
    'gx':{
        'country':'china',
        'population':'900w',
        'fact':'ccc',
    },
}
for city,info in cities.items():
    print(city)
    print("country: "+info['country'])
    print("population: "+info['population'])
    print("fact: "+info['fact'])
