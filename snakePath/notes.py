# Inheritance allows other classes to posess the exact attributes and methods of another class
# For instance:

# parent class:
class FootballClub:
    def __init__(self):
        self.num_of_players = 11;
        self.managers = 2;
        self.stadia = 1;

    def info(self):
        print("This is a football club");


# Inherited class
class ManUtd(FootballClub):
    def __init__(self,name):
        super().__init__() #initialises everything in the football class
        self.name = name;
        self.num_of_players = 35; #modifiiying number of players
    
    def info(self):
        super().info(); # getting past info from the parent class
        print(f"it's name is {self.name}, it has {self.num_of_players} players ");


Man_U_2023 = ManUtd("Man Utd: the Gen z era");

print(Man_U_2023.info());