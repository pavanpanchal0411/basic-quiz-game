print("-----------------")
print("!!!!Quiz Game!!!!")
print("-----------------")

questions=[
    {"que":"When was Microsoft's Hotmail launched? ","ans":"B"},#109
    {"que":"In which organisation was first video conferencing first used_______ ","ans":"A"},#121
    {"que":"Which of the following is not associated with respiration?","ans":"B"},#hb 46
    {"que":"What caused the craters on the moon ?","ans":"D"},#sp 27
    {"que":"The sun glows due to ___________ reactions. ","ans":"B"} #sp 28
]
options=[
    ["A. 1990","B. 1996","C. 2000","D. 1986"],
    ["A. NASA","B. Microsoft","C. IBM","D. Apple"],
    ["A. Lungs","B. Kidneys","C. Gills","D. Skin"],
    ["A. Stars","B. Planets","C. Sun","D. Meteors"],
    ["A. Chemical","B. Fission","C. Fusion","D. Neutralisation"]
]
score=0

def check_answer(user_guess,correct_answer):
    if user_guess==correct_answer:
        return True
    else:
        return False
    
    
for i in range(len(questions)):
    print("---------------------------------")
    print(questions[i]["que"])
    
    for j in options[i]:
        print(j)
        
    user_answer=input("Enter your answer(A or B or C or D):").upper()
    is_correct=check_answer(user_answer,questions[i]["ans"])
    if is_correct:
        print("correct answer")
        score+=1
        
    else:
        print("incorrect answer")
        print(f"the correct answer is {questions[i]['ans']}")
    print(f"Your present score is {score}/{i+1}")

print(f"You have given {score} correct answers")
print(f"Your score is {score/len(questions)*100}")