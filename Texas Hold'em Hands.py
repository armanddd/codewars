hand_starting_index = []

def hand(hole_cards, community_cards):
    combined_cards = hole_cards + community_cards
    combined_cards = sortCards(combined_cards)
    
    #     print(isFullHouse(combined_cards.copy()))
    #     print(combined_cards)

    if isStraightFlush(combined_cards):
        combined_cards = removeColorFromCards(changeNumbersToHighCards(combined_cards)) 
        return_string = "straight-flush"
        return_list = combined_cards[0:5]
        return (return_string, return_list)
    return "nothing", ["2", "3", "4", "7", "8"]

def removeColorFromCards(combined_cards):
    for idx, card in enumerate(combined_cards):
        combined_cards[idx] = card[:-1]
    return combined_cards

def sortCards(combined_cards):
    combined_cards = changeHighCardsToNumbers(combined_cards)
    
    sort_index = 0
    while sort_index < len(combined_cards) - 1:
        if (int(combined_cards[sort_index][:-1]) < int(combined_cards[sort_index + 1][:-1])):
            combined_cards[sort_index], combined_cards[sort_index + 1] = combined_cards[sort_index + 1], combined_cards[sort_index]
            sort_index = 0
            continue
        sort_index += 1
        
    return combined_cards

def changeNumbersToHighCards(combined_cards):
    # change numbers in to higher cards
    for idx, card in enumerate(combined_cards):
        if card[:-1] == "14":
            combined_cards[idx] = combined_cards[idx].replace("14", "A")
        if card[:-1] == "13":
            combined_cards[idx] = combined_cards[idx].replace("13" ,"K")
        if card[:-1] == "12":
            combined_cards[idx] = combined_cards[idx].replace("12" ,"Q")
        if card[:-1] == "11":
            combined_cards[idx] = combined_cards[idx].replace("11" ,"J")
    return combined_cards
    
def changeHighCardsToNumbers(combined_cards):
    # change higher cards in to numbers
    for idx, card in enumerate(combined_cards):
        if card[:-1] == "A":
            combined_cards[idx] = combined_cards[idx].replace("A", "14")
        if card[:-1] == "K":
            combined_cards[idx] = combined_cards[idx].replace("K" ,"13")
        if card[:-1] == "Q":
            combined_cards[idx] = combined_cards[idx].replace("Q" ,"12")
        if card[:-1] == "J":
            combined_cards[idx] = combined_cards[idx].replace("J" ,"11")
    return combined_cards

def isStraightFlush(combined_cards):
    global hand_starting_index
    check_index = 0
    while check_index <= len(combined_cards) - 5:
        if  int(combined_cards[check_index][:-1]) - 1 == int(combined_cards[check_index + 1][:-1]) and \
            int(combined_cards[check_index + 1][:-1]) - 1 == int(combined_cards[check_index + 2][:-1]) and \
            int(combined_cards[check_index + 2][:-1]) - 1 == int(combined_cards[check_index + 3][:-1]) and \
            int(combined_cards[check_index + 3][:-1]) - 1 == int(combined_cards[check_index + 4][:-1]) and \
            combined_cards[check_index][-1] == combined_cards[check_index + 1][-1] and \
            combined_cards[check_index + 1][-1] == combined_cards[check_index + 2][-1] and \
            combined_cards[check_index + 2][-1] == combined_cards[check_index + 3][-1] and \
            combined_cards[check_index + 3][-1] == combined_cards[check_index + 4][-1]:
            return True
        check_index += 1
    return False

def isStraight(combined_cards):
    global hand_starting_index
    check_index = 0
    while check_index <= len(combined_cards) - 5:
        if  int(combined_cards[check_index][:-1]) - 1 == int(combined_cards[check_index + 1][:-1]) and \
            int(combined_cards[check_index + 1][:-1]) - 1 == int(combined_cards[check_index + 2][:-1]) and \
            int(combined_cards[check_index + 2][:-1]) - 1 == int(combined_cards[check_index + 3][:-1]) and \
            int(combined_cards[check_index + 3][:-1]) - 1 == int(combined_cards[check_index + 4][:-1]):
            return True
        check_index += 1
    return False

def isFourOfAKind(combined_cards):
    global hand_starting_index
    check_index = 0
    while check_index <= len(combined_cards) - 4:
        if  int(combined_cards[check_index][:-1]) == int(combined_cards[check_index + 1][:-1]) and \
            int(combined_cards[check_index + 1][:-1]) == int(combined_cards[check_index + 2][:-1]) and \
            int(combined_cards[check_index + 2][:-1]) == int(combined_cards[check_index + 3][:-1]):
            return True    
        check_index += 1
    return False
    
def isThreeOfAKind(combined_cards):
    global hand_starting_index
    check_index = 0
    while check_index <= len(combined_cards) - 3:
        if  int(combined_cards[check_index][:-1]) == int(combined_cards[check_index + 1][:-1]) and \
            int(combined_cards[check_index + 1][:-1]) == int(combined_cards[check_index + 2][:-1]):
            return True    
        check_index += 1
    return False

def isPair(combined_cards):
    global hand_starting_index
    check_index = 0
    while check_index <= len(combined_cards) - 2:
        if int(combined_cards[check_index][:-1]) == int(combined_cards[check_index + 1][:-1]):
            return True    
        check_index += 1
    return False

def isTwoPairs(combined_cards):
    global hand_starting_index
    check_index = 0
    hasPair = False
    while check_index <= len(combined_cards) - 2:
        if int(combined_cards[check_index][:-1]) == int(combined_cards[check_index + 1][:-1]):
            del combined_cards[check_index]
            del combined_cards[check_index]
            hasPair = True
            break
        check_index += 1
    
    check_index = 0
    hasSecondPair = False
    while check_index <= len(combined_cards) - 2:
        if int(combined_cards[check_index][:-1]) == int(combined_cards[check_index + 1][:-1]):
            hasSecondPair = True
        check_index += 1
    if hasPair and hasSecondPair:
        return True
    else:
        return False
    
def isFlush(combined_cards):
    global hand_starting_index
    colors = {"hearts": 0, "spades": 0, "diamonds": 0, "clubs": 0}
    for card in combined_cards:
        if card[-1] == "♦":
            colors["diamonds"] += 1
        if card[-1] == "♠":
            colors["spades"] += 1
        if card[-1] == "♥":
            colors["hearts"] += 1
        if card[-1] == "♣":
            colors["clubs"] += 1
    for color,number in colors.items():
        if number >= 5:
            return True
    return False

def isFullHouse(combined_cards):
    global hand_starting_index
    hasThreeOfAKind = False
    check_index = 0
    while check_index <= len(combined_cards) - 3:
        if  int(combined_cards[check_index][:-1]) == int(combined_cards[check_index + 1][:-1]) and \
            int(combined_cards[check_index + 1][:-1]) == int(combined_cards[check_index + 2][:-1]):
            del combined_cards[check_index]
            del combined_cards[check_index]
            del combined_cards[check_index]
            hasThreeOfAKind = True
            break
        check_index += 1
    
    #checks for pair
    hasPair = False
    check_index = 0
    while check_index <= len(combined_cards) - 2:
        if int(combined_cards[check_index][:-1]) == int(combined_cards[check_index + 1][:-1]):
            hasPair = True  
        check_index += 1
    if hasPair and hasThreeOfAKind:
        return True
    else:
        return False
    
    
