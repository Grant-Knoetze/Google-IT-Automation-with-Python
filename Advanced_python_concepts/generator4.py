# Generator pipeline

def get_odd_numbers_squared_and_ending_in_1():
    """if number is odd, square that number,
    if the number ends in 1, print"""
    for n in range(1000):
        if n % 2 != 0:
            n **= 2
            if n % 10 == 1:
                print("Match found ---->{}".format(str(n)))


get_odd_numbers_squared_and_ending_in_1()
