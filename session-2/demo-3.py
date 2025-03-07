# Demo 3
#
# Manually converts integer from base 10 to binary
#
# Author: Reina Rowlands (20066312)
# Date: 2025-02-14
#

hot = input("Is it hot today? (Y/N): ").upper()
lecture = input("Do you have a lecture (Y/N): ").upper()

if hot == "Y":
    if lecture == "Y":
        print("Sorry, no swimming and surfing today.")
    else:
        print("What about going to the beach? ")
