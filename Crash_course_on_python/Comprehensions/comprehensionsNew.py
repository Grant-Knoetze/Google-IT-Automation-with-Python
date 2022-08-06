my_list = [1, 3, 6, 69, 97, 97]

my_new_list = [n + 10 for n in my_list]
print(my_new_list)

# Adding a conditional
my_better_list = [n + 10 for n in my_list if n >= 10]
print(my_better_list)

# Add a conditional in range
my_best_list = [n + 10 for n in my_list if n in range(1, 4, 2)]
print(my_best_list)