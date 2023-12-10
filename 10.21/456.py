n = int(input("请输入一个三位数："))
a = n//100
b = (n -a*100)//10
#b = n//10%10
c = n - 100*a - 10*b
#c = n%10
print("各位数分别为：",a,b,c)
i = a ** 3 + b ** 3 + c **3
if i == n:
    print("这是一个水仙花数！")
else:
    print("这不是一个水仙花数！")

