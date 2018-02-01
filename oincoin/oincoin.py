#!/usr/bin/env python3
'''

'''
import numpy as np
import matplotlib as plot
import hashlib
import crypto
import time
import string
import random
from texttable import Texttable

DIFFICULTY = 5

class Chain:
    """
    A structure that stores, creates, and validates blocks
    """
    def __init__(self, data):
        self.table = Texttable()
        self.links = [Block(0,random_string(),data)]
        self.table.add_rows([['Index', 'Timestamp', 'Address'],
                             [self.links[0]._index,
                              self.links[0]._timestamp,
                              self.links[0].address]])

    def __len__(self):
        return len(self.links)

    def __repr__(self):
        return self.table.draw()

    def add_block(self, data):
        current_len = len(self.links)
        New_Block = Block(current_len, self.links[current_len-1].address, data)
        assert New_Block.address.startswith("0" * DIFFICULTY),"INVALID Block"
        self.links.append(New_Block)
        self.table.add_row([New_Block._index,
                            New_Block._timestamp,
                            New_Block.address])


class Block:
    """
    Defines a single block object to add to the blockchain given information about
    the previous block in the chain
    """
    def __init__(self, index, previous, data):
        self._index = index
        self._timestamp = time.time()
        self._previous = previous
        self.data = data
        self.mine()


    def mine(self):
        """
        Takes in an integer difficulty and string. Incremements an nonce until
        the resulting hash has a number of leading 0's equal to difficulty.
        Returns: address
        """
        prefix = "0" * DIFFICULTY
        nonce = 0
        input_string = str(self._index) + str(self._timestamp) + str(self.data) + \
        str(self._previous)

        address = hashify(input_string, nonce)

        while not address.startswith(prefix):
            address = hashify(input_string, nonce)
            nonce += 1

        self.address = address
        self.nonce = nonce
        print("Address mined for Block #: {}").format(self._index)


def hashify(input_str, nonce=0):
    return hashlib.sha512(str(input_str) + str(nonce)).hexdigest()


def random_string(size=10):
    rand_str = ''.join(random.choice(string.ascii_uppercase + string.digits)
                       for _ in range(size))
    return rand_str




Test_Chain = Chain("Kendra is cool")
for data in ['stuff','things','stuffthings','thingstuff','stuffthings']:
    Test_Chain.add_block(data)

print(Test_Chain)
