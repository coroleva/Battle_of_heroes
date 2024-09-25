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
        return self.health > 0  # если здоровье больше нуля, то герои живы (True)


class PlayerHero(Hero):
    def __init__(self, name, health, attack_power):
        super().__init__(name, health, attack_power)
        self.armor = random.randint(1, 10)  # Защита (случайное число от 1 до 10)

    def attack(self, enemy):
        damage = self.attack_power - enemy.armor
        if damage < 0:
            damage = 0
        enemy.health -= damage
        print(f"{self.name} атакует {enemy.name} и наносит {damage} урона.")

    def info(self):
        print(f"Имя: {self.name}\nЗдоровье: {self.health}\nСила атаки: {self.attack_power}\nЗащита: {self.armor}")

    def special_ability(self, enemy):
        pass


class Knight(PlayerHero):
    def special_ability(self, enemy):
        """Увеличивает защиту на один ход"""
        self.armor += 10
        print(f"{self.name} использует специальную способность! Защита увеличена на один ход.")


class Mage(PlayerHero):
    def special_ability(self, enemy):
        """Восстанавливает 20 здоровья"""
        heal = 20
        self.health += heal
        print(f"{self.name} использует специальную способность! Восстанавливает {heal} здоровья.")


class Archer(PlayerHero):
    def special_ability(self, enemy):
        """Критический выстрел, удваивающий урон"""
        crit_damage = self.attack_power * 2
        enemy.health -= crit_damage
        print(f"{self.name} использует специальную способность! Критический урон: {crit_damage}.")


class ComputerHero(Hero):
    def __init__(self, name, health, attack_power):
        super().__init__(name, health, attack_power)
        self.armor = random.randint(1, 10)  # Защита (случайное число от 1 до 10)

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
        while True:
            print("\nМеню:")
            print("1. Начать игру")
            print("2. Выйти")
            choice = input("Выберите действие: ")

            if choice == '1':
                self.create_heroes()  # вызов функции создания героев
                self.battle()  # вызов функции битвы
            elif choice == '2':
                print("Выход из игры.")
                break
            else:
                print("Неверный ввод. Попробуйте снова.")

    def create_heroes(self):  # функция создания героев
        # Выбор героя для игрока
        print("\nВыберите своего героя:")
        heroes = {
            "1": Knight("Рыцарь", health=100, attack_power=20),
            "2": Mage("Маг", health=80, attack_power=30),
            "3": Archer("Лучник", health=90, attack_power=25)
        }

        for key, hero in heroes.items():
            print(f"{key}. {hero.name} (Здоровье: {hero.health}, Атака: {hero.attack_power})")

        player_choice = input("Введите номер вашего героя: ")
        while player_choice not in heroes:
            player_choice = input("Неверный выбор. Введите номер вашего героя: ")

        self.player = heroes[player_choice]
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
            action = input("Выберите действие: 1 - Атака, 2 - Способность: ")
            if action == '1':
                self.player.attack(self.computer)
            elif action == '2':
                self.player.special_ability(self.computer)
            else:
                print("Неверное действие. Пропуск хода.")

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
