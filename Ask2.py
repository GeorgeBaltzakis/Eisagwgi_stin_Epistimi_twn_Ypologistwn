# Ask 2
"""
Γράψτε ένα κώδικα σε Python ο οποίος ελέγχει αν ο ν όρος
της ακολουθίας Fibonacci είναι πρώτος ή όχι. Για να απαντήσετε
αν ένας αριθμός p είναι πρώτος θα πρέπει για 20 τυχαίες
επιλογές του a να ισχύει ότι a ^ p = a mod p. Ο κώδικάς σας
παίρνει τον όρο της ακολουθίας Fibonacci από το χρήστη.
"""
import random


# Make the Fibonacci number
def fib(k):

    if k == 0:
        return 0
    elif k == 1:
        return 1
    else:
        return fib(k - 1) + fib(k - 2)


# Check
while True:
    try:
        n = int(input("Give n: "))
        if n > 1:
            break
        else:
            print("Value Error")
    except ValueError:
        print("Value Error")

my_fib = fib(n)
print("F(n) =", my_fib)
i = 0
# Is it Prime?
if my_fib > 2:
    for i in range(20):
        a = random.randrange(1, 100)
        if (((a ** my_fib) - a) % my_fib) != 0:
            break
    if i == 19:
        print("It's Prime Number")
    else:
        print("It's not Prime Number")
else:
    print("It's Prime Number")
