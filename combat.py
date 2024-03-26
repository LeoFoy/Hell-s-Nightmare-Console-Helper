import random

#conjures a random number, based on that number certain parameters are input into the combat generation function
def gen_difficulty(contract):
    r = random.randint(0,100)

    #sets difficulty odds
    if contract == "none":
        difficultyArray = [10, 55, 85, 95, 100]
    elif contract == "challenger":
        difficultyArray = [5, 15, 45, 85, 100]
    elif contract == "coward":
        difficultyArray = [25, 75, 95, 100, 101]
        
    if r <=difficultyArray[0]:
        #Trivial
        print("")
        print("--Trivial Monster--")
        gen_combat_encounter("textFiles/monster_stats/trivialStats.txt", "textFiles/monster_names/trivialMonsters.txt")
    elif r <= difficultyArray[1]:
        #Common
        print("")
        print("--Common Monster--")
        gen_combat_encounter("textFiles/monster_stats/commonStats.txt", "textFiles/monster_names/commonMonsters.txt")
    elif r<= difficultyArray[2]:
        #Potent
        print("")
        print("--Potent Monster--")
        gen_combat_encounter("textFiles/monster_stats/potentStats.txt", "textFiles/monster_names/potentMonsters.txt")
    elif r<= difficultyArray[3]:
        #Dangerous
        print("")
        print("--Dangerous Monster--")
        gen_combat_encounter("textFiles/monster_stats/dangerousStats.txt", "textFiles/monster_names/dangerousMonsters.txt")
    elif r<=difficultyArray[4]:
        #Elite
        print("")
        gen_elite_combat()

#reads given monster files and outputs a random monster 
def gen_combat_encounter(stats, names):
    i = 0
    monsterStats = open(stats, "r")
    statBlocks = monsterStats.readlines()
    monsters = open(names, "r")
    monsterNames = monsters.readlines()

    line_number = random.randint(0,len(monsterNames)-1)

    mon = monsterNames[line_number]

    for m in statBlocks:
        if mon.strip() == m.strip():
            index = statBlocks.index(m)
            break
    
    while statBlocks[index+i].strip() != "~":
        print(statBlocks[index+i].strip())
        i+=1
    monsterStats.close()
    monsters.close()

#generates a Battle of Wits using the combat generation function
def gen_wit_combat(diff):
    if diff <= 2:
        print("")
        print("--Braindead Battle of Wits--")
        gen_combat_encounter("textFiles/wits_stats/braindeadStats.txt","textFiles/witOpp_names/braindeadOppenents.txt")
    elif diff <= 6:
        print("")
        print("--Average Battle of Wits--")
        gen_combat_encounter("textFiles/wits_stats/averageStats.txt","textFiles/witOpp_names/averageOppenents.txt")
    elif diff <= 9:
        print("")
        print("--Smart Battle of Wits--")
        gen_combat_encounter("textFiles/wits_stats/smartStats.txt","textFiles/witOpp_names/smartOppenents.txt")
    elif diff <= 11: 
        print("")
        print("--Genius Battle of Wits--")
        gen_combat_encounter("textFiles/wits_stats/geniusStats.txt","textFiles/witOpp_names/geniusOppenents.txt")
    elif diff >= 12:
        print("")
        print("--Elite Battle of Wits--")
        gen_combat_encounter("textFiles/wits_stats/witsEliteStats.txt","textFiles/witOpp_names/eliteOppenents.txt")


def gen_elite_combat():
    attributeArray = []
    tempArray = []
    eliteAttr = open("textFiles/eliteAttributes.txt", "r")
    attributes = eliteAttr.readlines()
    print("--Elite Attributes--")
    while len(tempArray) < 3:
        line_number = random.randint(0,len(attributes)-1)
        item = attributes[line_number]
        attributeArray.append(item)
        for a in attributeArray:
            if a not in tempArray:
                tempArray.append(item) 

    attributeArray = tempArray
    for a in attributeArray:
        print(a.strip())
    eliteAttr.close()

    print("")
    print("--Elite Monster--")
    gen_combat_encounter("textFiles/monster_stats/eliteStats.txt","textFiles/monster_names/eliteMonsters.txt")