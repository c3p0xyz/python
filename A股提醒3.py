# 查询多只股票
import tushare as tu
import smtplib
from email.mime.text import MIMEText

class Share():
    def __init__(self,code,buy,sell):
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
        self.buy = buy
        self.sell = sell


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

    share.desc = "股票名称: "+share.name+"股票价格: "+str(share.price)
    return share

# 邮件提醒
def sendEmai(subject,content):
    msg_from = "liutianhua522@163.com"
    to = "343585865@qq.com"
    code = "lth521"

    msg = MIMEText(content)
    msg["From"] = msg_from
    msg["To"] = to
    msg["Subject"] = subject
    try:
        email = smtplib.SMTP_SSL("smtp.163.com",465)
        email.login(msg_from,code)
        email.sendmail(msg_from,to,msg.as_string())
        print("邮件发送成功!")
    except Exception as e:
        print("邮件发送失败!",e)

def main(list1):
    for i in list1:
        share = get_realtime_quote(i)
        print(share.desc)

        if share.price < i.buy:
            print("老铁,可以买入")
            sendEmai("达到买点",share.desc)
        elif share.price > i.sell:
            print("老铁,可以卖出了")
            sendEmai("达到卖点",share.desc)
        else:
            print("老铁,再等等!")

share1 = Share("600106",3.1,3.3)
share2 = Share("601988",3.5,3.8)
share3 = Share("000591",3.3,3.4)

list1 = [share1,share2,share3]

main(list1)