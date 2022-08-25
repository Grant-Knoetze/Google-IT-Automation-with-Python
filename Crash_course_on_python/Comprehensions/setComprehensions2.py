#!/usr/bin/env python3

jan_2020_jhb_temp = [34, 53, 66, 44, 64, 67, 64, 64, 23, 36, 74, 77, 65, 23, 64, 64]


def main():
    """Convert temperature from fahrenhiet to celsius and ignore
    duplicates.
    c = (f - 32) * (5/9)"""
    #set_jan_2020_jhb_temp_c = set()
    #for f in jan_2020_jhb_temp:
    #    t_celsius = round((f - 32) * (5 / 9), 2)
    #    set_jan_2020_jhb_temp_c.add(t_celsius)
    #print(set_jan_2020_jhb_temp_c)

    # Do the same with a set comprehension
    set_jan_2020_jhb_temp_c_comp = {(round((f - 32) * (5 / 9), 2)) for f in jan_2020_jhb_temp}
    print(set_jan_2020_jhb_temp_c_comp)


if __name__ == '__main__':
    main()
