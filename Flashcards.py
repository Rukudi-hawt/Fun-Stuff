Question_Answer = {'Which gas moderates the ozone reaction?' : 'Nitrogen', 'Explain the reaction within the ozone layer?' : 'O3 separates into O2 and O, which then bond together with free particles (i.e. O2 wit free O and vice versa).', 'What is the third layer of the atmosphere?' : 'Mesosphere', 'What is the important gas in the second layer of Earth?' : 'Ozone', 'What is ozone made of?' : 'O3'}

#//TO DO:
#---add condition for multiple answers (i.e. more than 1 word/has spaces)
#---create piles for well known/not known (how would I set probabilities/recurrances based on how known)

# Let's play a GAME!!!
#Guess the answer to the given question. Get it right, and you move on. Get it wrong, and.... let's just say, you probably won't enjoy what comes next :)

import random

next_round = 'yes'
score = 0
while next_round.upper() == 'YES':

     RandInt = random.randint(0, 4)

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
