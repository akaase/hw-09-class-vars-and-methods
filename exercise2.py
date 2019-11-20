class Vampire:
    coven = []

    def __init__(self, name, age, in_coffin=True, drank_blood_today=True):
        self.name = name
        self.age = age
        self.in_coffin = True
        self.drank_blood_today = True

    def go_home(self):
        self.in_coffin = True

    def drink_blood(self):
        self.drank_blood_today = True

    @classmethod
    def create(cls, name, age, in_coffin=True, drank_blood_today=True):
        v = Vampire(name, age, in_coffin, drank_blood_today)
        cls.coven.append(v)
        return v

    @classmethod
    def sunset(cls):
        for vampire in cls.coven:
            vampire.in_coffin = False
            vampire.drank_blood_today = False

    @classmethod
    def sunrise(cls):
        # Be careful here not to modify a list while iterating through it!
        # You have to create a new list instead
        alive = []
        for vampire in cls.coven:
            if vampire.in_coffin and vampire.drank_blood_today:
                alive.append(vampire)
        cls.coven = alive

def main():
    riley = Vampire.create('Riley', 25)
    alice = Vampire.create('Alice', 24)
    jasper = Vampire.create('Jasper', 23)
    renesmee = Vampire.create('Renesmee', 25)
    marcus = Vampire.create('Marcus', 28)
    zafrina = Vampire.create('Zafrina', 49)
    demetri = Vampire.create('Demetri', 28)

    print('Coven at the beginning:')
    for vampire in Vampire.coven:
        print(vampire.name)

    Vampire.sunset()
    riley.drink_blood()
    riley.go_home()
    jasper.drink_blood()
    renesmee.drink_blood()
    renesmee.go_home()
    marcus.go_home()
    Vampire.sunrise() # Should remove all vampires except 'Riley' and 'Renesmee'

    print('Coven at the end:')
    for vampire in Vampire.coven:
        print(vampire.name) #--> 'Riley', 'Renesmee'

main()
