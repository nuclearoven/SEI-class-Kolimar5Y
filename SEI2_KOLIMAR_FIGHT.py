import random
print("pick between: Strike, Block, Charge")
print("GO!!")
charge = 0
oppCharge = 0
firstMove = True
def move():
    global charge
    global oppCharge
    global firstMove
    #your move
    you = (input("Your move:"))
    if you == "strike" or you == "Strike":
        if charge == 0:
            you = (input("Your strike is not charged"))
        else:
            a = 0
            charge -= 1
    if you == "block" or you == "Block":
        a = 1
    if you == "charge" or you == "Charge":
        a = 2
        charge += 1
    #opponent move
    if firstMove == False:
        opponent = random.randint(0, 2)
    else:
        opponent = 2
        firstMove = False

    if opponent == 0 and oppCharge == 0:
        opponent = random.randint(1, 2)
    if opponent == 2:
        oppCharge += 1
    #outcomes
    if a == 0 and charge >= 0:
        if opponent == 0:
            print("TIE, you both strike at the same time")
        if opponent == 1:
            print("NOTHING, your opponent blocked your strike, charges left:" + str(charge))
            return move()
        if opponent == 2:
            print("WIN, You struck while your opponent was charging")
    if a == 1:
        if opponent == 0:
            print("NOTHING, you blocked your opponent’s strike")
        if opponent == 1:
            print("NOTHING, you both block")
        if opponent == 2:
            print("NOTHING, your opponent was charging")
        return move()
    if a == 2:
        if opponent == 0:
            print("LOSE, your got struck while charging")
        if opponent == 1:
            print("NOTHING, you charged successfully, charges left:" + str(charge))
            return move()
        if opponent == 2:
            print("NOTHING, you both charged successfully, charges left:" + str(charge))
            return move()
move()