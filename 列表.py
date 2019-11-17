# 容器之列表

list1 = [1,2,3,"hello","世界"]

list1[0] = "liu"  # 直接设置列表的值
print(list1) # 直接打印列表

print(list1[4])

# 列表的切片
print(list1[0:3])  # 取值结果从0到3，包含0但是不包含3

# 逆向切片
print(list1[-3:-1]) # -1是指列表最后一个元素

# 列表新增
list1.append("zhang") # 在列表后追加

list1.insert(2,666)

# 列表删除
del list1[0]  # 根据索引删除方法1
list1.pop(0)  # 根据索引删除方法2

num = list1.count("hello") # 查询列表中元素为hello的个数

print(list1)

print(num)