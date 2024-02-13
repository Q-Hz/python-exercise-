# 确定'Alice in Wonderland.txt'里面大约有多少单词
file_name = 'Alice in Wonderland.txt'
try:
    with open(file_name, encoding='utf-8') as f_obj: # 用UTF-8 进行解码
        contents = f_obj.read()
except FileNotFoundError:
    print("Sorry, " + file_name + " does not exist.")
else:
    # 计算有多少个单词
    words = contents.split()
    num_words = len(words)
    print(" The file Alice in Wonderland has " + str(num_words) + " words.")