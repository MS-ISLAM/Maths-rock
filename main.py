import random as r
def result(rightcount,wrongcount,correctAnswer,yourAnswer):
    if wrongcount == 0:
        print("Correct answer = ",correctAnswer)
        print("your Answers = ",yourAnswer)
        print("well done! all answers are correct...\nKeep practicing")
    elif rightcount >=7:
        print("Correct answer = ",correctAnswer)
        print("your Answers = ",yourAnswer)
        print(rightcount,"answers are right and ",wrongcount,"answers are wrong")
        print("Good...! work more to be batter\nKeep praciting")
    else:
        print("Correct answer = ",correctAnswer)
        print("your Answers = ",yourAnswer)
        print(rightcount,"answers are right and ",wrongcount,"answers are wrong")
        print("You need to practice alot\n Keep practicing")

def add(level): 
    rightcount = 0
    wrongcount = 0
    correctAnswer = {}
    yourAnswer = {}
    questonNumList = []
    for k in range(10):
        print("Q",k+1,sep="",end=") ")
        questonNumList.append(k+1)
        if level == 1:
            a = r.randrange(20)
            b = r.randrange(15)
        elif level == 2:
            a = r.randrange(10,41)
            b = r.randrange(5,20)
        elif level == 3:
            a = r.randrange(20,51)
            b = r.randrange(20,30)
        elif level == 4:
            a = r.randrange(40,101,2)
            b = r.randrange(30,60)
        q = str(a)+" + "+str(b)+" = "
        correctAnswer[q] = a+b
        print(a,"+",b,"=",end="")
        answer = int(input())
        if answer == a+b:
            yourAnswer[q] = answer
            rightcount+=1
        else:
             yourAnswer[q] = answer
             wrongcount+=1
    result(rightcount,wrongcount,correctAnswer,yourAnswer)
def sub(level): 
    rightcount = 0
    wrongcount = 0
    correctAnswer = {}
    yourAnswer = {}
    for k in range(10):
        print("Q",k+1,sep="",end=") ")
        if level == 1:
            a = r.randrange(25)
            b = r.randrange(15)
            if a < b:
                a, b = b, a
        elif level == 2:
            a = r.randrange(10,36)
            b = r.randrange(20)
            if a < b:
                a, b = b, a
        elif level == 3:
            a = r.randrange(20,50)
            b = r.randrange(10,30)
            if a < b:
                a, b = b, a
        elif level == 4:
            a = r.randrange(40,111,2)
            b = r.randrange(20,50)
            if a < b:
                a, b = b, a
        q = str(a)+" - "+str(b)+" = "
        correctAnswer[q] = a-b
        print(a,"-",b,"=",end="")
        answer = int(input())
        if answer == a-b:
            yourAnswer[q] = answer
            rightcount+=1
        else:
             yourAnswer[q] = answer
             wrongcount+=1
    result(rightcount,wrongcount,correctAnswer,yourAnswer)
