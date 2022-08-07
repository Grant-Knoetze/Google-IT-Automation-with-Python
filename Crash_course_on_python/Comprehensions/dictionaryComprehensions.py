#!/usr/bin/env python3

def main():
    my_numbers = [1, 35, 514, 1235, 3456, 3, 2, 4]
    my_letters = ["l", "k", "l", "j", "h", "a", "h", "h"]
    my_letters_and_numbers = {}
    for number in my_numbers:
        for letter in my_letters:
            if my_numbers.index(number) == my_letters.index(letter):
                my_letters_and_numbers[number] = letter
    print(my_letters_and_numbers)

    my_letters_and_numbers2 = {number: letter for number in my_numbers for letter in my_letters
                               if my_numbers.index(number) == my_letters.index(letter)}
    print(my_letters_and_numbers2)

    # Creating a dictionary with the key as the number and value as the square of the number:
    my_dict = {}
    for n in my_numbers:
        my_dict[n] = n ** 2
    print(my_dict)

    my_numbers2 = [233, 255, 552]
    my_new_dict = {n: n ** 2 for n in my_numbers2}
    print(my_new_dict)

    # Add a conditional

    my_numbers2 = [233, 255, 552]
    my_new_dict2 = {n: n ** 2 for n in my_numbers2 if n % 2 == 0}
    print(my_new_dict2)

    my_numbers2 = [233, 255, 552, 553, 231]
    my_new_dict3 = {n: n ** 2 for n in my_numbers2 if n in range(233, 553)}
    print(my_new_dict3)


if __name__ == '__main__':
    main()
