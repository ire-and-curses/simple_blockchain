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
