import random

cards_list = ["Sunset Sarsaparilla", "Blood Pack", "Nuka-Cola", "Stimpak",
"Antivenom", "RadAway", "Pipe Pistol", "Combat Shotgun", "Plasma Rifle",
"Gatling Laser", "Super Sledge", "Fat Man", "Metal Armor", "Leather Armor",
"Combat Armor", "Power Armor Frame", "Assault Marine Armor",
"X-01 Power Armor", "EMP Grenade", "Plasma Pistol", "Pulse Grenade",
"Railway Rifle", "Plasma Caster", "Tesla Cannon", "Buffout", "Psycho",
"Grape Mentats", "Overdrive", "Psycho Buff", "Fury", "Flashbang Grenade",
"Plasma Grenade", "Cryolator", "Alien Blaster", "Experimental MIRV",
"Plasma Defender"]

computer_health = 1000
user_health = 1000
computer_strength = 100
user_strength = 100
computer_defense = 0
user_defense = 0
computer_turn = False
user_turn = False

def deck_generator(cards_list):
    deck = []
    for card in cards_list:
        deck.extend([card] * 6)
    random.shuffle(deck)
    print("A new deck of cards is shuffled")
    return deck

def hand_generator(deck):
    computer_hand = deck[0:6]
    del deck[0:6]
    print("I took 6 cards! I\'m ready to start.")
    user_hand = deck[0:6]
    del deck[0:6]
    print("You took 6 cards! Are you ready to play now?")
    return computer_hand, user_hand

def beginner():
    global user_turn, computer_turn
    cap = random.choice(["left", "right"])
    print("I have a cap in one fist. if you can guess in wich one, you can"\
    f"\nbegin the game! if not, I\'ll start to play first.")
    while True:
        user_choice = input("Enter right for right hand and left"\
        "\nfor left hand\n").lower()
        if user_choice != "left" and user_choice != "right":
            print("invalid input! Please try again.")
            continue
        break
    print("I open my fists")
    if user_choice == cap:
        print(f"You were right! The cap was in my {cap} hand! go"\
        f"\nahead and play!")
        user_turn = True
    if user_choice != cap:
        print(f"You were wrong! The cap was in my {cap} hand! I'll"\
        f"\nplay now.")
        computer_turn = True

def health_booster(health_booster_num):
    global computer_health, user_health, computer_turn, user_turn
    health_booster_num += 100
    if computer_turn:
        computer_health = int(health_booster_num * computer_health / 100)
        print(f"My health increased by {health_booster_num - 100}%"\
        f"\nIt\'s {int(computer_health)} now!")
    if user_turn:
        user_health = int(health_booster_num * user_health / 100)
        print(f"Your health increased by {health_booster_num - 100}%"\
        f"\nIt\'s {int(user_health)} now!")

def attack(damage):
    global computer_health, user_health, computer_defense, user_defense
    global computer_strength, user_strength, computer_turn, user_turn
    defended = 0
    if computer_turn:
        damage = int(computer_strength * damage / 100)
        if user_defense < 100:
            defended = 100 - user_defense
            damage = int(damage * defended / 100)
        if user_defense >= 100:
            damage = 0
        user_health -= damage
        print(f"Your health decreaced by {damage} points!"\
        f"\nIt\'s {int(user_health)} now.")
    if user_turn:
        damage = int(user_strength * damage / 100)
        if computer_defense < 100:
            defended = 100 - computer_defense
            damage = int(damage * defended / 100)
        if computer_defense >= 100:
            damage = 0
        computer_health -= damage
        print(f"My health decreaced by {damage} points!"\
        f"\nIt\'s {int(computer_health)} now.")

def defense_booster(defense_booster_num):
    global computer_defense, user_defense, computer_turn, user_turn
    if computer_turn:
        computer_defense += defense_booster_num
        print(f"My defense increased by {defense_booster_num} points!"\
        f"\nIt\'s {int(computer_defense)} now.")
    if user_turn:
        user_defense += defense_booster_num
        print(f"Your defense increased by {defense_booster_num} points!"\
        f"\nIt\'s {int(user_defense)} now.")

