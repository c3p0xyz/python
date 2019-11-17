# 复制文件

file = open("E:\道德经.txt","rb")
outFile = open("E:\道德经copy.txt","wb")

data = file.read()
outFile.write(data)

outFile.close()
file.close()

print("ok")