class dad:
    def house(self):
        print("House :Red")
class mom:
    def shop(self):
        print("shop :green")
class daughter(dad,mom):
    def factory(self):
        print("Factory : yellow")
d=daughter()
d.factory()
d.house()
d.shop()


'''dad and mom both are parents to their child -daughter'''