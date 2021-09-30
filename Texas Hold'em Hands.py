def hand(hole_cards, community_cards):
    combined_cards = hole_cards + community_cards
    combined_cards = sortCards(combined_cards)
    print(combined_cards)
    return "nothing", ["2", "3", "4", "7", "8"]

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
    combined_cards = changeHighCardsToNumbers(combined_cards)
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
    combined_cards = changeHighCardsToNumbers(combined_cards)
    check_index = 0
    while check_index <= len(combined_cards) - 5:
        if  int(combined_cards[check_index][:-1]) - 1 == int(combined_cards[check_index + 1][:-1]) and \
            int(combined_cards[check_index + 1][:-1]) - 1 == int(combined_cards[check_index + 2][:-1]) and \
            int(combined_cards[check_index + 2][:-1]) - 1 == int(combined_cards[check_index + 3][:-1]) and \
            int(combined_cards[check_index + 3][:-1]) - 1 == int(combined_cards[check_index + 4][:-1]):
                return True
        check_index += 1
    return False
        
    
    
