#*
#**
#***
#****
#*****
#******

x=int(input("Enter the no. of row "))
for i in range (0,x):
    for j in range (0,i+1):
            print("*",end='')
    print()
    
#******
#*****
#****
#***
#**
#*
    
x=int(input("Enter the no. of row"))
for i in range(0,x):
    for j in range(0,x-i):
          print("*",end='')
    print()

#      *
#     **
#    ***
#   ****
#  *****
# ******


x=int(input("Enter the no. of row"))
for i in range(0,x):
    for j in range(0,x):
        if j>=x-i:
          print("*",end='')
        else:
            print(" ",end='')
    print()


#******
# *****
#  ****
#   ***
#    **
#     *

x=int(input("Enter the no. of row"))
for i in range(0,x):
    for j in range(0,x):
        if j>=i:
          print("*",end='')
        else:
            print(" ",end='')
    print()

#   *
#  ***
# ******
#********

x=int(input("Enter the no. of row"))
y=int(input("Enter the no. of column"))
for i in range(0,x):
    for j in range(0,y):
        if j>=x-i and j<=3+i:
          print("*",end='')
        else:
            print(" ",end='')
    print()

#********
# ******
#  ***
#   *

x=int(input("Enter the no. of row"))
y=int(input("Enter the no. of column"))
for i in range(0,x):
    for j in range(0,y):
        if j>=i and j<8-i:
          print("*",end='')
        else:
            print(" ",end='')
    print()

#1
#12
#123
#1234
#12345
#123456

x=int(input("Enter the no. of row "))
for i in range (1,x):
    for j in range (1,i+1):
            print(j,end='')
    print()


