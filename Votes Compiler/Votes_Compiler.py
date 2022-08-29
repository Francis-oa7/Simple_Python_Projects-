import numpy as np
import pickle
import os


def file_dey(n):
    n+='.txt'
    if os.path.exists(n):
        print('\nData from this portfolio already exist.')
        ans = input('Would you like to override (y/n): ')
        while not ans in ['y','n']:
            print('Wrong input!')
            ans = input('Would you like to override (y/n): ')
        if ans == 'n':
            print('Run the program again and choose option "2" to update existing data..')
            exit()
        else:
            print('Overriding current data...')


def view_results(n):
    
    if os.path.exists(n+'.txt'):
        with open(portfolio[prompt2]+'.txt','rb') as f:
            store = pickle.load(f)
        total = store[0]
        names = store[1]
        cl = 0
        for contestant in range(1,int(len(names))+1):  
            print(str(names[cl])+'\'s total votes: '+str(total[cl])+' representing--- '+str(round(total[cl]/np.sum(total)*100,4))+'%')    
            cl+=1
    else:
        print('\nNo results exist for '+n+' portfolio')
    




portfolio = {'1':"President",'2':"General Secretary",'3':"Treasurer"}
prompt1 = input('What are we doing. Input \'1\' to input new data, \'2\' to update data and \'3\' to view existing results: ')
while not prompt1 in ['1','2','3']:
    print('\nWrong input. Try again')
    prompt1 = input('What are we doing. Input \'1\' to input new data, \'2\' to update data and \'3\' to view existing results: ')
prompt2 = input('Which portfolio are we working on. Input \'1\' for President, \'2\' for General Secretary or \'3\' for Treasurer: ')
while not prompt2 in ['1','2','3']:
    print('\nWrong input. Try again.')
    prompt2 = input('Which portfolio are we working on. Input \'1\' for President, \'2\' for General Secretary or \'3\' for Treasurer: ')


names = []
cb = 1
total = 0

if prompt1 == '1':
    file_dey(portfolio[prompt2])
    prompt1a = input('How many contestants: ')
    while prompt1a.isnumeric() == False:
        print('\nWrong input. Try again')
        prompt1a = input("How many contestants: ")
        "A loop to collect the names of the contestants and storing them in a list"
    for cc in range(1,int(prompt1a)+1):
        a = input('Name of Contestant '+str(cc)+': ').capitalize()
        names.append(a)
    prompt1b = input("Number of available halls: ")
    while prompt1b.isnumeric() == False:
        print('\nWrong input. Try again')
        prompt1b = input("Number of available halls: ")

    """Iteration for number of halls with an inside loop to collect the number of votes for each
     contestant"""
    while int(prompt1b) > 0: 
        print('\nHall '+str(cb))
        print('Votes must be in numbers!!!')
        ca = 0
        votes = []
        votesc = []

        for i in range(1,int(prompt1a)+1):
           v = input(str(names[ca])+"\'s votes: ")
           votes.append(int(v))
           votesc.append(0)
           ca+=1
        sum = np.array(votes) + np.array(votesc)
        total+=sum
        cb+=1
        prompt1b = int(prompt1b) - 1
        store = [total,names]
        """ The array is then saved into a file to make updating possible """
    with open(portfolio[prompt2]+'.txt','wb') as f:
            #f.write(str(total)+'\n')
        pickle.dump(store,f)
            #f.write(str(names))

        """Outputting the total votes of each candidate using a loop with a list of their names
         in the same order as the sum in the 'total' array """
    print()
    cl = 0
    for contestant in range(1,int(prompt1a)+1):  
     print(str(names[cl])+'\'s total votes: '+str(total[cl]))    
     cl+=1      
elif prompt1 == '2':
    try:
     with open(portfolio[prompt2]+'.txt','rb') as f:
        #total = f.readline()
        store = pickle.load(f)
        #names = f.readline()
    except:
        print('\nYou don\'t have data for this portfolio. Run the program again and input \'1\' to input new data.')
        exit() 
    'The names and total votes stored as an array are read from the file and assigned to the variables below'       
    
    total = store[0]#np.array([int(x) for x in total.replace('[','').replace(']','').split()])
    names = store[1]#[n for n in names.replace('[','').replace(']','').replace('\'','').split(',')]
    
    prompt1b = input("Number of available halls: ")
    while prompt1b.isnumeric() == False:
        print('\nWrong input. Try again')
        prompt1b = input("Number of available halls: ")
    while int(prompt1b) > 0: 
        print('\nHall '+str(cb))
        print('Votes must be in numbers!!!')
        ca = 0
        votes = []
        votesc = []

        for i in range(1,int(len(names))+1):
           v = input(str(names[ca])+"\'s votes: ")
           votes.append(int(v))
           votesc.append(0)
           ca+=1
        sum = np.array(votes) + np.array(votesc)
        total+=sum
        cb+=1
        prompt1b = int(prompt1b) - 1
        store = [total,names]
    with open(portfolio[prompt2]+'.txt','wb') as f:
        #f.write(str(total)+'\n')
        pickle.dump(store,f)
        #f.write(str(names))

        """Outputting the total votes of each candidate using a loop with a list of their names
         in the same order as the sum in the 'total' array """
    print()
    cl = 0
    print('TOTAL')
    for contestant in range(1,int(len(names))+1):  
     print(str(names[cl])+'\'s total votes: '+str(total[cl])+' representing--- '+str(round(total[cl]/np.sum(total)*100,4))+'%')    
     cl+=1

elif prompt1 == '3':
    view_results(portfolio[prompt2])
     