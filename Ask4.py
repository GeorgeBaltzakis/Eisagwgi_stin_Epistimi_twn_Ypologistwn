# Ask 4
"""
Γράψτε ένα κώδικα σε Python ο οποίος να παίρνει σαν είσοδο
ένα αρχείο ASCII κειμένου και να το κόβει σε συνεχόμενες
τριάδες λέξεων (όλες τις δυνατές). Στην συνέχεια, διαλέγει
τυχαία μια τριάδα και προσπαθεί να συντάξει ένα τυχαίο κείμενο
από αυτό, χρησιμοποιώντας τις δυο τελευταίες λέξεις και
επιλέγοντας μια τριάδα που να ξεκινάει από αυτές τις δυο.
Το πρόγραμμα ολοκληρώνεται, όταν γράψει 200 λέξεις ή δεν
μπορεί να επιλεγχεί άλλη τριάδα λέξεων.
"""
import random

# Check Input
while True:
    try:
        path = str(input("Give path of ASCII file: "))
        f = open(path, "r")
        break
    except FileExistsError or FileNotFoundError:
        print("Error")

my_words = list()
my_threes = list()

# List of words
for line in f:
    for word in (line.strip()).split(" "):
        my_words.append(word)
f.close()

# Set threes
for i in range(1, len(my_words) + 1):
    if i % 3 == 0:
        my_threes.append(my_words[i - 3:i])

# Find similar threes !!!
final_txt = ""
n = 3
j = 0
k = random.randrange(0, len(my_threes))
final_txt += my_threes[k][0] + " " + my_threes[k][1] + " " + my_threes[k][2] + " "
while n < 200 and j != len(my_threes):
    # Search for similar
    for i in range(len(my_threes)):
        if i != k and my_threes[i][0] == my_threes[k][1] and \
                my_threes[i][1] == my_threes[k][2]:
            final_txt += my_threes[i][2] + " "
            n += 1
            k = i
            break
    j += 1

# Output text
print("Output:", final_txt)
