#!/usr/bin/env python

'''
block.py - Simple linked hashes for simulating basic blockchain concepts

Author: Eric Saunders
May 2018
'''

import hashlib
from datetime import datetime


def create_genesis_block():
    '''Factory for simple genesis block, to seed the hashing for the subsequent
       blockchain.'''

    return Block(idx=0, timestamp=datetime.utcnow(),
                 data="Genesis Block", prev_hash="0")


def create_next_block(prev_block):
    '''Simple factory to build test blocks linked by hash.'''

    next_idx = prev_block.idx + 1
    next_timestamp = datetime.utcnow()
    next_data = "This is block number {}'s data".format(str(next_idx))

    return Block(next_idx, next_timestamp, next_data, prev_block.hash)


class Block(object):
    '''A Block is a very basic container which knows its chain position, has a
       timestamp, stores arbitrary data, and has a link to the hash of the
       previous Block in the chain.'''

    def __init__(self, idx, timestamp, data, prev_hash):
        self.idx = idx
        self.timestamp = timestamp
        self.data = data
        self.prev_hash = prev_hash
        self.hash = self.get_hash()

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
    '''Demonstrates a simple blockchain in action.'''

    n_blocks = 10
    print("Creating blockchain with {} blocks (plus one".format(n_blocks)
          + " extra for dummy genesis block)\n")

    root = create_genesis_block()

    blockchain = [root]
    prev_block = root
    for i in range(n_blocks):
        block = create_next_block(prev_block)
        blockchain.append(block)
        print("Added block {} with data '{}' and hash '{}' to blockchain".format(
              block.idx, block.data, block.hash))

        prev_block = block

    print("\nFinal blockchain size = {}".format(len(blockchain)))
