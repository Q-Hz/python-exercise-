# tyr-except 代码块处理指定异常
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero")