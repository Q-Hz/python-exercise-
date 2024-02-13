# 输入相关信息，返回一个字典
def make_album(musician_name, album_name, album_number=''):
    """输入名字，专辑名，和专辑数量 ，返回完整字典"""
    album = {
        'musician': musician_name,
        'album': album_name,
    }
    if album_number:
        musician_name['number'] = album_number
    return album


while True:
    name = input("name ")
    album_name = input("album_name ")
    number = input("album_number" )
    album = make_album(name, album_name, number)
    print(album)


