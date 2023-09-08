import random
rando=["rock","paper","scissors"]
choice="Y"
you=0
ai=0
while choice=="Y":
     n=random.randrange(0,3)
     opp=rando[n]
     your=input("Enter your choice rock paper or scissors:")
     your=your.lower()
     if(opp=="rock"and your=="rock"):
         print("""Tied 
               you="""+str(you)+"computer="+str(ai))
     elif(opp=="paper"and your=="paper"):
        print("""Tied 
               you="""+str(you)+"computer="+str(ai))
     elif(opp=="scissors"and your=="scissors"):
        print("""Tied 
               you="""+str(you)+"computer="+str(ai))
     elif(opp=="rock"and your=="scissors"):
        ai=ai+1
        print("Computer won")
        print("You="+str(you))
        print("Computer="+str(ai))
     elif(opp=="scissors"and your=="paper"):
        ai=ai+1
        print("Computer won")
        print("You="+str(you))
        print("Computer="+str(ai))
     elif(opp=="paper"and your=="rock"):
       ai=ai+1
       print("Computer won")
       print("You="+str(you))
       print("Computer="+str(ai))
     elif(opp=="scissors"and your=="rock"):
       you=you+1
       print("You won")
       print("You="+str(you))
       print("Computer="+str(ai))
     elif(opp=="rock"and your=="paper"):
       you=you+1
       print("You won")
       print("You="+str(you))
       print("Computer="+str(ai))
     elif(opp=="paper"and your=="scissors"):
       you=you+1
       print("You won")
       print("You="+str(you))
       print("Computer="+str(ai))
     choice=input("""Do you want to continue
                 Enter Y to continue else N:""")
     choice=choice.upper()
print("""The final scores are:
      You="""+str(you)+"""
      Computer="""+str(ai))
if(you>ai):
  print("You won")
if(you<ai):
  print("Computer won")
   
      
      
    
    

    