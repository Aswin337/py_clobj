class grandfather:
    def farm_land(self):
        print("Land location :Kanyakumari")
class dad(grandfather):
    def house(self):
        print("House :Red")
class son(dad):
    def factory(self):
        print("Factory : yellow")
    def house(self):
        print("House :Blue")
s=son()
s.factory()
s.house()
s.farm_land()