'''Class with constructor :'''
class student:
    def __init__(self,name,rollno):
        self.x=name
        self.y=rollno
    def attendance(self):
        print(f"{self.x} enters attendance using {self.y}")
    def exam(self):
        print(f"{self.x} seat alloted using {self.y}")
s=student("Mudicheruky","23ucs001")
s.attendance()
s.exam()
        