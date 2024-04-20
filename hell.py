import random
import combat

def flip_coin():
    flip = random.randint(0,1)
    if flip == 1:
        print("Heads")
    else:
        print("Tails")

def roll(type):
    if type == "d8":
        roll = random.randint(0,7)
        print ("Rolled d8: " + str(roll+1))
    elif type == "d4":
        roll = random.randint(0,3)
        print ("Rolled d4: " + str(roll+1))
    elif type == "d6":
        roll = random.randint(0,5)
        print ("Rolled d6: " + str(roll+1))
    elif type == "d10":
        roll = random.randint(0,9)
        print ("Rolled d10: " + str(roll+1))
    elif type == "d20":
        roll = random.randint(0,19)
        print ("Rolled d20: " + str(roll+1))
    elif type == "d100":
        roll = random.randint(0,99)
        print ("Rolled d: " + str(roll+1))

def find_shop_item():
    shopItems = open("textFiles/shopItems.txt", "r")
    lines = shopItems.readlines()

    line_number = random.randint(0,len(lines)-1)

    item = lines[line_number]
    print('''
--Price Guide--
Shop Items: 15 Coins
Attack Voucher: 15 Coins
Regular Item: 10 Coins
          ''')
    print("--Shop Item--")
    print(item.strip() + "\n")
    shopItems.close()


def find_attackVoucher():
    attackVouchers = open("textFiles/attackVouchers.txt", "r")
    lines = attackVouchers.readlines()
    
    line_number = random.randint(0,len(lines)-1)

    item = lines[line_number]

    print("--Attack Voucher--")
    print(item.strip() + "\n")
    attackVouchers.close()

def find_greatAttackVoucher():
    attackVouchers = open("textFiles/greatAttackVouchers.txt", "r")
    lines = attackVouchers.readlines()
    
    line_number = random.randint(0,len(lines)-1)

    item = lines[line_number]

    print("--Great Attack Voucher--")
    print(item.strip() + "\n")
    attackVouchers.close()

def find_all_attackVoucher():
    gAttackVouchers = open("textFiles/greatAttackVouchers.txt", "r")
    attackVouchers = open("textFiles/attackVouchers.txt", "r")

    lines = attackVouchers.readlines() + gAttackVouchers.readlines()

    line_number = random.randint(0,len(lines)-1)

    item = lines[line_number]

    print("--New Attack Voucher--")
    print(item.strip() + "\n")
    attackVouchers.close()
    gAttackVouchers.close()


def find_regular_items(num):
    regItemArray = []
    tempArray = []
    regItems = open("textFiles/regItems.txt", "r")
    lines = regItems.readlines()
    print("--Regular Items--")
    while len(tempArray) < num:
        line_number = random.randint(0,len(lines)-1)
        item = lines[line_number]
        regItemArray.append(item)
        for reg in regItemArray:
            if reg not in tempArray:
                tempArray.append(item) 

    regItemArray = tempArray
    for regItem in regItemArray:
        print(regItem.strip())
    regItems.close()
    
def grab_token():
    tokens = open("textFiles/tokens.txt", "r")
    lines = tokens.readlines()
    
    line_number = random.randint(0,len(lines)-1)

    token = lines[line_number]

    print("--New Token--")
    print(token.strip() + "\n")
    tokens.close()

def find_attribute():
    attr = open("textFiles/attributes.txt", "r")
    lines = attr.readlines()
    
    line_number = random.randint(0,len(lines)-1)

    item = lines[line_number]

    print("--New Attribute--")
    print(item.strip() + "\n")
    attr.close()

def main():
    print("")
    print("Type cmds for a list of commands")
    choice = input("What would you like to do: ") 
    print("")
    match choice:
        case "coin":
            flip_coin()
            main()
        case "roll":
            d = input("Dice type (d4, d6, d8, d10, d20, d100): ")
            roll(d)
            main()
        case "shop":
            vibeCheck = input("Good(g), Bad(b), or No(n) Vibes?: ")
            find_shop_item()
            find_attackVoucher()
            if vibeCheck == "n":
                find_regular_items(5)
            elif vibeCheck == "g":
                find_regular_items(6)
            elif vibeCheck == "b":
                find_regular_items(4)
            
            main()
        case "combat":
            contract = input("Does player posses a contract?(none, challenger, coward): ")
            combat.gen_difficulty(contract)
            main()
        case "wit":
            diff = input("Player Wits stat: ")
            combat.gen_wit_combat(int(diff))
            print("")
            roll("d8")
            main()
        case "elite":
            combat.gen_elite_combat()
            main()
        case "trivial":
            print("")
            print("--Trivial Monster--")
            combat.gen_combat_encounter("textFiles/monster_stats/trivialStats.txt", "textFiles/monster_names/trivialMonsters.txt")
            main()
        case "item":
            find_regular_items(1)
            main()
        case "token":
            grab_token()
            main()
        case "attr":
            find_attribute()
            main()
        case "atk":
            find_attackVoucher()
            main()
        case "gatk":
            find_greatAttackVoucher()
            main()
        case "aatk":
            find_all_attackVoucher()
            main()
        case "cmds":
            print('''
                --------------------------------------------------------------------------------------
                cmds: shows a list of commands
                --------------------------------------------------------------------------------------
                coin: flips a coin
                --------------------------------------------------------------------------------------
                roll: rolls choice of d4, d6, d8, d10, d20, and d100
                --------------------------------------------------------------------------------------
                shop: generates a shop inventory
                --------------------------------------------------------------------------------------
                combat: generates a combat encounter
                --------------------------------------------------------------------------------------
                wit: generates a Battle of Wits encounter
                --------------------------------------------------------------------------------------
                item: generates one random item
                --------------------------------------------------------------------------------------
                token: generates one random token
                --------------------------------------------------------------------------------------
                atk: generates one random attack voucher
                --------------------------------------------------------------------------------------
                gatk: generates one random great attack voucher
                --------------------------------------------------------------------------------------
                aatk: generates one random attack voucher from regualr and great lists
                --------------------------------------------------------------------------------------
                attr: generates one random attribute
                --------------------------------------------------------------------------------------
                elite: generates 3 elite attributes and a random elite combat encounter
                --------------------------------------------------------------------------------------
                  ''')
            main()
        case "exit":
            exit()
        case _:
            main()

main()

