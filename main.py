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
        self.armor = random.randint(1, 10) # Защита (случайное число от 1 до 10)

    def attack(self, enemy):
        damage = self.attack_power - enemy.armor
        if damage < 0:
            damage = 0
        enemy.health -= damage
        print(f"{self.name} атакует {enemy.name} и наносит {damage} урона.")

    def info(self):
        print(f"Имя: {self.name}\nЗдоровье: {self.health}\nСила атаки: {self.attack_power}\nЗащита: {self.armor}")

class Game:
    def __init__(self):
        self.player = None
        self.computer = None

    def start(self):
        print("Добро пожаловать в игру 'Битва героев'!")
        self.create_heroes() # вызов функции создания героев
        self.battle()        # вызов функции битвы

    def create_heroes(self):   # функция создания героев
        # Создание героя для игрока
        player_name = input("Введите имя вашего героя: ")
        self.player = PlayerHero(player_name, health=100, attack_power=random.randint(10, 20))
        self.player.info()

        # Создание героя для компьютера
        computer_name = "Орк"
        self.computer = ComputerHero(computer_name, health=100, attack_power=random.randint(10, 20))
        self.computer.info()

    def battle(self):
        print("\nНачинается битва!")
        round_number = 1

        # Цикл битвы, пока оба героя живы
        while self.player.is_alive() and self.computer.is_alive():
            print(f"\n=== Раунд {round_number} ===")
            # Ход игрока
            self.player.attack(self.computer)
            if self.computer.is_alive():
                # Ход компьютера, если он жив
                self.computer.attack(self.player)

            # Показать состояние здоровья героев после раунда
            print(f"\nСостояние после раунда {round_number}:")
            self.player.info()
            self.computer.info()

            round_number += 1

        # Определение победителя
        if self.player.is_alive():
            print(f"\n{self.player.name} победил!")
        else:
            print(f"\n{self.computer.name} победил!")


if __name__ == "__main__":
    game = Game()
    game.start()





