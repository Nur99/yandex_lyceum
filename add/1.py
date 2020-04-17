class Weapon:
    def __init__(self, name, damage, range):
        self.name = name
        self.damage = damage
        self.range = range

    def hit(self, actor, target):
        if not target.is_alive():
            print('Враг уже повержен')
            return
        coords1 = actor.get_coords()
        coords2 = target.get_coords()
        distance = ((coords1[0] - coords2[0]) ** 2 + (coords1[1] - coords2[1]) ** 2) ** 0.5
        if self.range >= distance:
            target.get_damage(self.damage)
            print(f'Врагу нанесен урон оружием {self.name} в размере {self.damage}')
        else:
            print(f'Враг слишком далеко для оружия {self.name}')

    def __str__(self):
        return self.name


class BaseCharacter:
    def __init__(self, pos_x, pos_y, hp):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.hp = hp
        self.alive = True

    def move(self, delta_x, delta_y):
        self.pos_x += delta_x
        self.pos_y += delta_y

    def is_alive(self):
        return self.alive

    def get_damage(self, amount):
        self.hp -= amount
        if self.hp < 0:
            self.alive = False

    def get_coords(self):
        return self.pos_x, self.pos_y


class BaseEnemy(BaseCharacter):
    def __init__(self, pos_x, pos_y, weapon, hp):
        self.weapon = weapon
        super().__init__(pos_x, pos_y, hp)

    def hit(self, target):
        if isinstance(target, MainHero):
            self.weapon.hit(self, target)
        else:
            print('Могу ударить только Главного героя')

    def __str__(self):
        return f"Враг на позиции {self.get_coords()} с оружием {self.weapon}"


class MainHero(BaseCharacter):
    def __init__(self, pos_x, pos_y, name, hp):
        self.name = name
        self.weapons = []
        self.curr_weapon_index = None
        super().__init__(pos_x, pos_y, hp)

    def hit(self, target):
        if not self.weapons:
            print("Я безоружен")
        elif not isinstance(target, BaseEnemy):
            print("Могу ударить только врага")
        else:
            self.weapons[self.curr_weapon_index].hit(self, target)

    def add_weapon(self, weapon):
        if isinstance(weapon, Weapon):
            self.weapons.append(weapon)
            print(f"Подобрал {weapon}")
            if self.curr_weapon_index is None:
                self.curr_weapon_index = 0
        else:
            print(f"Это не оружие")

    def next_weapon(self):
        if not self.weapons:
            print("Я безоружен")
        elif len(self.weapons) == 1:
            print('У меня только одно оружие')
        else:
            self.curr_weapon_index += 1
            if self.curr_weapon_index >= len(self.weapons):
                self.curr_weapon_index = 0
            print(f"Сменил оружие на {self.weapons[self.curr_weapon_index]}")

    def heal(self, amount):
        hp = self.hp
        self.hp = min(200, hp + amount)
        print(f'Полечился, теперь здоровья {self.hp}')
