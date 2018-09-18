# Author: Angie Dowdell
# Program Name: AngieDowdellL11.py
# Purpose: rock, paper, scissor modified
# Date: March 3, 2016



import random




def main(userWin,comWin):
      userWin=0
      compWin=0

      while userWin <2 and compWin<2:
            user_pick= eval(input('Choose your weapon! Enter 0 for scissor, 1 for rock, 2 for paper, q to quit: '))
      #Invalid Input
            if (user_pick != '0') or (user_pick != '1') or (user_pick != '2'):
                  user_pick= eval(input('You may only enter a 0,1, or 2. Choose your weapon: '))



      #Determine Results
            user_pick= int(user_pick)
            c=computerResponse()
            winner=determineWin(user_pick,c)
      #Annouce Results

            if winner==0:
                  userWin=userWin+1
                  print("You win!")

            elif winner==1:
                  compWin=compWin+1
                  print("You lose!")
            elif winner==-1:
                  print("You tie!")

##            if userWin> compWin:
##
##                  print("You win!")
##            elif compWin> userWin:
##                  print("You lose!")
            print("Player: ", userWin)
            print("Computer: ", compWin)
##
##      if user_pick== 'q' or compWin>=2 or userWin>=2:
##            print ("Final score: ")
##            print("Player: ", userWin)
##            print("Computer: ", compWin)
##            print("Goodbye!")





def computerResponse():

      computer= random.randint(0,2)
      return computer

def determineWin(user_pick, computer):
       # It's a Draw
      if (computer==0) and (user_pick==0):
            print('The computer is scissor. You are scissor too! It is a draw.')
            return -1
      elif (computer==1) and (user_pick==1):
            print('The computer is rock. You are rock too! It is a draw.')
            return -1
      elif (computer==2) and (user_pick==2):
            print('The computer is paper. You are paper too! It is a draw.')
            return -1

      # You win!

      if (computer==0) and (user_pick==1):
            print('The computer chose scissor. You chose rock.')
            return 0
      elif (computer==1) and (user_pick==2):
            print('The computer chose. You chose.')
            return 0
      elif (computer==0) and (user_pick==2):
            print('The computer chose. You chose paper.')
            return 0

      # You lose:(

      elif (computer==1) and (user_pick==0):
            print('The computer chose rock. You chose scissor.')
            return 1
      elif (computer==2) and (user_pick==1):
            print('The computer chose paper. You chose rock.')
            return 1
      elif (computer==2) and (user_pick==0):
            print('The computer is scissor. You chose paper. ')
            return 1

print ('Welcome to paper, rock, scissor!')
user_pick= eval(input('Choose your weapon! Enter 0 for scissor, 1 for rock, 2 for paper, q to quit: '))
if user_pick=='q' or user_pick=='Q' or user_pick=='quit' or user_pick=='Quit':
      print("YESSS IT WORKSS!!!")
##      userWin=main(userWin)
##      compWin=main(compWin)
##      print ("Final score: ")
##      print("Player: ", userWin)
##      print("Computer: ", compWin)
##      print("Goodbye!")
else:
      user_pick= eval(input('Choose your weapon! Enter 0 for scissor, 1 for rock, 2 for paper, q to quit: '))




     

