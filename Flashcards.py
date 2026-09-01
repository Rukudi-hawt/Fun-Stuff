Question_Answer = {'Which gas moderates the ozone reaction?' : 'Nitrogen', 'What is the third layer of the atmosphere?' : 'Mesosphere', 'What is the important gas in the second layer of Earth?' : 'Ozone', 'What is ozone made of?' : 'O3'}

# Let's play a GAME!!!
#Guess the answer to the given question. Get it right, and you move on. Get it wrong, and.... let's just say, you probably won't enjoy what comes next :)

import random

#variables to tally amount of times a specific question was correct [can i pair the dictionary with a list indexing how often things are correct??]
## {key1: item1, key2: item2, key3: item3} == [tally1, tally2, tally 3]

tally_questions = []
#populate tally_questions (with 0 counter) to correspond with dictionary using a for loop
for i in range(0, len(Question_Answer), 1):
     tally_questions.append(0)

print(tally_questions)

next_round = 'yes'
score = 0
while next_round.upper() == 'YES':

     RandInt = random.randint(0, 3)

     Q_A = list(Question_Answer.items())[RandInt] #turns dict. into list then extracts Q&A PAIR at an index in that new list
     # Q_A = ('Question', 'Answer')
     Q = Q_A[0]
     A = Q_A[1]
     print(Q)

     if input('Answer: ', ).upper() == A.upper(): 
          print('Congratulations! You got the answer correct.')
          score += 1
          
     else:
          print('ER-OR! Wrong, wrong, wrong, better luck next time lad.')

     next_round = input('\nWould you like to continue to the next round? [Yes/No]', )


print('\nThank you for practicing your work. Your score is: ', score, '\nRemember: a question a day keeps the uncertainty away!')
