from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo

print(logo)

input("Welcome to the secret auction program." + "\n" + "Press enter to continue.")

bidders = {}
def add_bidder(name, bid):
    bidders[name] = bid
  
def find_highest_bidder(bidders):
  highest_bidder = ""
  highest_bid = 0
  for bidder in bidders:
    if highest_bid < bidders[bidder]:
      highest_bid = bidders[bidder]
      highest_bidder = bidder
  print(f"The winner is {highest_bidder} with a bid of ${highest_bid}.")
  
more_bidders = "yes"
while more_bidders == "yes":
  add_bidder(input("What is your name? "), int(input("What is your bid? $")))
  more_bidders = input("Are there any other bidders? Type 'yes' or 'no'. ")
  clear()

find_highest_bidder(bidders)
          