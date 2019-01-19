from user import User
import time
import hashlib


class Transaction:
    def __init__(self, sender, recipient, amount):
        self.sender = sender
        self.recipient = recipient
        self.amount = amount
        self.time = time.time()
        self.generate_id()

    def generate_id(self):
        concat_name = self.sender.get_id() + self.recipient.get_id() + str(self.time)
        m = hashlib.sha256()
        m.update(concat_name.encode('utf-8'))
        self.id = 'tx_' + m.hexdigest()[0:10]

    def get_time(self):
        return time.asctime(time.localtime(self.time))
