import random

# 1) list of names
# 2) select one name randomly
# 3) get user char
# 4) check => win/loss

names=['Ali', 'Mohi' ,'Danial', 'Mary', 'Arshia', 'Saba', 'Rha', 'Aban']

selected_name=random.choice(names).lower()

guess_count = len(selected_name)
guessed_list = ['-'] * len(selected_name)

while guess_count>0:
    guessed_char = input('enter char: \n')
    
    if guessed_char.isalpha():
        if guessed_char in selected_name:
            if guessed_char in guessed_list:
                print('you have guessed this befor, try a new character')
            else:
                for idx,char in enumerate(selected_name):
                    if char == guessed_char:
                        guessed_list[idx]=guessed_char
                current_guess=" ".join(guessed_list)
                print(f"perfect => {current_guess}")
                
                if not "-" in guessed_list:
                    print("you won!")
                    break
                    
            
        else:
            guess_count -= 1
            print(f'Wrong! => remained guesses:{guess_count}')
            
    else:
         print('please enter a valid number')