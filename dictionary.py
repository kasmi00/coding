"""
It ia always represent in form of:
my_dictionary = {"key" :"value"}
"""
# why we need dictionary?
#--> To overcome the problem exist in list.
#eg:
#detail=["kasmi","thapa",20{"english","nepali","japnese"},9845141112,{"burger","pizza","momo"}]

user_details={
    "first_name":"Kasmi",
    "last_name":"thapa",
    "language_spoken":["english","nepali","japanese"],
    "contact":9845141112,
    "fav_food":["burger","pizza","momo"]    
    }

# print(user_details["first_name"])

for key,value in user_details.items():
        print(f"the key is:{key}and its value is:{value}")

 
 
 
for key in user_details.items():
            print(f"the key is:{key}")
