import random
class Hero:
    def __init__(self, name, health, attack_power):
        self.name = name  # Имя героя
        self.health = health  # Здоровье
        self.attack_power = attack_power  # сила атаки

    def info(self):
        print(f"Имя: {self.name}\nЗдоровье: {self.health}\nСила атаки: {self.attack_power}")
    def attack(self, enemy):
        enemy.health -= self.attack_power
        print(f"{self.name} атакует {enemy.name} и наносит {self.attack_power} урона.")
    def is_alive(self):
        return self.health > 0   # если здоровье больше нуля, то герои живы (True)

class PlayerHero(Hero):
    pass

class ComputerHero(Hero):
    pass

class Game:
    pass

def battle(player, computer):
    pass




