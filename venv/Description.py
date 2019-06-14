from os import system
def spl(s): #кажется мне это не нужно но я это пока оставлю
    l=[]
    for i in range(len(s)//8):
        l.append(s[i*8:8*(i+1)])
    if len(s)%8!=0:
        l.append(s[len(s)-len(s)%8:])
    return l
def screen(arm,table,entable,enarm,face,enface):
    system("cls")
    print("/"+"~"*(len(enarm)*10-2 if enarm else 8)+"\\")
    print("|",(len(enarm)*10-2 if enarm else 8)//2*" ",enface[0],((len(enarm)*10-2 if enarm else 8)-(len(enarm)*10-2 if enarm else 8)//2-len(str(enface[0])))*" ","|",sep="")
    print("\\" + "~" * (len(enarm) * 10 - 2 if enarm else 8) + "/")
    for i in range(len(enarm)):
        print("   ",i," "*(5-len(str(i))),end="")
    print()
    for _ in enarm:
        print("/--------\\",end="")
    print()
    for _ in enarm:
        print("|????????|" , sep="", end="")
    print()
    for _ in enarm:
        print("\\--------/",end="")
    print()

    print("-"*10*max(len(enarm),len(entable)))

    for i in range(len(entable)):
        print("   ",i," "*(5-len(str(i))),end="")
    print()
    for _ in entable:
        print("/--------\\",end="")
    print()
    for _ in entable:
        print("|hp   str|",end="")
    print()
    for i in entable:
        print("|", i.hp, " " * (8 - len(str(i.hp)) - len(str(i.str))), i.str, "|" , sep="", end="")
    print()
    for _ in entable:
        print("\\--------/",end="")
    print()

    print("="*10*max(len(arm),len(enarm)))

    for i in range(len(table)):
        print("   ",i," "*(5-len(str(i))),end="")
    print()
    for _ in table:
        print("/--------\\",end="")
    print()
    for _ in table:
        print("|hp   str|",end="")
    print()
    for i in table:
        print("|", i.hp, " " * (8 - len(str(i.hp)) - len(str(i.str))), i.str, "|" , sep="", end="")
    print()
    for _ in table:
        print("\\--------/",end="")
    print()

    print("-"*10*max(len(arm),len(table)))

    print()
    for i in range(len(arm)):
        print("   ",i," "*(5-len(str(i))),end="")
    print()
    for _ in arm:
        print("/--------\\",end="")
    print()
    for _ in arm:
        print("|hp   str|",end="")
    print()
    for i in arm:
        print("|", i.hp, " " * (8 - len(str(i.hp)) - len(str(i.str))), i.str, "|" , sep="", end="")
    print()
    for _ in arm:
        print("\\--------/",end="")
    print()
    print("/" + "~" * (len(arm) * 10 - 2 if arm else 8) + "\\")
    print("|", (len(arm) * 10 - 2 if arm else 8) // 2 * " ", face[0], ((len(arm) * 10 - 2 if arm else 8) - (len(arm) * 10 - 2 if arm else 8) // 2 - len(str(face[0]))) * " ", "|", sep="")
    print("\\" + "~" * (len(arm) * 10 - 2 if arm else 8) + "/")
    print()