class parent:
    def pub(self):
        print("I AM PUBLIC")
    def _pro(self):
        print("I AM PROTECTED")
    def __pri(self):
        print("I AM PRIVATE")
    def access_same_class(self):
        print("INSIDE SAME CLASS :")
        self.pub()
        self._pro()
        self.__pri()
class child(parent):
    def access_sub_class(self):
        print("INSIDE SUB(OR)CHILD CLASS :")
        self.pub()
        self._pro()
        try:
            self.__pri()
        except AttributeError:
            print("private variable cannot Access")
class strange:
    def access_strange_class(self,obj):
        print("INSIDE STRANGE CLASS :")
        obj.pub()
        obj._pro()
        try:
            obj.__pri()
        except AttributeError:
            print("private variable cannot Access")
p=parent()
p.access_same_class()
c=child()
c.access_sub_class()
s=strange()
s.access_strange_class(p)