def create_multiplication_table(row, col):
    multiplication_list = []

    r = 0

    while r < row:
        c = 0

        while c < col:
            num = (r + 1) * (c + 1)
            multiplication_list.append(num)
            c += 1        

        multiplication_list.append('\n')
        r += 1


    return multiplication_list

def display_multiplication_table(list):
    for num in list:
        print(str(num).rjust(3, " "), end=" ")
