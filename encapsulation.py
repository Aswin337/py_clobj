class order:
    def __init__(self,name,items,total_amount,discount):
        self.name=name
        self.it=items
        self.__totalamount=total_amount
        self.__discount=discount
    def __calculation(self):
        return self.__totalamount-self.__discount
    def _access_by_admin(self):
        return {
            "Customer Name :":self.name,
            "Odered Items :":self.it,
            "Total Amount :":self.__totalamount,
            "Discount :":self.__discount,
            "Final Amount :" :self.__calculation()
        }
    def access_by_customer(self):
        return {
            "Customer Name :":self.name,
            "Odered Items :":self.it,
            "Final Amount :" :self.__calculation()
        }
class admin:
    def show_order(self,obj):
        print("Admin view :")
        return obj._access_by_admin()
class customer:
    def show_order(self,obj):
        print("Customer view :")
        return obj.access_by_customer()
ord=order("Aswin",["Dosa","Chappati"],500,100)
ad=admin()
print(ad.show_order(ord))
cust=customer()
print(cust.show_order(ord))