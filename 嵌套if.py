#　嵌套if
yearsal = 110
given = 35

if yearsal > 100:
    print("可以买宝马!")
    if given > 50:
        print("可以买宝马7系")
    elif given > 30:
        print("可以买宝马5系")
    elif given > 10:
        print("可以买宝马3系")
    else:
        print("还是买二手宝马吧!")
elif yearsal > 50:
    print("可以买奥迪!")
elif yearsal > 20:
    print("还是买二手吧!")
else:
    print("老铁,还是骑自行车吧!")