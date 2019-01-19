from user import User
from transaction import Transaction
from tabulate import tabulate
from test_data import Test_Data
from block import Block

users = []
tx_pool = []
test_data = Test_Data()
blockchain = []

users, tx_pool = test_data.load_test_data(users, tx_pool)


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
        if len(tx_pool) > 0:
            print('|    4    |  Show Tx Pool    |')
        print('|    5    |  Mine a Block    |')
        if len(blockchain) > 0:
            print('|    6    |  Print Blocks    |')
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
            print_tx_pool()
        elif response == '5':
            create_block()
        elif response == '6':
            print_blocks()
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
    tx_pool.append(transaction)
    print(tx_pool)


def print_users():
    table_data = []
    headers = ['User #', 'Name']
    for index, user in enumerate(users, start=1):
        table_data.append([index,
                           user.print_user_info_short()])

    print(tabulate(table_data, headers, tablefmt="grid"))


def print_tx_pool():
    table_data = []
    headers = ['ID', 'Sender', 'Recipient', 'Amount', 'Time']
    for tx in tx_pool:
        table_data.append([tx.id,
                           tx.sender.get_name(),
                           tx.recipient.get_name(),
                           tx.amount,
                           tx.get_time()])
    print(tabulate(table_data, headers, tablefmt="grid"))


def create_block():
    block = Block(blockchain, tx_pool)
    blockchain.append(block)
    print('New Block Added!')
    for _ in range(len(tx_pool)):
        tx_pool.pop()


def print_blocks():
    for block in blockchain:
        print('-'*30)
        print('Block height: ' + str(block.height))
        print('Block hash: ' + block.hash)
        print('Transactions: ')
        table_data = []
        headers = ['ID', 'Sender', 'Recipient', 'Amount', 'Time']
        for tx in block.tx_pool:
            table_data.append([tx.id,
                            tx.sender.get_name(),
                            tx.recipient.get_name(),
                            tx.amount,
                            tx.get_time()])
            print(tabulate(table_data, headers, tablefmt="grid"))

user_menu()
