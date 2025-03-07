# Strings revisited
#
# Manually converts integer from base 10 to binary
#
# Author: Reina Rowlands (20066312)
# Date: 2025-03-07
#

tic_tic= "- X 0\n"+"X - X\n"+"0 - 0\n"

#write the code to print the length of the string
print(len(tic_tic))

#write the code to print only the 13th character
print(tic_tic[12])

#write the code to show only the first 5 characters
print(tic_tic[:5])

#write the code the show only characters 8 to 10
print(tic_tic[7:9])

#write code to print every other character
print(tic_tic[0:18:2])
print(tic_tic[::2])

#various other tricks
print(tic_tic.lower())
print(tic_tic.upper())
print(tic_tic.title())
print(tic_tic[0:5].center(50))
print(tic_tic.capitalize())
print(tic_tic.replace("0", "p"))
print(tic_tic.swapcase())
print(tic_tic)