def strength_booster(strength_booster_num):
    global computer_strength, user_strength, computer_turn, user_turn
    strength_booster_num += 100
    if computer_turn:
        computer_strength = int(computer_strength * strength_booster_num / 100)
        print(f"My strength increased by {strength_booster_num - 100}%!"\
        f"\nIt\'s {int(computer_strength)} now.")
    if user_turn:
        user_strength = int(user_strength * strength_booster_num / 100)
        print(f"Your strength increased by {strength_booster_num - 100}%!"\
        f"\nIt\'s {int(user_strength)} now.")

def defense_disruptor(defense_disruptor_num):
    global computer_defense, user_defense, computer_turn, user_turn
    if computer_turn:
        user_defense -= defense_disruptor_num
        print(f"Your defense decreased by {defense_disruptor_num} points!"\
        f"\nIt\'s {int(user_defense)} now.")
    if user_turn:
        computer_defense -= defense_disruptor_num
        print(f"My defense decreased by {defense_disruptor_num} points!"\
        f"\nIt\'s {int(computer_defense)} now.")

def strength_disruptor(strength_disruptor_num):
    global computer_strength, user_strength, computer_turn, user_turn
    strength_disruptor_num = 100 - strength_disruptor_num
    if computer_turn:
        user_strength = user_strength * strength_disruptor_num / 100
        print(f"Your strength decreaced by {100 - strength_disruptor_num}%!"\
        f"\nIt\'s {int(user_strength)} now.")
    if user_turn:
        computer_strength = computer_strength * strength_disruptor_num / 100
        print(f"My strength decreaced by {100 - strength_disruptor_num}%!"\
        f"\nIt\'s {int(computer_strength)} now.")

cards_action = {
    "Sunset Sarsaparilla": lambda: health_booster(9),
    "Blood Pack": lambda: health_booster(11),
    "Nuka-Cola": lambda: health_booster(15),
    "Stimpak": lambda: health_booster(24),
    "Antivenom": lambda: health_booster(25),
    "RadAway": lambda: health_booster(33),
    "Pipe Pistol": lambda: attack(60),
    "Combat Shotgun": lambda: attack(90),
    "Plasma Rifle": lambda: attack(150),
    "Gatling Laser": lambda: attack(220),
    "Super Sledge": lambda: attack(310),
    "Fat Man": lambda: attack(370),
    "Metal Armor": lambda: defense_booster(3),
    "Leather Armor": lambda: defense_booster(5),
    "Combat Armor": lambda: defense_booster(8),
    "Power Armor Frame": lambda: defense_booster(14),
    "Assault Marine Armor": lambda: defense_booster(15),
    "X-01 Power Armor": lambda: defense_booster(18),
    "EMP Grenade": lambda: defense_disruptor(5),
    "Plasma Pistol": lambda: defense_disruptor(11),
    "Pulse Grenade": lambda: defense_disruptor(17),
    "Railway Rifle": lambda: defense_disruptor(25),
    "Plasma Caster": lambda: defense_disruptor(31),
    "Tesla Cannon": lambda: defense_disruptor(41),
    "Buffout": lambda: strength_booster(2),
    "Psycho": lambda: strength_booster(8),
    "Grape Mentats": lambda: strength_booster(15),
    "Overdrive": lambda: strength_booster(20),
    "Psycho Buff": lambda: strength_booster(26),
    "Fury": lambda: strength_booster(32),
    "Flashbang Grenade": lambda: strength_disruptor(6),
    "Plasma Grenade": lambda: strength_disruptor(12),
    "Cryolator": lambda: strength_disruptor(15),
    "Alien Blaster": lambda: strength_disruptor(16),
    "Experimental MIRV": lambda: strength_disruptor(21),
    "Plasma Defender": lambda: strength_disruptor(27)
}

