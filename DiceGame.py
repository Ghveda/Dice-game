import random



score1 = 0
score2 = 0

dice1 = random.randint(1,6)
dice2 = random.randint(1,6)

if dice1 < dice2:
    score2+=1
elif dice1 > dice2:
    score1+=1
else:
    print("Draw")


print('you roled ',dice1,'and ',score2)
print('score is ',score1,score2)