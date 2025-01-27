import random

def rps(com,me):
    if(com==me):
        return None
    elif(com=='r' and me=='p'):
        return True
    elif(com=='p' and me=='s'):
        return True
    elif(com=='s' and me=='r'):
        return True
    else:
        return False
    
choice=('r','p','s')

com=random.randint(0,2)
com=choice[com]

me=input("Enter r for rock, p for paper or s for scissor: ")
win=rps(com,me)
print(f"you chose {me} computer chose {com}")
if(win==None):
    print('Match drawn')

if(win==True):
    print('You win')
elif(win==False):
    print('Computer wins')

