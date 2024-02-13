# 调用函数，打印一个句子
def favourite_book():
    """打印一个句子"""
    print("The content I have learned in this chapter is parameter and argument.")

favourite_book()

# 调用函数，打印最喜欢的书
def favorite_book(username):
    """打印最喜欢的书名"""
    print("My favorite book is "+username.title())

favorite_book('Glefo')
