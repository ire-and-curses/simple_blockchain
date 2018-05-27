#!/usr/bin/env python

'''
block.py - Simple linked hashes for simulating basic blockchain concepts

Author: Eric Saunders
May 2018
'''

import hashlib

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
                    str(self.idx) +
                    str(self.timestamp) + 
                    str(self.data) + 
                    str(self.prev_hash)
                  )

        return sha.hexdigest()
