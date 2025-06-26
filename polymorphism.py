'''polymorphism :
poly-Many and Morphism-forms'''
class dad:
    def house(self):
        print("House colour :yellow")
class daughter(dad):
    def mall(self):
        print("Mall colour : pink")
    def house(self):                       #overriding-same method with same argument
        print("House colour :Blue")
d=daughter()
d.mall()
d.house()