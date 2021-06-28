str1 = input('문자열일 입력 : ')

first = str1[1::3]
second = str1[0::3]
third = str1[2::3]

password = first + second + third
print('암호화 :', password)
