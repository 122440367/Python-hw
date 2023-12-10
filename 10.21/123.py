x = float(input("请输入x的值："))
y = float(input("请输入y的值："))
z = float(input("请输入z的值："))
a = (x + y + z)/3
if x > y:
    if x > z:
        print("最大值为：",x,sep = "")
    else:
        print("最大值为：",z,sep = "")
else:
    if y > z:
        print("最大值为：",y,sep = "")
    else:
        print("最大值为：",z,sep = "")
print("平均数为：",a)
        
    
#x = float(input("请输入x的值："))
#y = float(input("请输入y的值："))
#z = float(input("请输入z的值："))
#a = (x + y + z)/3
#if x > y and x >z:
#   print("最大值为：",x,sep = "")
#elif ......:
#elif
#print("平均数为：",a)
