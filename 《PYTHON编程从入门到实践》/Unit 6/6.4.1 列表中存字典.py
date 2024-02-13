# 字典存储在列表中
alien_0={'color':'green','point':'5'}
alien_1={'color':'yellow','point':'10'}
alien_2={'color':'red','point':'15'}
aliens =[alien_0,alien_1,alien_2]
for alien in aliens:
    print(alien)

# 自动生成30个，存在列表中
aliens=[]
for alien_num in range(0,30):
    new_alien ={'color':'green','points':'5','speed':'slow',}
    aliens.append(new_alien)
for alien in aliens[:5]:
    print(alien)
print("The total number of aliens is "+str(len(aliens)))
# 修改前三个字典元素的值
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = '10'
        alien['speed'] = 'medium'
for alien in aliens[:5]:
    print(alien)

#