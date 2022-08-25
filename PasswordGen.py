import random
import string

# Generate a strong password
# Characteristcs of strong password
## >= 12 characters
## Mixture of uppercase & lowercase 
## Mixture of letters & numbers
## Inclusion of special characters "! @ # $ ? [ ]"

listofchar = []
numofchar = 0

for c in (chr(i) for i in range(32, 127)):
    listofchar.append(c)

while numofchar < 12:
    numofchar = int(input("How long is your password? "))
    if numofchar < 12:
        print("You need a longer password")

newpassword = ''

for i in range(numofchar):
    newpassword += listofchar[random.randint(0,len(listofchar)-1)]

print(f"Your generated password is {newpassword}")