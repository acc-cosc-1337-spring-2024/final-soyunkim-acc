import question_d

def multiplication_main():
    choice = '1'

    while choice != '2':
        choice = input('To continue, 1 for multiplication table or 2 for exit: ')
        handle_menu_option(choice)

def handle_menu_option(choice):

    if choice == '1':
        num1 = int(input('Enter the 1st number: '))
        num2 = int(input('Enter 2nd number: '))

        table = question_d.create_multiplication_table(num1, num2)

        question_d.display_multiplication_table(table)

    elif choice == '2':
        print('Exiting...')

    else:
        print('Invalid choice, choose between 1 or 2')

multiplication_main()