# 用字典存储每个人喜欢的数字并打印
information_num={
    'crazy':['1','2'],
    'candy':['2','3','4'],
    'landy':['3','1'],
    'hansy':['4','2'],
    'dery':['5'],
    }
for name,num in information_num.items():
    if len(num)== 1:
        print(name+"'s favorite number is "+num[0]+".")
    else:
        end_number = num[-1]
        last_but_one = num[-2]
        print(name+"'s favourite numbers are: ",end='')
        for number in num:
            if end_number == number:
                print("and "+end_number+".")
            elif last_but_one== number:
                print(number,end=' ')
            else:
                print(number,end=', ')