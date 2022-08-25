#!/usr/bin/env python3

# Set will return unique items

set_nums = {1, 2, 4, 4, 4, 6, 0, 44, 5, 2}
set_cities = {'Johannesburg', 'Cape Town', 'Bloemfontein', 'Port Elizabeth'}
list_nums = [33, 5, 56, 7, 4, 73, 73, 7, 2, 7, 8, 2, 7]


def main():
    set_list_nums = set()
    for n in list_nums:
        set_list_nums.add(n)
        print(type(set_list_nums))
        print(set_list_nums)


# Do the same using a set comprehension

set_list_nums_comp1 = {n for n in list_nums}

if __name__ == '__main__':
    main()
