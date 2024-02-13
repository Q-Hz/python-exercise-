# 函数返回一个字典
def build_person(first,last):
    """返回一个字典"""
    person = {'first——name':first,'last_name':last}
    return person
musician = build_person('jimi', 'hendrix')
print(musician)

# 函数和while循环
def get_formatted_name(first_name,last_name):
    full_name = first_name + ' ' + last_name
    return full_name
while True:
    print("Please tell me your name.\nEnter 'no' at any time to end the program")
    active = input("If  continue? (yes/no) ")
    if active == 'no':
        break
    first = input("Your first name ")
    if first == 'no':
        break
    last = input("Your last name ")
    if last == 'no':
        break
    full = get_formatted_name(first,last)
    print("Hello, "+full)