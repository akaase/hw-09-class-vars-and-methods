class Vampire:
    ???
    
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
