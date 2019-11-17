import tushare as tu
import time
while True:
    dataNow = tu.get_realtime_quotes("000591")
    name = dataNow.loc[0][0]   # 第一个0表示数据的第一行，第二个0表示第一行数据的第一个字段
    price = float(dataNow.loc[0][3])
    high = dataNow.loc[0][4]   # 最高价
    low = dataNow.loc[0][5]	# 最低价
    volumn = dataNow.loc[0][8] # 成交量
    amount = dataNow.loc[0][9] # 成交金额
    openToday = dataNow.loc[0][1]  # 当天开盘价
    pre_close = dataNow.loc[0][2]  # 昨日收盘价
    timee = dataNow.loc[0][30]     # 日期

    print("股票名：",name,"当前价格：",price,"最高价：",high,"最低价：",low,"成交量：",volumn,"成交额：",amount,"开盘价：",openToday,"收盘价：",pre_close,"日期：",timee)

    buy = 3.3
    sell = 3.4

    if price <= buy:
        print("可以买进了!")
    elif price > sell :
        print("可以开始卖了!")
    else:
        print("在等等吧!")
    time.sleep(5)