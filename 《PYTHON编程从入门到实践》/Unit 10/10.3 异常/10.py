# 统计某书本里面单词‘the’出现了多少次
def count_special_word(file_name,special_word):
    """统计某特定单词出现次数"""
    try:
        with open(file_name,encoding='utf-8') as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        print("Sorry " + file_name + " can't be found.")
    else:
        num_words = contents.count(special_word)
        print(num_words)


file_name = 'Alice in Wonderland.txt'
count_special_word(file_name,'the')
