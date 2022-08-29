import random 

print("\nRock Paper Scissors\n___________________\nPlay \"rock paper scissors\" with your device.\nEach match will be made up of the number of rounds you indicate.\nIndicate either 1 for \"rock\",2 for \"paper\" or 3 for \"scissors\" in the \"Input your choice:\" section.\nHave Fun!")

i = input("\nNumber of rounds in this match:")
win = 0
loss = 0
rou_d = 0
d_ict = {'1':'rock',"2":'paper','3':'scissors'}
while i.isnumeric() == False:
  print("Wrong Input!!")
  print("Input must be a number(eg. 1,2,3,4...)")
  i = input("\nNumber of rounds in this match:")
 
while int(i) > 0:
  try:
   rou_d+=1 
   print('\nRound '+str(rou_d))
   your_choice = d_ict[input('Input your choice:')]#.lower()# add the dict() to use numbers
   rock_paper = ['rock','paper','scissors']
   c_choice = random.choice(rock_paper)
  
   if your_choice in rock_paper: # line no more needed with dict added, but den e be cool so i no go remove
    if your_choice == c_choice:
     print('Your choice: '+your_choice)
     print('Computer\'s choice: '+c_choice)
     print("It\'s a tie")
     win+=0.5
     loss+=0.5
    if your_choice == 'rock' and c_choice == 'scissors' or your_choice == 'paper' and c_choice == 'rock' or your_choice == 'scissors' and c_choice == 'paper':
     print('Your choice: '+ your_choice)
     print('Computer\'s choice: ' + c_choice)
     print(random.choice(['You win!!','Way to go!','You rock!',"Lucky you!"]))
     win+=1   
    if c_choice == 'rock' and your_choice == 'scissors' or c_choice == 'paper' and your_choice == 'rock' or c_choice == 'scissors' and your_choice == 'paper':
     print('Your choice: '+ your_choice)
     print('Computer\'s choice: '+c_choice)
     print(random.choice(['You lose','Better luck next time',"Try again panco!"]))
     loss+=1
   else:
     i+=1
     rou_d-=1
     a = " ".join((i for i in rock_paper if your_choice[0] in i )) # line no longer needed but den i be cool
     print("Wrong spelling of " + a)
  except KeyError:
    print('Wrong input. Input either 1 for \'rock\', 2 for \'paper\' or 3 for \'scissors\'') 
    rou_d-=1
    continue
   
  i=int(i)-1   
print('\nEND OF MATCH')
print("\nYour score:"+str(win))
print("Computer\'s score:"+str(loss))
if win > loss:
    print('You won!!!')
elif win < loss:
    print('You lost')
elif win == loss:
    print("It\'s a Draw")