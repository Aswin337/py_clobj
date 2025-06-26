'''Abstraction :
     Abstraction is used to hide actual code to explicit some important code'''
from abc import ABC,abstractmethod        #import abstract using base class ABC from abc builtin module
class feature_plan(ABC):       #abstract class
    @abstractmethod
    def login(self):            #abstract method
        pass
    @abstractmethod
    def logout(self):           #abstract method
        pass
    def orders(self):
        pass
class web_develop(feature_plan):
    def design(self):
        print("Design completed")
    def login(self):                    #abstract method implementation.
        print("Login creation completed")
    def logout(self):                    #abstract method implementation.
        print("Logout creation completed")
w=web_develop()
w.design()
w.login()



''' once you declared abstract method inside ,abstract class then we must implement that method in child class.
 if we declare normal method in abstract class then it is (optional) to implement in child class.'''