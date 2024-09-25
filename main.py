import random
class Hero:
    def __init__(self, name, health, damage):
        self.name = name  # Имя героя
        self.health = health  # Здоровье
        self.damage = damage  # Урон

    def info(self):
        print(f"Name: {self.name}\nHealth: {self.health}\nDamage: {self.damage}\nDefence: {self.defence}")
    def attack(self, enemy):
        enemy.health -= self.damage
        print(f"{self.name} атакует {enemy.name} и наносит {self.damage} урона.")
class PlayerHero(Hero):
    pass

class ComputerHero(Hero):
    pass

def battle(player, computer):
    pass



player = PlayerHero("Player", 100, 10)
computer = ComputerHero("Computer", 100, 10)

battle(player, computer)
