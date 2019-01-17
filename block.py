class Block:
    def __init__(transactions, height, previous_block):
        self.height = height + 1
        self.transactions = transactions
        self.previous_block = previous_block['hash']

    def make_hash():