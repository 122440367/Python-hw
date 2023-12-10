d = float(input("请输入年月，如202301："))
y = d // 100
m = d % 100
if m != 2:
    if m in (1,3,5,7,8,10,12):
        print("这个月有31天")
    else:
        print("这个月有30天")
else:
    if y %100 == 0:
        if y %400 == 0:
            print("这个月有29天")
        else:
            print("这个月有28天")
    else:
        if y % 4 == 0:
            print("这个月有29天")
        else:
            print("这个月有28天")
