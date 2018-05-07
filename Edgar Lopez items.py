class Item(object):
    def __init__(self, name):
        self.name = name

    def name(self):
        print("You have %s" % self.name)


class Consumable(Item):
    def __init__(self, name, perks):
        super(Consumable, self).__init__(name)
        self.perks = perks

    def name (self):
        print("You drink %s" % self.name)

class speed_cola(Consumable):
    def __init__(self, name, perks):
        super(Consumable, self).__init__(name)
        self.perks = perks

    def name (self):
        print("You drink %s to get more speed" % self.name)


class jerganaut(Consumable):
    def __init__(self, name, perks):
        super(Consumable, self).__init__(name)
        self.perks = perks

    def name (self):
        print("You drink %s to take more hits" % self.name)

class double_tap(Consumable):
    def __init__(self, name, perks):
        super(Consumable, self).__init__(name)
        self.perks = perks

    def name (self):
        print("You drink %s to fast reload" % self.name)


class Wearable(Item):
    def __init__(self, name, cloth):
        super(Wearable, self).__init__(name)
        self.cloth = cloth

    def name(self):
        print("You where cloth %s" % self.name)


class Helmet(Wearable):
    def __init__(self, name):
        super(Helmet, self).__init__(name)

    def protection(self):
        print("My %s has a lot of protection for my head" % self.name)


class Shoes(Wearable):
    def __init__(self, name):
        super(Shoes, self).__init__(name)

    def laces(self):
        print("Makes me take more %s hits" % self.name)


class Shirt(Wearable):
    def __init__(self, name):
        super(Shirt, self).__init__(name)

    def brand(self):
        print("Makes me have more %s damage" % self.name)

class Weapons(Item):
    def __init__(self, name, attack, weapons):
        super(Weapons, self).__init__(name)
        self.weapons = weapons
        self.attack = attack

    def attack(self):
        print("You haved attack a zombie")


class Thunder_Gun(Weapons):
    def __init__(self, name, attack):
        super(Weapons, self).__init__('Thunder_Gun', 100)
        self.attack = attack

class Ray_Gun(Weapons):
    def __init__(self, name, attack):
        super(Weapons, self).__init__('Ray_Gun', 100)
        self.attack = attack.class Item(object):
    def __init__(self, name):
        self.name = name

    def name(self):
        print("You have %s" % self.name)


class Consumable(Item):
    def __init__(self, name, perks):
        super(Consumable, self).__init__(name)
        self.perks = perks

    def name (self):
        print("You drink %s" % self.name)

class speed_cola(Consumable):
    def __init__(self, name, perks):
        super(Consumable, self).__init__(name)
        self.perks = perks

    def name (self):
        print("You drink %s to get more speed" % self.name)


class jerganaut(Consumable):
    def __init__(self, name, perks):
        super(Consumable, self).__init__(name)
        self.perks = perks

    def name (self):
        print("You drink %s to take more hits" % self.name)

class double_tap(Consumable):
    def __init__(self, name, perks):
        super(Consumable, self).__init__(name)
        self.perks = perks

    def name (self):
        print("You drink %s to fast reload" % self.name)


class Wearable(Item):
    def __init__(self, name, cloth):
        super(Wearable, self).__init__(name)
        self.cloth = cloth

    def name(self):
        print("You where cloth %s" % self.name)


class Helmet(Wearable):
    def __init__(self, name):
        super(Helmet, self).__init__(name)

    def protection(self):
        print("My %s has a lot of protection for my head" % self.name)


class Shoes(Wearable):
    def __init__(self, name):
        super(Shoes, self).__init__(name)

    def laces(self):
        print("Makes me take more %s hits" % self.name)


class Shirt(Wearable):
    def __init__(self, name):
        super(Shirt, self).__init__(name)

    def brand(self):
        print("Makes me have more %s damage" % self.name)

class Weapons(Item):
    def __init__(self, name, attack, weapons):
        super(Weapons, self).__init__(name)
        self.weapons = weapons
        self.attack = attack

    def attack(self):
        print("You haved attack a zombie")


class Thunder_Gun(Weapons):
    def __init__(self, name, attack):
        super(Weapons, self).__init__('Thunder_Gun', 100)
        self.attack = attack

class Ray_Gun(Weapons):
    def __init__(self, name, attack):
        super(Weapons, self).__init__('Ray_Gun', 100)
        self.attack = attack