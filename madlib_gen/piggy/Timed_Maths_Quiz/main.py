import random
import time

MIN_NUM = 3
MAX_NUM = 7
OPERATORS = ["+", "-", "*"]
MAX_QUES = 10

def maths_challenge():
    left = random.randint(MIN_NUM, MAX_NUM)
    right = random.randint(MIN_NUM, MAX_NUM)
    operand = random.choice(OPERATORS)
    expression = str(left) + " " + operand + " " + str(right)

    answer = eval(expression)
    #print(expression, answers)
    return(expression, answer)

input('press any key to begin: ')
print("-------------------------------")

start_time = time.time()
wrong = 0
for i in range(MAX_QUES):
    expr, ans = maths_challenge()
    while True:
        guess_ans = input("problem" + str(i+1) + " " + expr + " = ")
        if guess_ans == str(ans):
            break
        wrong += 1
end_time = time.time()
total_time = round(end_time - start_time, 2)
print("-------------------------------------------------------")
print('\nYou finished the quiz in', total_time, 'secomds')
print('You made', wrong, 'error')