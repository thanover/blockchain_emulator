from user import User
from transaction import Transaction

users = []
trans_pool = []

def load_test_data():
    new_user = User('Tom', 'Hanover', users)
    users.append(new_user)
    new_user = User('Liz', 'Hanover', users)
    users.append(new_user)
    new_trans = Transaction(users[0], users[1], 500.00)
    trans_pool.append(new_trans)
    print('Test Data Loaded\n\n')


def user_menu():
    def get_input():
        print('\n')
        print('What would you like to do?')
        print('-'*30)
        print('| option  |   description    |')
        print('-'*30)
        print('|    1    |  Add a new user  |')
        print('|    2    |  See all users   |')
        print('|    3    |  Create a Tx     |')
        if len(trans_pool) > 0:
            print('|    4    |  Show Tx Pool    |')
        print('|    e    | Exit the program |')
        print('-'*30)
        return str(input('Select your Option: '))

    while True:
        response = get_input()
        if response == '1':
            create_user()
            input('Press "Enter" key to continue')
        elif response == '2':
            print_users()
            input('Press "Enter" key to continue')
        elif response == '3':
            create_transaction()
        elif response == '4':
            print_trans_pool()
        elif response == 'e':
            print('goodbye!')
            break


def create_user():
    print('\n')
    print('Please enter the information for this user')
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


def create_transaction():
    print_users()
    print('\n')
    sender_num = int(input('Enter user # for the sender: '))
    sender = users[sender_num - 1]
    recipient_num = int(input('Enter user # for the recipient: '))
    recipient = users[recipient_num - 1]
    amount = float(input('How much is the transaction for? '))
    transaction = Transaction(sender, recipient, amount)
    trans_pool.append(transaction)
    print(trans_pool)


def print_users():
    print('\n' + '-'*30)
    print('|  User #  |  Name\t\t|')
    print('-'*30)
    for index, user in enumerate(users, start=1):
        print('|  ' + str(index) + str(user.print_user_info_short()))
    

def print_trans_pool():
    print('\n' + '-'*58)
    print('| ID            | Sender        | Recipient     | Amount |')
    print('-'*58)
    for transaction in trans_pool:
        print(str(Transaction.get_transaction_info(transaction)))

load_test_data()
user_menu()

