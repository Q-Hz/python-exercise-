# 创建一个用于计算文档字数的函数，并尝试运用
def count_word_1(filename):
    """计算一个文件中大概有多少字数"""
    try:
        with open(filename, encoding='utf-8') as f_obj:  # 用UTF-8 进行解码
            contents = f_obj.read()
    except FileNotFoundError:
        print("Sorry, " + filename + " does not exist.")
    else:
        # 计算有多少个单词
        words = contents.split()
        num_words = len(words)
        print("The file Alice in Wonderland has " + str(num_words) + " words.")


# 创建要计算字数的文件名列表，其中有一个文件不存在
file_name_list = ['Alice in Wonderland.txt','siddhartha.txt' ,'little_women.txt', 'moby_dick.txt']
for filename in file_name_list:
    count_word_1(filename)
print()

#  当文件不存在时，pass
def count_word_2(filename):
    """计算一个文件中大概有多少字数"""
    try:
        with open(filename, encoding='utf-8') as f_obj:  # 用UTF-8 进行解码
            contents = f_obj.read()
    except FileNotFoundError:
        pass
    else:
        # 计算有多少个单词
        words = contents.split()
        num_words = len(words)
        print("The file Alice in Wonderland has " + str(num_words) + " words.")


# 创建要计算字数的文件名列表，其中有一个文件不存在
file_name_list = ['Alice in Wonderland.txt','siddhartha.txt' ,'little_women.txt', 'moby_dick.txt']
for filename in file_name_list:
    count_word_2(filename)