from art import logo
import os

print(logo)
print("Welcome to the secret auction  program.")

have_bidder = True
bidders = {}
highest_bid = 0
winner = ""

while have_bidder:
    name = input("What is yout name: ")
    bid = round(float(input("What is your bid: $")))
    bidders[name] = bid
    other_bindder = input("Are there any other bidders: Type 'yes' or 'no'. \n").lower()

    if other_bindder != "yes":
        have_bidder = False

    os.system("clear")

for bidder in bidders:
    if bidders[bidder] > highest_bid:
        highest_bid = bidders[bidder]
        winner = bidder

print(f"The winner is {winner} with a bid of ${highest_bid}")
