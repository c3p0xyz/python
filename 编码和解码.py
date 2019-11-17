# python 字符串有两种类型
#    bytes 存二进制
#    unicode 存字符串
#    bytes --> unicode 即编码 encode
#    unicode --> bytes 即解码 decode

# 编码
str = "我爱一条柴"
byte = str.encode("gbk")
print(byte)
print(type(byte))

# 解码
strr = byte.decode("gbk")  # 默认以utf8解码, 编码和解码必须一致
print(strr)
print(type(strr))
