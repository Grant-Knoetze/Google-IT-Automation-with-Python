#!/usr/bin/env python3

def main():
    my_numbers = [1, 35, 514, 1235, 3456, 3, 2, 4]

    # Creating a dictionary with the key as the number and value as the square of the number:
    my_dict = {}
    for n in my_numbers:
        my_dict[n] = n ** 2
    print(my_dict)

    my_numbers2 = [233, 255, 552]
    my_new_dict = {n: n ** 2 for n in my_numbers2}
    print(my_new_dict)

    # Add a conditonal

    my_numbers2 = [233, 255, 552]
    my_new_dict = {n: n ** 2 for n in my_numbers2 if n % 2 == 0}
    print(my_new_dict)


if __name__ == '__main__':
    main()
