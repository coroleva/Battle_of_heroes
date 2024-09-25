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
    def __init__(self, name, health, attack_power):
        super().__init__(name, health, attack_power)
        self.armor = random.randint(1, 10) # Защита (случайное число от 1 до 10)

    def attack(self, enemy):
        damage = self.attack_power - enemy.armor
        if damage < 0:
            damage = 0
        enemy.health -= damage
        print(f"{self.name} атакует {enemy.name} и наносит {damage} урона.")

    def info(self):
        print(f"Имя: {self.name}\nЗдоровье: {self.health}\nСила атаки: {self.attack_power}\nЗащита: {self.armor}")



class ComputerHero(Hero):
    def __init__(self, name, health, attack_power):
        super().__init__(name, health, attack_power)

    def attack(self, enemy):
        damage = self.attack_power
        enemy.health -= damage
        print(f"{self.name} атакует {enemy.name} и наносит {damage} урона.")

    def info(self):
        print(f"Имя: {self.name}\nЗдоровье: {self.health}\nСила атаки: {self.attack_power}")

class Game:
    pass

def battle(player, computer):
    pass




