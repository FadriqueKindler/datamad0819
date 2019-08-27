
# Soldier


class Soldier:
    
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
    
    def attack(self):
        return self.strength
          
    
    def recieveDamage(self, damage):
        self.health = self.health - damage
        


# Viking

class Viking(Soldier):

    def __init__(self, name, health, strength):
        self.name = name
        
        
    def recieveDamage(self, damage):
        self.health = self.health - damage
        if self.health > damage:
            return "{} has received {} points of damage".format(self.name, damage)
        else: 
            return "{} has died in act of combat".format(self.name)
    
    
    def battleCry(self):
        return "Odin Owns You All!"
        
        

# Saxon


class Saxon(Soldier):
    
    def __init__(self, health, strength):
    
    def recieveDamage(self, damage):
        self.health = self.health - damage
        if self.health > damage:
            return "A Saxon has received {} points of damage".format(damage)
        else: 
            return "A Saxon has died in combat"
        
    


# War


class War(self):
    
     def __init__(self):
            vikingarmy = ([])
            saxonarmy = ([])
    
        def addViking(self, viking):
            self.vikingarmy.append(viking)
    
    
        def addSaxon(self, saxon):
            self.saxonarmy.append(saxon)
    
    
    
        def vikingAttack(self):
        
        def saxonAttack(self):
    
        def showStatus(self):










