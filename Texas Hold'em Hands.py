hand_starting_index = []
good_color = ""

def hand(hole_cards, community_cards):
    combined_cards = hole_cards + community_cards
    combined_cards = sortCards(combined_cards)
    if isStraightFlush(combined_cards.copy()):
        combined_cards = removeDuplicatesWithLessColors(combined_cards)
        combined_cards = removeColorFromCards(changeNumbersToHighCards(combined_cards))
        return_string = "straight-flush"  
        return_list = combined_cards[hand_starting_index[-1]:hand_starting_index[-1] + 5]
        return (return_string, return_list)
    elif isFourOfAKind(combined_cards.copy()):
        combined_cards = removeDuplicatesForFourOfAKind(combined_cards)
        combined_cards = removeColorFromCards(changeNumbersToHighCards(combined_cards))
        return_string = "four-of-a-kind"
        return (return_string, combined_cards)
    elif isFullHouse(combined_cards.copy()):
        combined_cards = removeDuplicatesForFullHouse(combined_cards)
        return_string = "full house"
        return (return_string, combined_cards)
    elif isFlush(combined_cards.copy()):
        getGoodFlushIndexes(combined_cards)
        combined_cards = removeColorFromCards(changeNumbersToHighCards(combined_cards)) 
        return_string = "flush"
        return_list = []
        for id in hand_starting_index:
            return_list.append(combined_cards[id])
        return (return_string, return_list)
    elif isStraight(combined_cards.copy()):
        combined_cards = removeDuplicatesWithLessColors(combined_cards)
        combined_cards = removeColorFromCards(changeNumbersToHighCards(combined_cards))
        return_string = "straight"
        return_list = combined_cards[hand_starting_index[-1]:hand_starting_index[-1] + 5]
        return (return_string, return_list)
    elif isThreeOfAKind(combined_cards.copy()):
        combined_cards = removeDuplicatesForThreeOfAKind(combined_cards)
        return_list = removeColorFromCards(changeNumbersToHighCards(combined_cards))
        return_string = "three-of-a-kind"
        return (return_string, return_list)
    elif isTwoPairs(combined_cards.copy()):
        combined_cards = removeDuplicatesForTwoPairs(combined_cards)
        return_list = removeColorFromCards(changeNumbersToHighCards(combined_cards))
        return_string = "two pair"
        return (return_string, return_list)
    elif isPair(combined_cards.copy()):
        combined_cards = removeDuplicatesForPair(combined_cards)
        return_list = removeColorFromCards(changeNumbersToHighCards(combined_cards))
        return_string = "pair"
        return (return_string, return_list)
    else:
        combined_cards = removeColorFromCards(changeNumbersToHighCards(combined_cards))
        return ("nothing", [combined_cards[0], combined_cards[1], combined_cards[2], combined_cards[3], combined_cards[4]])

def removeDuplicatesForPair(combined_cards):
    global hand_starting_index
    temp_combined_cards = combined_cards[hand_starting_index[0]:hand_starting_index[0] + 2]
    for id, card in enumerate(combined_cards):
        for id2, card2 in enumerate(temp_combined_cards):
            if combined_cards[id] == temp_combined_cards[id2]:
                combined_cards.pop(id)
    return [temp_combined_cards[0], combined_cards[0], combined_cards[1], combined_cards[2]]

def removeDuplicatesForTwoPairs(combined_cards):
    global hand_starting_index
    temp_combined_cards = combined_cards[hand_starting_index[0]:hand_starting_index[0] + 2] + combined_cards[hand_starting_index[1]:hand_starting_index[1] + 2]
    for id, card in enumerate(combined_cards):
        for id2, card2 in enumerate(temp_combined_cards):
            if combined_cards[id] == temp_combined_cards[id2]:
                combined_cards.pop(id)
    return [temp_combined_cards[0], temp_combined_cards[2], combined_cards[0]]

