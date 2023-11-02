import random
def guess_number():
    return random.randint(1,100)
target_number=guess_number()
attempt=0
while True:
    user_guess=int(input("guess a number"))
    attempt+=1
    if user_guess==target_number:
        print("Congratulation ! you have guesses the number in",attempt,"attempts")
        break
    elif user_guess<target_number:
        print("Try higher no")
    else:
        print("try lower no")