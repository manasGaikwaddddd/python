# dicct ={
#      "bug":"an error in program",
#      "func":"a piece of code",
#      "loop":"looppppppppppppp",
#      1:123,
#  }
# print(dicct["bug"])
# print(dicct[1])
#
# # adding new items
# dicct["pop"]="poped"
# print(dicct)
# # empty
# dicctem={}
# dicctem["poppp"]="popopop"
# print(dicctem)

# loop through dict
# for n in dicct:
#     print(n)
# studentscore={
#     "manas":81,
#     "tom":10,
#     "drac":20,
#     "juicy":90
# }
# studentgrades={
#
# }
# for student in studentscore:
#     score = studentscore[student]
#     if score>80:
#         studentgrades[student]="outstanding"
#     elif score >10:
#         studentgrades[student]="poor"
#     else:
#         studentgrades[student]="fail"
# print(studentgrades)

# travel={
#     "maha":{"citiesvisited":["pen","mumbai"],"toyalvisits":12,},
#     "india":{"citiesvisited":["goa","kerla"],"tptalvisits":10}
#
# }
# print(travel)
#
# travel_log = [
#     {
#         "country":"india",
#         "cities visites":["pen",'mumbai','pune'],
#         "total_visites":121
#
#     },
#     {
#         "country": "uk",
#         "cities visites": ["newjersey", 'london', ],
#         "total_visites": 121
#
#     },
#
# ]
# print(travel_log)
#
# country = input() # Add country name
# visits = int(input()) # Number of visits
# list_of_cities = eval(input()) # create list from formatted string
# travel_log = [
#   {
#     "country": "France",
#     "visits": 12,
#     "cities": ["Paris", "Lille", "Dijon"]
#   },
#   {
#     "country": "Germany",
#     "visits": 5,
#     "cities": ["Berlin", "Hamburg", "Stuttgart"]
#   },
# ]
# # Your code here 👇
# def add_new_countrt(name,times_visited,cities_visited):
#     new_country={}
#     new_country["country"]=name
#     new_country["visits"]=times_visited
#     new_country["cities"]=cities_visited
#     travel_log.append(new_country)
#
#
#
#
#
# add_new_countrt(country,visits,list_of_cities)
# print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
# print(f"My favourite city was {travel_log[2]['cities'][0]}.")

# the screte aution

bids = {}
bidding_finished = False


def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    # bidding_record = {"Angela": 123, "James": 321}
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")


while not bidding_finished:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
    if should_continue == "no":
        bidding_finished = True
        find_highest_bidder(bids)
    elif should_continue == "yes":
     print()




