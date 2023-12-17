#Having the player Type, Focus and Descriptor be a class didnt make sense. They need to be hard coded sets of the data, that can de databased, then a function interal to the
#player class object can handle assigning features from those. 
# 

class playerCharacter:

    def __init__(self) -> None:
        self.name = ""
        self.tier = 1
        self.xp = 0
        self.stats = {"Might":0,"Speed":0,"Intellect":0,"Effort":1,"MightEdge":0,"SpeedEdge":0,"IntellectEdge":0}
        self.type = ""
        self.descriptor = ""
        self.focus =""
        self.armor = []
        self.weapon = []
        self.cyphers = []
        self.skills = []
        self.artifacts = []
  
    def assignType(self, type):

        match type:
            case "Protector":
                self.stats["Might"] = 10
                self.stats["Speed"] = 10
                self.stats["Intellect"] = 8
                
        pass

    def assignDesc():
        pass

    def assignFocus():
        pass



class equipment:
    def __init__(self) -> None:
        pass

class armor:
    def __init__(self) -> None:
        pass

class weapon:
    def __init__(self) -> None:
        pass

class cyphers:
    def __init__(self) -> None:
        pass

class artifacts:
    def __init__(self) -> None:
        pass

