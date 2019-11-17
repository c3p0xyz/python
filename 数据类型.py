# 数据类型转换

a = "1000"

b = float(a)

c = int(a)
print(b)
print(type(b))

print(bool(2000))
print(bool("2000"))

print(bool(0))  # bool() 为 0、""、None时为 False,其它为 True
print(bool(""))
print(bool(None))
print(bool("None"))