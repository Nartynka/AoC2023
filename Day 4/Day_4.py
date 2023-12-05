import re
from dataclasses import dataclass

@dataclass
class Card:
   card_id: int
   wining_numbers: list
   card_numbers: list

copied_card_ids = []
coppied_cards = []

all_winning_numbers = []
all_card_numbers = []

card_count = 0

with open("input.txt") as file:
   # One card at a time
   for line in file:
      card_count+=1
      num_of_winning = 0
      line.strip()
      card_id = re.search(r'\d+',line.strip()).group()
      line = re.sub(r'Card\s+\d+: ','',line.strip())
      wining_numbers = line.split(" | ")[0].split(" ")
      card_numbers = line.split(" | ")[1].split(" ")
      
      wining_numbers = [int(num) for num in wining_numbers if num]
      card_numbers = [int(num) for num in card_numbers if num]
      
      all_winning_numbers.append(wining_numbers)
      all_card_numbers.append(card_numbers)
      
      for number in card_numbers:
         if number in wining_numbers:
            num_of_winning+=1
            copied_card_ids.append(int(card_id)+num_of_winning)

while True:
   for card_id in copied_card_ids:
      c = Card(card_id, all_winning_numbers[card_id-1], all_card_numbers[card_id-1])
      coppied_cards.append(c)
   
   copied_card_ids = []
   
   for card in coppied_cards:
      # Porcess one card
      card_count+=1
      num_of_winning = 0
      for number in card.card_numbers:
            if number in card.wining_numbers:
               num_of_winning+=1
               copied_card_ids.append(int(card.card_id)+num_of_winning)
   coppied_cards.clear()

   # If there are no more copies, break the loop
   if len(copied_card_ids) == 0:
      break

print("Card Count: ", card_count)