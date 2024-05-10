import question_b

def stock_menu():

    choice = '1'

    while choice != '2':
        choice = input('1 to display stock purchase history or 2 to exit: ')
        handle_menu_option(choice)

def handle_menu_option(choice):
    
    if choice == '1':
        question_b.stock_purchase_history()

    elif choice == '2':
        print('Exiting...')

    else:
        print('Invalid option, please choose 1 or 2')

stock_menu()