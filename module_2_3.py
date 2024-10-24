my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
my_list.remove(0)
x = 0
y = len(my_list)
while x < y:
    if my_list[x] >= 0:
        print(my_list[x])
        x += 1
        continue