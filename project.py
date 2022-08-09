from random import sample
from users import usernames

class InvalidUserError(Exception):
    def __init__(self,m):
        self.msg=m
    def __str__(self):
        return "User name or pwd Incorrect \n"+self.msg
def menu():
    print("1.Add Questions")
    print("2.Take Assements & Final Score :")
    print("3.Exit")

def addQS():
    print("\t 1.Through Console...")
    print("\t 2.File Copy...")
    c=int(input("Enter your choice :"))
    if c==1:
        print("...Through Console...")
        fqb=open("QBank.txt","a")
        q=input("Enter the question :")
        op1=input("OP1 :")
        op2=input("OP2 :")
        op3=input("OP3 :")
        op4=input("OP4 :")
        ans=input("Answer is :")
        fqb.write(q+"#"+op1+"#"+op2+"#"+op3+"#"+op4+"#"+ans+"\n")
        fqb.close()
    elif c==2:
        print(".....File Copying....")
        fname=input("Enter the File Name:")
        fp=open(fname,"r")
        fc=fp.read()
        fqb=open("QBank.txt","a")
        fqb.write(fc)
        fp.close()
        fqb.close()
uname=input("Enter the User Name :")
pwd=input("Enter the Password :")
# Compare this uname Ans pwd with the users.py dictionary content
if usernames.get(uname)==pwd:
    print("Valid User")

else:
    print("Invalid User")
    try:
        raise InvalidUserError(uname)
    except InvalidUserError as ob:
        print(ob)
    exit()

while True:
    menu()
    ch=int(input("Enter your choice :"))
    if ch==1:
        addQS()
    elif ch==2:
        score=0
        print("Take Assements :")
        n=int(input("How many Questions you would like to have in Assements :"))
        fqb=open("QBank.txt","r")
        QL=fqb.readlines()
        #print(type(QL))
        fqb.close()
        #print(QL)
        RL=sample(QL,n)
        #print(RL)
        for Q in RL:
            #print(Q)
            Q=Q.strip()
            #print(Q)
            Q=Q.split("#")
            #print(Q)
            Qname=Q[0]
            op1=Q[1]
            op2=Q[2]
            op3=Q[3]
            op4=Q[4]
            ans=int(Q[5])
            print("Q :",Qname)
            print("1.",op1)
            print("2.",op2)
            print("3.",op3)
            print("4.",op4)
            a=int(input("Enter Your Answer :"))
            if a==ans:
                #print("Good")
                score=score+1
            else:
                score=score-0.25
                #print("Better luck")
        print("Your Final Score is :",score)

    elif ch==3:
        print("Thanks for Taking Assements..")
        exit()
