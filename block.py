from transaction import Transaction
import hashlib

class Block:
    def __init__(self, blockchain, tx_pool):
        self.height = len(blockchain) + 1
        self.tx_pool = tx_pool.copy()
        self.get_hash()

    def get_hash(self):
        concat_tx_ids = ''
        for tx in self.tx_pool:
            concat_tx_ids += str(tx.id)
        m = hashlib.sha256()
        m.update(concat_tx_ids.encode('utf-8'))
        self.hash = 'b_' + m.hexdigest()[0:10]
        