num1 = float(input("请输入第一个数："))
num2 = float(input("请输入第二个数："))
operator = input("请输入运算符号：")
if operator == "+":
    print("结果为：",num1 + num2)
elif operator == "-":
    print("结果为：",num1 - num2)
elif operator == "*":
    print("结果为：",num1 * num2)
elif operator == "/" :
    if num2 != 0:
        print("结果为：",num1 / num2)
    else:
        print("无意义")
