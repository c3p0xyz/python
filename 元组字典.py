# 容器之元组和字典

a = (1,2,3,"hello",True,"世界")

print(a)  # 元组不能增删改，元组中的元素是不可变的

user = {"name":"liu","age":29,"hobby":"编程"}  # python的字典类似java的map

print(user)
print(user["name"])
print(user["hobby"])

name = user.get("name")
print(name)