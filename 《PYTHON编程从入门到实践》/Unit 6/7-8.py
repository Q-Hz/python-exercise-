# 创建三个人的字典，打印其信息
information={
    'Q.Hz':{
        'first':'Q',
        'last':'Hz',
        'age':'18',
        'city':'gd',
    },
    'kuku':{
        'first':'andy',
        'last':'kuku',
        'age':'19',
        'city':'wuhan',
    },
    'landy':{
        'first':'angel',
        'last':'landy',
        'age':'17',
        'city':'yunnan',
    },
}
for name,info in information.items():
    full_name=info['first']+' '+info['last']
    print(name+' :'+full_name,end=', ')
    print("age: "+info['age'],end=', ')
    print("locates in "+info['city'])

