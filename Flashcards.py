Question_Answer = {'Which gas moderates the ozone reaction?' : 'Nitrogen', 'What is the third layer of the atmosphere?' : 'Mesosphere', 'What is the important gas in the second layer of Earth?' : 'Ozone', 'What is ozone made of?' : 'O3'}

# Let's play a GAME!!!
#Guess the answer to the given question. Get it right, and you move on. Get it wrong, and.... let's just say, you probably won't enjoy what comes next :)

#how to sort questions based on adequacy

import random

tally_questions = [] 
well_known = [] # answered correctly thrice
medium_known = [] # answered correctly twice
least_known = [] # answered correctly less than twice

#populate tally_questions (with 0 counter) to correspond with dictionary using a for loop
for i in range(0, len(Question_Answer), 1):
     tally_questions.append(0)

next_round = 'yes'
score = 0
while next_round.upper() == 'YES':

     RandInt = random.randint(0, 3)

     Q_A = list(Question_Answer.items())[RandInt] #turns dict. to select questions easily
     # Q_A = ('Question', 'Answer')
     Q = Q_A[0]
     A = Q_A[1]
     print(Q)

     if input('Answer: ', ).upper() == A.upper(): 
          print('Congratulations! You got the answer correct.')
          score += 1
          Tally = tally_questions[RandInt] 
          tally_questions[RandInt] = Tally + 1
          
     else:
          print('ER-OR! Wrong, wrong, wrong, better luck next time lad.')
          Tally = tally_questions[RandInt] 
          tally_questions[RandInt] = Tally - 1

     next_round = input('\nWould you like to continue to the next round? [Yes/No]', )


print('\nThank you for practicing your work. Your score is: ', score, '\nRemember: a question a day keeps the uncertainty away!')
for i in tally_questions:
     if i == 3:
          well_known.append(tally_questions.index(i))

     if i == 2:
          medium_known.append(tally_questions.index(i))

     if i < 2:
          least_known.append(tally_questions.index(i))

print(well_known, ':', medium_known, ':', least_known)