# 利用循环删除列表中重复的元素
pets=['cat', 'dog', 'duck', 'cat', 'cat']
while 'cat' in pets:
    pets.remove('cat')
for pet in pets:
    print(pet,end=' ')