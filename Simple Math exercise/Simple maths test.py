import random as rd
from inputimeout import inputimeout as it, TimeoutOccurred
c = 0
s = 0
t = 5

i = input("\nHow many questions will you like to try(Input must be digits):")
while i.isnumeric() == False:
    print('Wrong input! Input must be numeric')
    i = input("\nHow many questions will you like to try(Input must be digits):")

level = input("\nChoose your preffered difficulty level:Indicate either '1' for Easy, '2' for Intermediate, '3' for Hard or '4' for Impossible: ")
while not level in ['1','2','3','4']: 
    print("\nIncorrect input!. Indicate either '1' for Easy, '2' for Intermediate, '3' for Hard or '4' for Impossible: ")
    level = input('\nTry again: ')
    
while int(i) > 0:
    if level == '1':
     F_value = rd.randint(1,20)
     S_value = rd.randint(1,20)
     timer = 10
    elif level == '2':
     F_value = rd.randint(20,60)
     S_value = rd.randint(20,60)
     timer = 9
    elif level == '3':
     F_value = rd.randint(60,120)
     S_value = rd.randint(60,120)
     timer = 10
    elif level == '4':
     F_value = rd.randint(100,150)
     S_value = rd.randint(100,150)
     timer = 8   
    compl = rd.choice(['Correct!','Well done','You rock!','Excellent!','You\'re smart!','Bravo!!!'])
    comp = rd.choice(["Wrong answer",'Try again panco!',"You\'ve got this",'You sha o!'])
    c+=1
    print('\nQuestion '+ str(c))
    
    try:
     print('You have '+str(timer)+' seconds to answer')
     ans = it(prompt=""+str(F_value)+" + " + str(S_value)+' = ',timeout=timer)
    
    except (TimeoutOccurred,NameError,ValueError): 
        ans = '0'
        print('Time up!!')
        input('\nInput \"Y\" to continue')
        

    Ans = F_value+S_value
    try:
     if int(ans) == Ans:
        print(compl+'\n')
        s+=1
     else:
        print(comp)
        print('Correct answer:'+str(Ans)+'\n')
    except ValueError:
        ans = '0'
        print('Input must be numeric')  
        print('Correct answer:'+str(Ans)+'\n') 
    i = int(i)-1    

percentage = (s/c)*100
print("\n End of Test")
print('You scored '+ str(s)+' out of '+str(c)+' ('+str(percentage)+'%)\n')       