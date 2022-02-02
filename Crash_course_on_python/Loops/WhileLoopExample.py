# Simple while loop that iterates through the function until the condition
# is no longer met.


def attempts(n):
    x = 0
    while x <= n:
        print("Not yet met! " + str(x))
        x += 1
    print("Completed")


attempts(20)
