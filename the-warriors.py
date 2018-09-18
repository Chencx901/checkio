class Warrior:
#    初始化health and attack
    def __init__(self,health = 50,attack = 5):
        self.health = health
        self.attack = attack
# 定义is_alive()属性 :use @property
    @property
    def is_alive(self):
        if self.health > 0:
            return True
        else:
            return False
class Knight(Warrior):
    def __init__(self,health = 50,attack = 7):
        self.attack = attack
        self.health = health

def fight(unit_1, unit_2):
    while unit_1.health >0 and unit_2.health >0:
        if unit_1.health >0:
            unit_2.health =  unit_2.health - unit_1.attack
        if unit_2.health >0:
            unit_1.health =  unit_1.health - unit_2.attack
        
    if unit_1.health > 0:
        return True
    else:
        return False