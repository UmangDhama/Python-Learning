
from art import  logo

print(logo)

print("Welcome to the secret auction program.")
ans="yes"
dictionary = {}
while ans=="yes":
    name=input("What is yor name?: ")
    bid=int(input("What's your bid?: $"))
    print("Are there any other bidders? Type 'yes' or 'no'.")
    ans=input().lower()

    dictionary[name]=bid

    print(('\n'*100))
max_bid=0
Winner=""
for name in dictionary:

   if(dictionary[name]>max_bid):
       max_bid=dictionary[name]
       Winner=name


print(f"the winner is {Winner} with a bid of ${max_bid}.")
