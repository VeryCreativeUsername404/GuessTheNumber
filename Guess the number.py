from random import randint

num_range = 0, 10000
secret_num = randint(*num_range)

while True:
    try:
        user_num = int(
            input(f'Guess a number between {num_range[0]} and {num_range[1]}: '))        
        if user_num > num_range[1]:
            print(f'It must be between {num_range[0]} and {num_range[1]}!')
        elif user_num > secret_num:
            print('Too high...')
        elif user_num < secret_num:
            print('Too low...')
        else:
            print('You got it! Congrats!')
            break
    except ValueError:
        print('Type in an actual number.')
    print()