from user import User
from transaction import Transaction

class Test_Data:
    
    def load_test_data(self, users, tx_pool):
        new_user = User('Tom', 'Hanover', users)
        users.append(new_user)
        new_user = User('Liz', 'Hanover', users)
        users.append(new_user)
        new_trans = Transaction(users[0], users[1], 500.00)
        tx_pool.append(new_trans)
        new_trans = Transaction(users[1], users[0], 400.00)
        tx_pool.append(new_trans)
        print('Test Data Loaded\n\n')
        return users, tx_pool
