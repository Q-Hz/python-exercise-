# 使用标志
prompt = "Tell me something, and I will reperat it to you."
prompt += "\nEnter 'quit' to end the program."
message = ""
active = True
while active:
     message = input(prompt)
     if message== 'quit':
         active = False
     else:
        print(message)

# break
prompt = "Tell me something, and I will reperat it to you."
prompt += "\nEnter 'quit' to end the program."
while True:
    message=input(prompt)
    if message != 'quit':
        print(message)
    else:
        break