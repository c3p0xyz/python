import datetime as dt

# 获取当前日期
# now = dt.datetime.now()
# print(now)

# 获取指定日期
# date = dt.datetime(2019,10,1)
# print(date)

# 日期转字符串
# now = dt.datetime.now()
# # nowStr = now.strftime("%Y-%m-%d %H:%M:%S")
# # print(nowStr)
# # print(type(nowStr))

# 字符串转日期
str = "2020-2-20 2:20:20"
date = dt.datetime.strptime(str,"%Y-%m-%d %H:%M:%S")
print(date)
print(type(date))