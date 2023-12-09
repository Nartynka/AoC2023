from dataclasses import dataclass

@dataclass
class Hand:
   cards: str
   bid: int
   strength: int = 0

"""
strength:
   7 - Five of a kind
   6 - Four of a kind
   5 - Full house
   4 - Three of a kind
   3 - Two pairs
   2 - One pair
   1 - High card
"""

posibilities = "AKQJT98765432"
all_hands = []

# Revers the alpahabetical sort order
letter_map = {"T": "A", "J": ".", "Q": "C", "K": "D", "A": "E"}

sum = 0

def get_strength(cards):
   return [letter_map.get(card, card) for card in cards]


with open("input.txt") as file:
   # One hand at a time
   for line in file:
      curr_hand = line.strip().split(" ")
      curr_hand = Hand(curr_hand[0], int(curr_hand[1]))
      all_hands.append(curr_hand)

      types = []
      joker_count = curr_hand.cards.count("J")
      for char in posibilities:
         count = curr_hand.cards.count(char)
         if count > 0:
            types.append(count)
      
      if 5 in types or joker_count == 5:
         curr_hand.strength = 7
      if 4 in types:
         if joker_count > 0:
            curr_hand.strength = 7
         else:
            curr_hand.strength = 6

      elif 3 in types:
         if joker_count == 1:
            curr_hand.strength = 6
         elif joker_count == 2:
            curr_hand.strength = 7
         elif joker_count == 3:
            if 2 in types:
               curr_hand.strength = 7
            else:
               curr_hand.strength = 6
         else:
            if 2 in types:
               curr_hand.strength = 5
            else:
               curr_hand.strength = 4

      elif 2 in types and types.count(2) == 2:
         if joker_count == 1:
            curr_hand.strength = 5
         elif joker_count == 2:
            curr_hand.strength = 6
         elif joker_count == 3:
            curr_hand.strength = 7
         else:
            curr_hand.strength = 3

      elif 2 in types:
         if joker_count == 1:
            curr_hand.strength = 4
         elif joker_count == 2:
            curr_hand.strength = 4
         elif joker_count == 3:
            curr_hand.strength = 7
         else:
            curr_hand.strength = 2
         
      elif 1 in types:
         if joker_count == 1:
            curr_hand.strength = 2
         elif joker_count == 2:
            curr_hand.strength = 4
         elif joker_count == 3:
            curr_hand.strength = 6
         elif joker_count == 4:
            curr_hand.strength = 7
         else:
            curr_hand.strength = 1


# First sort by strength and then by get_strength
all_hands.sort(key=lambda hand: (hand.strength, get_strength(hand.cards)))

for count, hand in enumerate(all_hands):
   sum += hand.bid * (count + 1)

print("Sum: ", sum)