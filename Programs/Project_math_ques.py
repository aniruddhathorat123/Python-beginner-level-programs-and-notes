# Practive for maultiplication table.
# - User specifies number of random practive question.
# - user is presented with promt e.g. `5x5=` and input the answer for each
#   of the question.
# - WHen all questions are answered: print
#     - some for of `thankes for playing`.
#     - number of correct answers/total answrs.
#     - % of correct.
# Bonus 1: Also present the time it took to answer question: in total and
#          per question
# Bonus 2: let user specify how high the numbers used should be.
# Bonus 3: Show all questions and answers at the end


from random import randrange
from time import time

num_ques = int(input("Enter how many questions you want: "))
max_no = int(input("Enter highest number that can be use in questions: ")) 
correct = 0
answer_list = []

start_time = time()
if num_ques > 0:
    for i in range(num_ques):
        # `max_no + 1` because end boundary value is never shows in randrange.
        num1, num2 = randrange(1, max_no + 1), randrange(1, max_no + 1)
        question = f" {num1} x {num2} = "
        ans = int(input(question))
        answer_list.append(f"{question}{num1 * num2} | your answer: {ans}")
        if ans == num1 * num2:
            correct += 1
tot_time = time() - start_time
print(f'''-------------- Result -------------------
Total Question: {num_ques}
Total correct answers: {correct}
Total Incorrect answers: {num_ques - correct}
Percent of accuracy: {(100 * correct) / num_ques}%
Total time taken: {round(tot_time, 1)} sec
Average time per question: {round((tot_time)/num_ques, 1)}''')
print("Answers: ")
for i in range(num_ques):
    print(answer_list[i])
print("-----------------------------------------")


#OP: 
# Enter how many questions you want: 2
# Enter highest number that can be use in questions: 10
#  7 x 6 = 42
#  8 x 8 = 64
# -------------- Result -------------------
# Total Question: 2
# Total correct answers: 2
# Total Incorrect answers: 0
# Percent of accuracy: 100.0%
# Total time taken: 6.1 sec
# Average time per question: 3.0
# Answers:
#  7 x 6 = 42 | your answer: 42
#  8 x 8 = 64 | your answer: 64
# -----------------------------------------