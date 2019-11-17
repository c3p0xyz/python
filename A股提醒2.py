import tushare as tu
import time


class Share():
    def __init__(self,code):
        self.name = ""
        self.price = ""
        self.high = ""
        self.low = ""
        self.volumn = ""
        self.amount = ""
        self.openToday = ""
        self.pre_close = ""
        self.timee = ""
        self.desc = ""
        self.code = code


def get_realtime_quote(share):
    dataNow = tu.get_realtime_quotes(share.code)
    share.name = dataNow.loc[0][0]  # 第一个0表示数据的第一行，第二个0表示第一行数据的第一个字段
    share.price = float(dataNow.loc[0][3])
    share.high = dataNow.loc[0][4]  # 最高价
    share.low = dataNow.loc[0][5]  # 最低价
    share.volumn = dataNow.loc[0][8]  # 成交量
    share.amount = dataNow.loc[0][9]  # 成交金额
    share.openToday = dataNow.loc[0][1]  # 当天开盘价
    share.pre_close = dataNow.loc[0][2]  # 昨日收盘价
    share.timee = dataNow.loc[0][30]

    share.desc = "股票名称: ",share.name," 股票价格: ",str(share.price)

    return share

def main(code,buy,sell):
    share = Share(code)
    share = get_realtime_quote(share)
    print(share.desc)

    if share.price <= buy:
        print("好时机,可以买进!")
    elif share.price > sell:
        print("抓紧时间,可以卖出!")
    else:
        print("时机未到,再等等!")

while True:
    main("000591",3.3,3.4)
    time.sleep(5)