cards_discription = {
    "Sunset Sarsaparilla": "health booster: 9%",
    "Blood Pack": "health booster: 11%",
    "Nuka-Cola": "health booster: 15%",
    "Stimpak": "health booster: 24%",
    "Antivenom": "health booster: 25%",
    "RadAway": "health booster: 33%",
    "Pipe Pistol": "attack: 60 points default damage",
    "Combat Shotgun": "attack: 90 points default damage",
    "Plasma Rifle": "attack: 150 points default damage",
    "Gatling Laser": "attack: 220 points default damage",
    "Super Sledge": "attack: 310 points default damage",
    "Fat Man": "attack: 370 points default damage",
    "Metal Armor": "defense booster: 3 points",
    "Leather Armor": "defense booster: 5 points",
    "Combat Armor": "defense booster: 8 points",
    "Power Armor Frame": "defense booster: 14 points",
    "Assault Marine Armor": "defense booster: 15 points",
    "X-01 Power Armor": "defense booster: 18 points",
    "EMP Grenade": "defense disruptor: 5 points",
    "Plasma Pistol": "defense disruptor: 11 points",
    "Pulse Grenade": "defense disruptor: 17 points",
    "Railway Rifle": "defense disruptor: 25 points",
    "Plasma Caster": "defense disruptor: 31 points",
    "Tesla Cannon": "defense disruptor: 41 points",
    "Buffout": "strength booster: 2%",
    "Psycho": "strength booster: 8%",
    "Grape Mentats": "strength booster: 15%",
    "Overdrive": "strength booster: 20%",
    "Psycho Buff": "strength booster: 26%",
    "Fury": "strength booster: 32%",
    "Flashbang Grenade": "strength disruptor: 6%",
    "Plasma Grenade": "strength disruptor: 12%",
    "Cryolator": "strength disruptor: 15%",
    "Alien Blaster": "strength disruptor: 16%",
    "Experimental MIRV": "strength disruptor: 21%",
    "Plasma Defender": "strength disruptor: 27%"
}

def computer_plays():
    global computer_hand, cards_action, deck
    global computer_turn, user_turn, computer_defense, computer_health
    global computer_strength, user_defense, user_health, user_strength
    global cards_action
    print("It\'s my turn.")
    card = computer_hand.pop(0)
    print(f"I played {card}.")
    cards_action[card]()
    computer_hand.append(deck[0])
    del deck[0]
    print(f"My stats: defense {int(computer_defense)}, health {int(computer_health)},"\
    f"\nstrength {int(computer_strength)}")
    print(f"Your stats: defense {int(user_defense)}, health {int(user_health)},"\
    f"\nstrength {int(user_strength)}")
    print("I took a card from the deck")
    computer_turn, user_turn = False, True

def user_plays():
    global user_hand, cards_action, deck, cards_discription
    global computer_turn, user_turn, computer_defense, computer_health
    global computer_strength, user_defense, user_health, user_strength
    print("It\'s your turn")
    counter = 1
    for card in user_hand:
        print(f"{counter}- {card} -> {cards_discription[card]}.")
        counter += 1
    while True:
        try:
            card = int(input("Please enter the number of the card you\
            \nwant to play, from 1 to 6 or enter 0 to close the game now.\n"))
        except:
            print("Invalid input! Please try again.")
            continue
        if card == 0:
            exit()
        if card < 1 or card > 6:
            print("Invalid input! Please try again.")
            continue
        else:
            card -= 1
            break
    card = user_hand.pop(card)
    print(f"You played {card}.")
    cards_action[card]()
    user_hand.append(deck[0])
    del deck[0]
    print(f"Your stats: defense {int(user_defense)}, health {int(user_health)},"\
    f"\nstrength {int(user_strength)}")
    print(f"My stats: defense {int(computer_defense)}, health {int(computer_health)},"\
    f"\nstrength {int(computer_strength)}")
    print(f"You took a {user_hand[-1]} card from the deck")
    computer_turn, user_turn = True, False

# main
print("Welcome to the Duel time: FallOut.\nGood luck, dear wastelander.")
deck = deck_generator(cards_list)
computer_hand, user_hand = hand_generator(deck)
print("Lets find out who can start the game")
beginner()
while True:
    if computer_turn:
        computer_plays()
    if user_health <= 0:
        print("and yes! I just won! Hope you play again with me dear, but"\
        f"\nI'll win again!")
        break
    if not deck:
        deck = deck_generator(cards_list)
    if user_turn:
        user_plays()
    if computer_health <= 0:
        print("Did you really win?! if it was an honest victory, prove me by"\
        f"\nPlaying again!")
        break