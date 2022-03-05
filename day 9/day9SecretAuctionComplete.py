from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.
print(logo)
print("Welcome to the secret auction program")
attender = {}
def auctioneer(bidder, bid_number):
  attender[bidder]= bid_number
  #attender.append(attender) 

def find_highest_bidder(bidding_record):
  highest_bid = 0
  winner = ""
  # {"Angela": 123, "James": 321}
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder
  print(f"The Winner {winner} with a bid of ${highest_bid} ")

bidding_finished = False
while not bidding_finished:
  bidder = input("What is your name?: ")
  bid_number = int(input("What's your bid?: $"))
  auctioneer(bidder, bid_number)
  should_continue = input("Are there any other bidders? Type 'yes' or 'no' ")
  if should_continue == "no":
    find_highest_bidder(attender)
    bidding_finished = True
  elif should_continue == "yes":
    clear()
  
    
    
  
  


