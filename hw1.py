song = '''
동해물과 백두산이 마르고 닳도록
하느님이 보우하사 우리나라 만세
무궁화 삼천리 화려강산
대한사람 대한으로 길이 보전하세
'''
equal24 = '='*24

print(equal24)
print(song)

print(equal24)
print("\"대한\" 은 몇번 등장 : ", song.count("대한"))
print("\"동해\"의 인덱스 : ", song.index("동해"))
print("\"사랑\"의 인덱스 : ", song.find("사랑"))

song = song.replace("동해", "남해")
song = song.replace("백두산", "한라산")
print(equal24)
print(song)

song = song.strip()
print(equal24)
print(song)

song_list = song.split("\n")
print(equal24)
print(song_list)

print(equal24)
print(song_list[0])
print(song_list[1])
print(song_list[2])
print(song_list[3])
print(equal24)
