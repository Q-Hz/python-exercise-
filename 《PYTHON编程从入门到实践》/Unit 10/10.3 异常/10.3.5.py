# 练习FileNotFoundError
file_name = 'Alice.txt'
try:
    with open(file_name) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    print("Sorry, " + file_name + " does not exist.")