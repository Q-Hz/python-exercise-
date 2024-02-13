# 练习ValueError_1
print("Give me two numbers and I'll give you the result. ")
number_1 = input("Enter the first number ")
number_2 = input("Enter the second number ")
try:
    answer = int(number_1) / int(number_2)
except ValueError:
    print("I need number instead of string.")
else:
    print(answer)


# 练习ValueError_2
print("Give me two numbers and I'll give you the result. ")
print("Enter 'q' to quit the program.")
while True:
    number_1 = input("Enter the first number ")
    if number_1 == 'q':
        break
    number_2 = input("Enter the second number ")
    if number_2 == 'q':
        break
    try:
        answer = int(number_1) / int(number_2)
    except ValueError:
        print("I need number instead of string.")
    else:
        print(answer)