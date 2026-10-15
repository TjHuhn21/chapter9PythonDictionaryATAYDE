valid_action = ['a', 'b', 'c']
information = dict()
def print_display_main_menu():
    print('a. Add Data')
    print('b. Delete Data')
    print('c. End')

while True:
    print_display_main_menu()
    action = input('Select action: ')
    if action not in valid_action:
        continue

    if action.lower() == 'a':
        key = input('Enter a key: ')
        value = input('Enter a value: ')
        information[key] = value
        print(information)
    elif action.lower() == 'b':
        key = input('Enter a key:')
        if key in information:
            information.pop(information[key])
            print(information)

    elif action.lower() == 'c':
        print('THANK YOU. Program will now end')
        exit()
