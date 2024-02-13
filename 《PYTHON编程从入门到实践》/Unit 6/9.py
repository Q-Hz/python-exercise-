# 输入每个人最喜欢的地方名字
favourite_places={
    'Q.Hz':['gd','wuhan','macao'],
    'kuku':['yunnan','henan'],
    'landy':['england'],
}

for name,info in favourite_places.items():
    if len(info) == 1:
        print(name+' say: my favourite place is:',end=' ')
        for place in info:
            print(place,end='. ')
    else:
        print(name+' say: my favourite places are:',end=' ')
        end_place = info[-1]
        for place in info:
            if end_place == place:
                print(" and " + end_place, end='.')
            else:
                print(place,end=',')

    print()
