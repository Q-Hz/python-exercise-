#  分别打印键值对、健、值
rivers={
    'chang jiang':'china',
    'nile':'egypt',
    'Mekong River':'Burma',
    }
for river,country in rivers.items():
    print("The "+river.title()+"runs through "+country.title()+".")
for river_name in rivers.keys():
    print(river_name)
for country_name in rivers.values():
    print(country_name)

#根据调查名单，若有字典中人名，则...
favourite_languages ={
    'jen':'python',
    'sarah':'C',
    'edward':'ruby',
    'phil':'python',
}

researched_list = ['jen','kuku']
for researched_name in researched_list:
    if researched_name in favourite_languages.keys():
        print(researched_name+", thank you for your participation.")
    else:
        print(researched_name+", please participate in the research.")