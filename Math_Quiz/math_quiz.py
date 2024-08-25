import random
import time

def question_generator():
    # generate two random numbers 
    a = random.randint(1, 9)
    b = random.randint(1 ,9)
    
    # random operator
    operator_list =["+", "-" ,"*"]
    selected_operator = random.choice(operator_list)
    
    print(f"{a} {selected_operator} {b} = ?")
    
    if selected_operator == "+":
        return a + b
    elif selected_operator == "-":
        return a - b
    else:
        return a*b

question_number_limit=5
question_number=0
score = 0
time_limit = 7

while question_number<question_number_limit:
    # step 1 :  generate a random question
    result = str(question_generator())
    start_time = time.time()
    
    # step 2 : get user answer
    user_answer = input("Enter your answer: ")
    end_time= time.time()
    
    time_difrence = end_time - start_time
    
    # step 3 : chwck the answer and time
    if time_difrence < time_limit:
        if result == user_answer:
             score += 1
             print(f"perfect, score: {score}")
        else:
            print("sorry! your answer is wrong")    
    else:
        print("your time is up!")        
        
        
    question_number += 1

print(f"FINAL SCORE:{score} out of {question_number_limit}")