# 新建一个类

class Phone():
    def __init__(self,band,price,color):
        self.band = band
        self.price = price
        self.color = color

    def sendMessage(self):
        print(self.band,"可以用来发短信")


phone = Phone("小米",2799,"蓝")
print(phone.band)
print(phone.price)
print(phone.color)

phone.sendMessage()