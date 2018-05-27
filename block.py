#!/usr/bin/env python

'''
block.py - Simple linked hashes for simulating basic blockchain concepts

Author: Eric Saunders
May 2018
'''

import hashlib
from datetime import datetime


def create_genesis_block():
    return Block(idx=0, timestamp=datetime.utcnow(),
                 data="Genesis Block", prev_hash="0")


def create_next_block(prev_block):
    next_idx = prev_block.idx + 1
    next_timestamp = datetime.utcnow()
    next_data = "This is block number {}'s data".format(str(next_idx))

    return Block(next_idx, next_timestamp, next_data, prev_block.hash)



class Block(object):
    def __init__(self, idx, timestamp, data, prev_hash):
        self.idx       = idx
        self.timestamp = timestamp
        self.data      = data
        self.prev_hash = prev_hash
        self.hash      = self.get_hash()


    def get_hash(self):
        '''Simple hash function to uniquely identify each block. The hash
           includes the previous block so that the chain is immutable.'''

        sha = hashlib.sha256()
        sha.update(
                    (
                        str(self.idx) +
                        str(self.timestamp) + 
                        str(self.data) + 
                        str(self.prev_hash)
                     ).encode('utf-8')
                  )

        return sha.hexdigest()


if __name__ == "__main__":
    root = create_genesis_block()

    blockchain = [root]
    prev_block = root
    for i in range(10):
        block = create_next_block(prev_block)
        blockchain.append(block)
        print("Added block {} with data '{}' and hash '{}' to blockchain".format(
              block.idx, block.data, block.hash))

        prev_block = block

    print()
    print("Final blockchain size = {}".format(len(blockchain)))
