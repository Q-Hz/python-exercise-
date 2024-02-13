# 调用pyhton库里面的OrdereDict 方法 可以按顺序输出字典键值对
from collections import OrderedDict
favourite_languages = OrderedDict()
favourite_languages['jen'] = 'python'
favourite_languages['sarah'] = 'C'
favourite_languages['edwad'] = 'ruby'
favourite_languages['phil'] = 'pyhton'
for name,language in favourite_languages.items():
    print(name.title() + "'s favorite language is " + language.title() + ".")