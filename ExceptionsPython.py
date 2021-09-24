

itemsInCart = 0
# 2 items willl be added to cart

if itemsInCart != 2:
    # raise Exception("Products cartcount not matching")
    pass

assert(itemsInCart == 0)

#try , catch

try:
    with open('filelog.txt', 'r') as reader:
        reader.read()


except Exception as e:
    print(e)

finally:
    print("cleaning up resources ")