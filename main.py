"""
Простая игра
"""

from abc import ABC, abstractmethod

#Шаг 1: Создание абстрактного класса для оружия
class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass

# Шаг 2: Реализация конкретных типов оружия
class Sword(Weapon):
    def attack(self):
        return "Боец наносит удар мечом."


class Bow(Weapon):
    def attack(self):
        return "Боец наносит удар из лука."


 # Шаг 3: Модификация класса Fighter
class Fighter:
    def __init__(self, weapon: Weapon):
        self.weapon = weapon

    def attack(self):
        print(self.weapon.attack())

    def changeWeapon(self, new_weapon: Weapon):
        self.weapon = new_weapon

# Шаг 4: Класс Monster и Реализация боя
class Monster:
    # В рамках примера детали класса Monster могут быть пропущены
    pass

# Функция для боя между бойцом и монстром
def fight(fighter, monster):
    fighter.attack()
    print("Монстр побежден!")


def main():
    # Создание оружия
    sword = Sword()
    bow = Bow()

    # Создание бойца с мечом
    fighter = Fighter(sword)
    monster = Monster()  # Создание монстра

    print("Боец выбирает меч.")
    fight(fighter, monster)

    # Смена оружия на лук
    print("\nБоец выбирает лук.")
    fighter.changeWeapon(bow)
    fight(fighter, monster)


if __name__ == "__main__":
    main()
