# pizza中包括表皮类型和配料表
pizza={
    'crust':'thick',
    'toppings':['mushrooms','extra cheese']
     }
print(pizza['crust'])
for topping in pizza['toppings']:
    print(topping)

# 调查每个人喜欢的语言
favourite_languages={
    'jen':['python','ruby'],
    'sarah':['c'],
    'edward':['ruby','go'],
    'phil':['python','haskell'],
    }
for name,languages in favourite_languages.items():
    if len(languages) == 1:
        print(name.title()+"'s favourite language is:")
        for language in languages:
            print("\t" + language)
    else:
        print(name.title()+"'s favourite languages are :")
        for language in languages:
            print("\t"+language)
