# 总结练习
names = ['kuku', 'xiaoyao', 'chaige']
tra_des = ['singapore', 'ice land', 'switzerland', 'france', 'germany']
message = " want to have a travel to "
print("\t" + names[0].upper() + message + tra_des[0].title())
names.append('haha')  # 在names的末尾加上'haha'
print("\t" + names[-1].upper() + message + tra_des[1].title())

tra_des.insert(0,'israel')  # 在tra_des第一个位置插入israel
print("\t" + names[0].upper() + message + tra_des[0].title())
print(names)

del names[-1]  # 删除names的最后一个元素
print("\t" + names[-1].upper() + message + tra_des[0].title())

popped_tra_des = tra_des.pop(0)  # 弹出tra_des的第一个元素
print("\t"+names[0]+message+tra_des[0].title()+" and "+popped_tra_des.title())
names.remove('kuku')  # 去掉元素'kuku'
print(names)
names.sort()

print(names)  # 对names里面的元素按字母排序
'''
错误用法
（1）sor_names=names.sort()
print(sor_names)
why? 也许是函数sort()对names做的是永久性排序
（2）print（names.sort()）
why？“永久性”
函数sorted（）则可以运用上述用法
'''

names.sort(reverse=True)   # 对names的元素按字母进行反排序（反排序是指跟现有的排序相反，不是按照字母方式）
print(names)
sor_names = sorted(names)  # 对names的元素进行按字母的暂时排序
print(sor_names)
sor_names = sorted(names, reverse=True)  # 对names的元素进行暂时的按字母的反排序
print(sor_names)

'''
函数reverse()的错误用法
print(tra_des.reverse())
why,“永久性”
'''
print(tra_des)
tra_des.reverse()  # 永久性反排序
print(tra_des)
print(len(tra_des))  # 计算tra_des的元素个数
