def working_w_list():
    numbers = []

    list_num = input('Enter 5 of numbers separated by commas: ')
    values = list_num.split(',')

    for val in values:
        numbers.append(float(val))

    minimum = min(numbers)
    maximum = max(numbers)
    total = sum(numbers)
    average = total / len(numbers)

    print(f'Minimum value: {minimum}\n'
          f'Maximum value: {maximum}\n'
          f'Total value: {total}\n'
          f'Average value: {average}')

    