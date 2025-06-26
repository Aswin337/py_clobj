''' 1. @classmethod:
        *Takes cls (the class itself) as the first argument.
        *Can access and modify class-level data.
        *Called with either class or instance.
     2. @staticmethod:(run indepentantly)
        *Takes no default argument (no self, no cls).
        *Can't access instance or class data.
        *Used for utility/helper functions that belong to the class logically.'''

#Basic Example for class and static method
class myclass:
    def instance_method(self):
        print("called an instance method")
    @classmethod
    def class_method(cls):
        print("called an class method")
    @staticmethod
    def static_method():
        print("called an static method")
cl=myclass()
cl.instance_method()
myclass.class_method()
myclass.static_method()

#class method:
class team:
    team_leader="Aswin"
    @classmethod
    def new_team_leader(cls):
        cls.team_leader="Anachi"
#we dont want to create object for class method
team.new_team_leader()
print("New Team Leader :",team.team_leader)

#static method:
class math:
    @staticmethod
    def tool(x,y):
        return x+y
print(math.tool(1,3))


#class and static method example
class team:
    team_leader="Aswin"
    @classmethod
    def new_team_leader(cls):
        cls.team_leader="Anachi"
    @staticmethod
    def try_new_team_leader():
        team_leader="mudicheruky"
        return team_leader

#we dont want to create object for class method
team.new_team_leader()
print("New Team Leader(After class method) :",team.team_leader)
team. try_new_team_leader()
print("New Team Leader(After static method) :",team.team_leader)
print(team. try_new_team_leader())