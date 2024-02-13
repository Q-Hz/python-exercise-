#sort sorted reverse len
tra_des=['hai nan province','kun ming city','wu han city','singapo','ice land']
print(tra_des)
print(sorted(tra_des))#暂时按字母排序
print(tra_des)

tra_des.sort()#永久性按字母排序
print(tra_des)

tra_des.reverse()#倒序
print(tra_des)

tra_des.reverse()#再倒序
print(tra_des)
tra_des.sort()
print(tra_des)

tra_des.sort(reverse=True)#按字母倒序
print(tra_des)

print(sorted(tra_des,reverse=True)) # 暂时性按字母倒序

num=len(tra_des)#列表中的元素数
print(num)