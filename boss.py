from enemy import Enemy


class Boss(Enemy):
    """A stronger enemy with a powered-up attack."""

    def __init__(self, name):
        super().__init__(name, health=250, attack_power=50)

    def attack(self):
        damage = super().attack()
        bonus_damage = 5
        print(f"{self.name} unleashes a crushing blow!")
        return damage + bonus_damage

    def introduce(self):
        print(f"And in the other corner, we have, the mighty, the powerful, {self.name}!!!!")