def getGoodFlushIndexes(combined_cards):
    global hand_starting_index, good_color
    hand_starting_index.clear()
    temp_array = 0
    for idx, card in enumerate(combined_cards):
        if card[-1] == good_color and temp_array < 5:
            hand_starting_index.append(idx)
            temp_array += 1
        elif temp_array >= 5:
            break
        

def removeDuplicatesForFullHouse(combined_cards):
    global hand_starting_index
    temp_combined_cards = []
    combined_cards = changeNumbersToHighCards(combined_cards)
    temp_combined_cards.append(combined_cards[hand_starting_index[0]][:-1])
    temp_combined_cards.append(combined_cards[hand_starting_index[-1]][:-1])
    return temp_combined_cards
    
def removeDuplicatesForFourOfAKind(combined_cards):
    global hand_starting_index
    temp_combined_cards = combined_cards[hand_starting_index[-1]:hand_starting_index[-1] + 4]
    print(combined_cards, temp_combined_cards, hand_starting_index)
    for id,val in enumerate(combined_cards):
        for id2,val2 in enumerate(temp_combined_cards):
            if combined_cards[id] == temp_combined_cards[id2]:
                combined_cards.pop(id)
    return [temp_combined_cards[0], combined_cards[0]]

def removeDuplicatesForThreeOfAKind(combined_cards):
    global hand_starting_index
    temp_combined_cards = combined_cards.copy()
    temp_combined_cards = combined_cards[hand_starting_index[-1]:hand_starting_index[-1] + 3]
    for id,elem in enumerate(temp_combined_cards):
        for id2,elem2 in enumerate(combined_cards):
            if combined_cards[id2] == temp_combined_cards[id]:
                combined_cards.pop(id2)
#     combined_cards = changeNumbersToHighCards(combined_cards)
    return [temp_combined_cards[0], combined_cards[0], combined_cards[1]]

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
    hand_starting_index.clear()
    check_index = 0
    removeDuplicatesWithLessColors(combined_cards)
    while check_index <= len(combined_cards) - 5:
        if  int(combined_cards[check_index][:-1]) - 1 == int(combined_cards[check_index + 1][:-1]) and \
            int(combined_cards[check_index + 1][:-1]) - 1 == int(combined_cards[check_index + 2][:-1]) and \
            int(combined_cards[check_index + 2][:-1]) - 1 == int(combined_cards[check_index + 3][:-1]) and \
            int(combined_cards[check_index + 3][:-1]) - 1 == int(combined_cards[check_index + 4][:-1]) and \
            combined_cards[check_index][-1] == combined_cards[check_index + 1][-1] and \
            combined_cards[check_index + 1][-1] == combined_cards[check_index + 2][-1] and \
            combined_cards[check_index + 2][-1] == combined_cards[check_index + 3][-1] and \
            combined_cards[check_index + 3][-1] == combined_cards[check_index + 4][-1]:
            hand_starting_index.append(check_index)     
            return True
        check_index += 1
    return False

def removeDuplicatesWithLessColors(combined_cards):
    colors = {"♥": 0, "♠": 0, "♦": 0, "♣": 0}
    for card in combined_cards:
        if card[-1] == "♦":
            colors["♦"] += 1
        if card[-1] == "♠":
            colors["♠"] += 1
        if card[-1] == "♥":
            colors["♥"] += 1
        if card[-1] == "♣":
            colors["♣"] += 1
    temp_index = 0
    while temp_index < len(combined_cards) - 1:
        if combined_cards[temp_index][:-1] == combined_cards[temp_index + 1][:-1]:
            if colors[combined_cards[temp_index][-1]] < colors[combined_cards[temp_index + 1][-1]]:
                combined_cards.pop(temp_index)
                temp_index = 0
            else:
                combined_cards.pop(temp_index + 1)
                temp_index = 0
        temp_index += 1
    return combined_cards
        
    
