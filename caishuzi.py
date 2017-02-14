import random
num= int(input('请输入猜数字的范围   \n' ))
s = random.randint(1,num)
n = 0
while n < 10:
    numguess = int(input('请输入数字\n'))
    if numguess > s:
        print("数字太大")
    elif numguess <s:
        print("数字太小")
    elif numguess == s:
        print("Bingo!")
        break
    n +=1

