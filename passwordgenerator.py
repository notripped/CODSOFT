import random
import string
x=int(input("Enter number of characters for password: "))
z=int(input("""Enter complexity of password
        1:Only numbers
        2:Only characters
        3:Numbers and characters
        4:Numbers,Characters and special characters: """))
choice="N"
while choice!="Y":
  y=""
  if(z==1):
     for i in range(x):
        random_char=random.choice(string.digits)
        y=y+random_char
  elif(z==2):
      for i in range(x):
          random_char=random.choice(string.ascii_letters)
          y+=random_char
  elif(z==3):
        for i in range(x):
          random_char=random.choice(string.digits+string.ascii_letters)
          y=y+random_char
  elif(z==4):
        for i in range(x):
          random_char=random.choice(string.digits+string.ascii_letters+string.punctuation)
          y=y+random_char
  print("The password generated is :"+y)
  print("""Are you satisfied with the password
      Press Y for yes or N for no""")
  choice=input()       
  choice=choice.upper() 
    
