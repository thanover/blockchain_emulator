from user import User

users = []
trans_pool = []


def user_menu():
    def get_input():
        print('\n')
        print('What would you like to do?')
        print('-'*30)
        print('| option  |   description    |')
        print('-'*30)
        print('|    1    |  Add a new user  |')
        print('|    2    |  See all users   |')
        print('|    e    | Exit the program |')
        print('-'*30)
        return str(input('Select your Option: '))

    while True:
        response = get_input()
        if response == '1':
            create_user()
        elif response == '2':
            get_users()
        elif response == 'e':
            print('goodbye!')
            break


def create_user():
    print('\n')
    print('Please enter the information for this user?')
    print('-'*30)
    first_name = str(input('Enter their First Name: '))
    last_name = str(input('Enter their Last Name: '))
    new_user = User(first_name, last_name, users)
    users.append(new_user)
    print('-'*30)
    print('\n')
    print('-'*30)
    print('New User Created!')
    print('User Id: ' + new_user.id)
    print('First Name: ' + new_user.first_name)
    print('Last Name: ' + new_user.last_name)
    print('-'*30)
    input('Enter any key to continue')


def get_users():
    for user in users:
        print(user.print_user_info())

    input('Enter any key to continue')


user_menu()
