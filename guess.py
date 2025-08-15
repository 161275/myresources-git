from random import randint

low_num, high_num = 1,10
rand: int = randint(low_num, high_num)
print(f'Guess the number in range {low_num} and {high_num}')
print(f'you have max 4 attempts.')


s = 4
while s>0:
    try: 
        user_guess: int = int(input('Guess: '))
    except ValueError as e:
        s-=1
        print(f"Please enter a valid number |r {s} attempt left")
        continue
        
    
    if user_guess > rand:
        s-=1
        print(f"the number is lower  |r {s} attempt left")
    elif user_guess < rand:
        s-=1
        print(f"the number is greater |r {s} attempt left")
    else:
        print("you guess it right")
        break
        exit(0)
if s == 0:
    print("you lost max attempts")



