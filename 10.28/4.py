a = float(input("输入第一边："))
b = float(input("输入第二边："))
c = float(input("输入第三边："))
if a>0 and b>0 and c>0:
    if a <= b <= c:
        MIN = a
        MAX = c
        MID = b
    elif a <= c <= b:
        MIN = a
        MAX = b
        MID = c
    elif b <= a <= c:
        MIN = b
        MAX = c
        MID = a
    elif b <= c <= a:
        MIN = b
        MAX = a
        MID = c
    elif c <= a <= b:
        MIN = c
        MAX = b
        MID = a
    elif c <= b <= a:
        MIN = c
        MAX = a
        MID = b
    if MIN**2 + MID**2 == MAX**2:
        S = MIN * MID / 2
        print("面积为",S,sep = "")
    else:
        print("no")
