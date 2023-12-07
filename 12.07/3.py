list1 = []
list2 = []


for i in range(10):
    num = int(input("请输入一个正整数: "))
    if num % 2 == 0:
        list1.append(num)
    else:
        list2.append(num)

print("奇数列表:", list2)
print("偶数列表:", list1)
