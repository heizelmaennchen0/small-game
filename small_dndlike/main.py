import random
import mage
import warrior

schleife1 = True
while schleife1 :
    print("Player 1 choose your character")
    print("01 = warrior")
    print("02 = mage")
    print("03 = assasin") 
    choice = input()
    choice_int = int (choice)
    if choice_int == 1 :
        player1 = warrior.CWarrior
        break
    elif choice_int == 2 :
        player1 = mage.CMage
        break
    elif choice_int == 3 :
        exit
    else : 
        print("wrong input")

while schleife1 :
    print("Player 2 choose your character")
    print("01 = warrior")
    print("02 = mage")
    print("03 = assasin") 
    choice = input()
    choice_int = int (choice)
    if choice_int == 1 :
        player2 = warrior.CWarrior
        break
    elif choice_int == 2 :
        player2 = mage.CMage
        break
    elif choice_int == 3 :
        exit
    else : 
        print("wrong input")

       
def scoreboard() :
    print("1    player    2")
    print("----",player1.get_life(player1),"    life   ", player2.get_life(player2))
    print("----",player1.get_mana(player1),"    mana   ", player2.get_mana(player2))
    print("----",player1.get_initiative(player1),"    initiative   ", player2.get_initiative(player2))



if (player2.get_initiative(player2) > player1.get_initiative(player2) ) :
    player_turn = False
elif (player2.get_initiative == player1.get_initiative ) :
    a = random.randint(1,2)
    if a == 1 :
        player_turn = True
    else :
        player_turn = False
else :
    player_turn = True


while (player1.get_life(player1) > 0 and player2.get_life(player2) > 0 ) :
    damage = int
    scoreboard()
    if player_turn :
        print("player 1 choose the ability you want to use")
        player1.ability_screen()
        choice = input()
        choice_int = int(choice)
        if choice_int == 1 :
            damage = int(player1.ability1(player1))
            player2.set_life(player2, player2.get_life(player2) - damage)
            player_turn = False
        elif choice_int == 2 :
            player1.ability2(player1)
            player2.set_life(player2, player2.get_life(player2) - damage)
            player_turn = False
        else :
            print("no ability used")
        player_turn = False
    else :
        print("player 1 choose the ability you want to use")
        player2.ability_screen()
        choice = input()
        choice_int = int(choice)
        if choice_int == 1 :
            player2.ability1(player2)
            player1.set_life(player1, player1.get_life(player1) - damage)
            player_turn = False
        elif choice_int == 2 :
            player2.ability2(player2)
            player1.set_life(player1, player1.get_life(player1) - damage)
            player_turn = False
        else :
            break
        player_turn = True


print("game ended")
exit()
