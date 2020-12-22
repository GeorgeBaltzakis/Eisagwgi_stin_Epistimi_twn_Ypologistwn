# Ask 9
"""
Γράψτε ένα κώδικα σε Python ο οποίος να παίρνει σαν είσοδο
ένα αρχείο ASCII κειμένου και μετατρέπει τον κάθε χαρακτήρα
στον αντίστοιχο αριθμό ASCII και κρατάει τους μονούς.
Εμφανίστε τα στατιστικά εμφάνισης του κάθε γράμματος με
“μπάρες” χρησιμοποιώντας το χαρακτήρα *,
όπου κάθε * αντιστοιχεί σε 1%
"""


# Check Input
while True:
    try:
        path = str(input("Give path of ASCII file: "))
        f = open(path, "r")
        break
    except FileExistsError or FileNotFoundError:
        print("Error")

file_txt = f.read()
my_chars = [" "]
f.close()

for i in file_txt:
    if ord(i) % 2 == 1:
        for j in range(len(my_chars)):
            if i == my_chars[j][:1]:
                my_chars[j] += i
                break
            elif j == len(my_chars) - 1:
                my_chars.append(str(i))
                break

for i in range(1, len(my_chars)):
    print(my_chars[i][:1], "*" * int(len(my_chars[i]) / len(file_txt) * 100))
