import random as r

class Hero:
    def __init__(self, name, battle_class):
        self.name = name
        self.health = r.randint(100,150)
        self.attack_power = r.randint(10,25)
        self.battle_class = battle_class

    def attack(self):
        return r.randint(1, self.attack_power)

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0
            print(f"{self.name} takes {damage} damage. {self.name} is dead.")
        else:
            print(f"{self.name} takes {damage} damage. {self.health} health remaining.")

    def is_alive(self):
        if self.health > 0:
            return True
        else:
            return False
