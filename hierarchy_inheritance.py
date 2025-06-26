class dad:
    def house(self):
        print("House :Red")
class son1(dad):
    def factory(self):
        print("Factory : yellow")
    def house(self):
        print("House :Blue")
    
class son2(dad):
    def mart(self):
        print("mart :voilet")
    def house(self):
        print("House :Orange")
s1=son1()
s1.factory()
s1.house()
s2=son2()
s2.house()
s2.mart()
d=dad()
d.house()