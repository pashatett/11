my_list = [42, 69, 322, 13, 0, 99, 9, 8, 7, 5]
count = 0

while count < len(my_list):
    num = my_list[count]
    count += 1
    if num == 0:
        continue
    elif num < 0:
        break
    elif count == len(my_list):
        print(num)
    else:
        print(num)
