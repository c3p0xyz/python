import json

# json 是有特定结构的字符串

# json 转为字典
j = '{"city":"北京","animal":"熊猫"}'
d = json.loads(j)
print(d)
print(type(d))
print("---------")
#  字典转 json

di = {"name":"天华","gender":"man"}
jsons = json.dumps(di,ensure_ascii=False)  # ensure_ascii 表示是否将汉字将为 ascii码
print(jsons)
print(type(jsons))