def isStraight(combined_cards):
    global hand_starting_index
    hand_starting_index.clear()
    combined_cards = removeDuplicatesWithLessColors(combined_cards)
    check_index = 0
    while check_index <= len(combined_cards) - 5:
        if  int(combined_cards[check_index][:-1]) - 1 == int(combined_cards[check_index + 1][:-1]) and \
            int(combined_cards[check_index + 1][:-1]) - 1 == int(combined_cards[check_index + 2][:-1]) and \
            int(combined_cards[check_index + 2][:-1]) - 1 == int(combined_cards[check_index + 3][:-1]) and \
            int(combined_cards[check_index + 3][:-1]) - 1 == int(combined_cards[check_index + 4][:-1]):
            hand_starting_index.append(check_index)
            return True
        check_index += 1
    return False

def isFourOfAKind(combined_cards):
    global hand_starting_index
    hand_starting_index.clear()
    check_index = 0
    while check_index <= len(combined_cards) - 4:
        if  int(combined_cards[check_index][:-1]) == int(combined_cards[check_index + 1][:-1]) and \
            int(combined_cards[check_index + 1][:-1]) == int(combined_cards[check_index + 2][:-1]) and \
            int(combined_cards[check_index + 2][:-1]) == int(combined_cards[check_index + 3][:-1]):
            hand_starting_index.append(check_index)
            return True    
        check_index += 1
    return False
    
def isThreeOfAKind(combined_cards):
    global hand_starting_index
    hand_starting_index.clear()
    check_index = 0
    while check_index <= len(combined_cards) - 3:
        if  int(combined_cards[check_index][:-1]) == int(combined_cards[check_index + 1][:-1]) and \
            int(combined_cards[check_index + 1][:-1]) == int(combined_cards[check_index + 2][:-1]):
            hand_starting_index.append(check_index)
            return True    
        check_index += 1
    return False

def isPair(combined_cards):
    global hand_starting_index
    hand_starting_index.clear()
    check_index = 0
    while check_index <= len(combined_cards) - 2:
        if int(combined_cards[check_index][:-1]) == int(combined_cards[check_index + 1][:-1]):
            hand_starting_index.append(check_index)
            return True    
        check_index += 1
    return False

def isTwoPairs(combined_cards):
    global hand_starting_index
    hand_starting_index.clear()
    check_index = 0
    hasPair = False
    while check_index <= len(combined_cards) - 2:
        if int(combined_cards[check_index][:-1]) == int(combined_cards[check_index + 1][:-1]):
            del combined_cards[check_index]
            del combined_cards[check_index]
            hasPair = True
            hand_starting_index.append(check_index)
            break
        check_index += 1
    
    check_index = 0
    hasSecondPair = False
    while check_index <= len(combined_cards) - 2:
        if int(combined_cards[check_index][:-1]) == int(combined_cards[check_index + 1][:-1]):
            hand_starting_index.append(check_index + 2)
            hasSecondPair = True
            break
        check_index += 1
    if hasPair and hasSecondPair:
        return True
    else:
        return False
    
def isFlush(combined_cards):
    global hand_starting_index, good_color
    hand_starting_index.clear()
    colors = {"♥": 0, "♠": 0, "♦": 0, "♣": 0}
    for card in combined_cards:
        if card[-1] == "♦":
            colors["♦"] += 1
        if card[-1] == "♠":
            colors["♠"] += 1
        if card[-1] == "♥":
            colors["♥"] += 1
        if card[-1] == "♣":
            colors["♣"] += 1
    for color,number in colors.items():
        if number >= 5:
            good_color = color
            return True
    return False

def isFullHouse(combined_cards):
    global hand_starting_index
    hand_starting_index.clear()
    hasThreeOfAKind = False
    check_index = 0
    temp_index = 0
    while check_index <= len(combined_cards) - 3:
        if  int(combined_cards[check_index][:-1]) == int(combined_cards[check_index + 1][:-1]) and \
            int(combined_cards[check_index + 1][:-1]) == int(combined_cards[check_index + 2][:-1]):
            hand_starting_index.append(check_index)
            temp_index = check_index
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
            if temp_index > check_index:
                hand_starting_index.append(check_index)
            else:
                hand_starting_index.append(check_index + 3)
            break
        check_index += 1
    if hasPair and hasThreeOfAKind:
        return True
    else:
        return False
    
    
