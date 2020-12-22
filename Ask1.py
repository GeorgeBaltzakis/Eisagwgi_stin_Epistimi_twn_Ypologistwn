# Ask 1
"""
  Γράψτε ένα κώδικα σε Python ο οποίος να παίρνει την διάσταση
ενός τετραγώνου και θα φτιάχνει μέσα από λίστες τον αντίστοιχο
πίνακα. Στην συνέχεια θα βρίσκει το πλήθος των θέσεων και θα
γεμίζει στην τύχη τις μισές με μονάδες. Σκοπός είναι να
μετρήσετε πόσες τετράδες από μονάδες υπάρχουν οριζόντια,
κάθετα, και διαγώνια. Το πρόγραμμα επαναλλαμβάνεται 100 φορές
(για την ίδια διάσταση) και επιστρέφει τον μέσο όρο των
τετράδων.
"""
import random
d = -1

# Check
while d <= 3:
    try:
        d = int(input("Give n: "))
    except ValueError:
        print("Value Error")
fours = 0

# Four 100 times
for p in range(100):
    # Square Creation
    my_square = [[0 for _ in range(d)] for _ in range(d)]

    # 1s location
    for i in range(int((d**2)/2)):
        while True:
            my_i = random.randrange(0, d)
            my_j = random.randrange(0, d)
            if my_square[my_i][my_j] == 0:
                my_square[my_i][my_j] = 1
                break

    # Output
    """print("\n")
    for row in my_square:
        print(row)"""

    # Horizontally
    for i in range(d):
        ones = 1
        for j in range(d - 1):
            if my_square[i][j] == 1 and my_square[i][j + 1] == 1:
                ones += 1
            if ones == 4:
                fours += 1
                # print("o", i)
                ones = 1

    # Vertically
    for j in range(d):
        ones = 1
        for i in range(d - 1):
            if my_square[i][j] == 1 and my_square[i + 1][j] == 1:
                ones += 1
            if ones == 4:
                fours += 1
                # print("v", j)
                ones = 1

    # Diagonal
    for i in range(d - 3):
        ones = 1
        for j in range(d - 3):
            if my_square[i][j] == 1 and my_square[i + 1][j + 1] == 1 and my_square[i + 2][j + 2] == 1 and my_square[i + 3][j + 3] == 1:
                # if a diagonal have 5 ones then don't count tow fours ( 1 [ 1  1  1 ) 1 ]
                if i < d - 4 and j < d - 4:
                    if my_square[i + 4][j + 4] == 1:
                        ones -= 1
                ones += 1
            if ones == 4:
                fours += 1
                # print("d", i, j)
                ones = 1

# Output
print("Average", fours / 100)
