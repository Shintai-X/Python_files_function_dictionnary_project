import random
def replay(score):
    answer = input("You want to replay? Y)es or N)o")
    if answer == "Y":
        return True
    elif answer == "N":
        print("Ok! see you next time you score was: " + str(score) )
        return False
    else:
        print("Please answer only by Y or N")


print("Hello,Welcome to the guessing game! ")
playing = True
mystery_number = random.randint(1, 101)
score = 0
print(mystery_number)
print("This game will generate a random number from 1 to 100 ! Good luck to find the right one :)  ")
while playing:
    user_number = int(input("What number do you think of ? "))
    if user_number < mystery_number:
        print("Your number is to small , try again!")
    elif user_number > mystery_number:
        print("Your number is to big , try again!")
    else:
        score += 1
        print("Good Job man !")
        playing = replay(score)
        mystery_number = random.randint(1, 101)
        print(mystery_number)




