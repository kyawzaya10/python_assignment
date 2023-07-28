for x in range(1, 101):
    print(x)

my_num = int(input("Enter your number: "))

if my_num % 2 == 0:
    print(my_num, "is even")
else:
    print(my_num, "is odd")

my_list = [1, 5, 2, 7, 8, 9, 200, 155]
max_number = my_list[0]
for y in my_list:
    if y > max_number:
        max_number = y

print(max_number)


