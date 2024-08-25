# mini project discription:
# 1) user input => low and high bound
# 2) random => [a,b]
# 3) loop => condition => guess_count=5 => feedback

import random

try:
    low=int(input('Enter the lower bound: \n'))
    high=int(input('Enter the higher bound: \n'))
except:
    print('please enter a valid number')
    

r= random.randint(low, high)

guess_count=5

while guess_count>0:
    
    try:
        new_guess_str=input(f'remained guesses:{guess_count} => enter your next guess: \n')
        new_guess=int(new_guess_str)
        
        if r== new_guess:
            print('Great! your guess is correct.')
            break
        elif r>new_guess:
             print('your guess is lower than selected number!')
        else:
             print('your guess is higher than selected number!')
             
        guess_count -= 1
             
    except:
         print('please enter a valid number')

