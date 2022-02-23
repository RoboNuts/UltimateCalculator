
midtermExam = int(input('Enter your midterm score: ' ))
assignments = int(input('Enter your assignment score: '))
participation = int(input('Enter your score: '))
finalExam = int(input('Enter your final exam score: '))


finalScore = (midtermExam * .3) + (assignments * .3) + participation + (finalExam *.35)

print('Your final score is: ' + str(finalScore))
