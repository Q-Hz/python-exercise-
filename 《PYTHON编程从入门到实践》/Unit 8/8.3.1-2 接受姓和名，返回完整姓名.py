# 接受姓和名 返回完整的姓名
def get_full_name(first,last):
    """返回完整姓名"""
    full=first.title()+' '+last.title()
    return full
print(get_full_name('Q.','hz'))

# 接受姓和名 返回完整的姓名
def get_full_name(first,last,middle=''):
    """可带中间名返回完整姓名"""
    if middle:
        full=first.title()+' '+middle+' '+last.title()
    else:
        full=first.title()+' '+last.title()
    return full
print(get_full_name('Q.','Hz','handsome'))
print(get_full_name('Q.','Hz'))