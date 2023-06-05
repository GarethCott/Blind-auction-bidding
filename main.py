from replit import clear

print("Welcome to secrect auction bidding")
users = {}
more_bidders = True

while more_bidders is True:
  user_name = input("What is your name: ")
  user_bid = int(input("What is your bid amount?: $"))
  other_bidders = input("Are there other bidders? Type yes or no. ")
  users[user_name] = user_bid
  if other_bidders == "no":
    more_bidders = False
  else:
    clear()
    
print(users)
highest_bid = max(users.values())
highest_user = max(users, key=users.get)

print(f"The winner is {highest_user} with a bid of ${highest_bid}")
