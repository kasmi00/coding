import random

winning_number = random.randint(0,100)

print(winning_number)

def guess_function(user_provided_num):
    game_over=False
    guess_counter=1 
    while not game_over:
        if winning_number==user_provided_num:
            print(f"You won the game in {guess_counter} {'times' if guess_counter==1 else 'times'}")
            game_over = True
        else:
            if user_provided_num > winning_number:
                print("The number is too high")
            else:
                print("The number is too low")
                user_provided_num= int(input("please guess again"))


user_provided_num = int(input("please provide yor number:"))
print(guess_function(user_provided_num))



