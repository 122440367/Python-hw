a = float(input("请输入答案:"))
i = 0
while i < 5:
    g = float(input("猜猜这个数是多少:"))
    if g < a:
        print("猜小了")
        i = i + 1
    elif g > a:
        print("猜大了")
        i = i + 1
    elif g == a:
        print("恭喜你猜中了")
        break
        #i = 6
if i == 5:
    print("很遗憾，5次机会已用尽，游戏结束")
