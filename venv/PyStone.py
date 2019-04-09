from random import randint
import Scripts
import Description
class card:
    str=0
    hp=0
    bc=""
    ds=False
    ch=False
def baffs():
    #todo написать баффы
    pass

deck1=[]
deck2=[]
arm1=[]
arm2=[]
table1=[]
table2=[]

#инициализация колод
f=open("deck1.txt")
for i in f:
    deck1.append(card())
    [deck1[-1].str,deck1[-1].hp,deck1[-1].bc,deck1[-1].ds,deck1[-1].ch]=i.split()
    deck1[-1].str=int(deck1[-1].str)
    deck1[-1].hp=int(deck1[-1].hp)
f.close()
f=open("deck2.txt")
for i in f:
    deck2.append(card())
    [deck2[-1].str,deck2[-1].hp,deck2[-1].bc,deck2[-1].ds,deck2[-1].ch]=i.split()
    deck2[-1].str=int(deck2[-1].str)
    deck2[-1].hp=int(deck2[-1].hp)
f.close()

#false - 1, true -2
for i in range(3):
    arm1.append(deck1.pop(randint(0,len(deck1)-1)))
    arm2.append(deck2.pop(randint(0, len(deck2) - 1))) # 3 рандомных карты в руку
turn=bool(randint(0,1))
face1=face2=30
while face1*face2>0:
    if turn:
        table=table2
        arm=arm2
        deck=deck2
        entable=table1
        enarm=arm1
    else:
        table=table1
        arm=arm1
        deck=deck1
        entable=table2
        enarm=arm2
    Description.screen(arm,table,entable,enarm)
    inp=Scripts.select("'pass' to pass the turn,'cast' to cast the card or 'attack' to attack with casted card\n",-1,["pass","cast","attack"])
    if inp=="pass":
        turn = not turn
    elif inp=="cast":
        inp=Scripts.select("select number of card to cast or 'cancel'\n", len(arm),["cancel",])
        if inp=="cancel":
            pass
        else:
            table.append(arm.pop(inp))
    elif inp=="attack":
        inp = Scripts.select("select number of card to attack with or 'cancel'\n", len(table), ["cancel", ])
        if inp=="cancel":
            pass
        else:
            inp2=Scripts.select("select number of enemy card to attack it or 'cancel'\n", len(entable), ["cancel", ])
            if inp2 == "cancel":
                pass
            else:
                entable[inp2].hp-=table[inp].str
                table[inp].hp-=entable[inp2].str
                if entable[inp2].hp<=0:
                    entable.pop(inp2)
                if table[inp].hp<=0:
                    pass