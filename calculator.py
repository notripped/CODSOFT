import math
ch="N"
while(ch=="N"):
  print("Input two operands:")
  x=int(input())
  y=int(input())
  print("Enter the type of operation you want to perform")
  print("""List of operations are :
      + - addition
      - - subtraction
      * - multiplication
      / - division
      % - remainder calculation""")
  z=input()
  if z=='+':
    print("Result="+str(x+y))
  elif z=='-':
    print("Result="+str(x-y))
  elif z=='*':
    print("Result="+str(x*y))
  elif z=='/':
    print("Result="+str(x/y))
  elif z=='%':
    print("Result="+str(x%y))
  else:
      print("Wrong input please enter a the operations entered above")
  ch=input("""Are You satisfied with the operations
           If yes then enter Y else enter N:""")
  ch=ch.upper()