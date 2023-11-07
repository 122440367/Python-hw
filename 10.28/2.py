w = float(input("输入行李的重量（kg）:"))
if w <= 10:
    print("运费为2.5元")
else:
    t = (w-10)*1.5 + 2.5
    print("运费为",t,"元",sep="")
