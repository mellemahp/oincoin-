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
from collections import deque

DIFFICULTY = 5

class Chain:
    """
    A structure that stores, creates, and validates blocks
    """
    def __init__():
        self.links = deque(genesis_block())

    def __len__(self):
        return len(self.links)

    def __dict__(self):
        stuff = 1 
        
    def add_block(self, data):
        current_len = len(self.links)
        New_Block = Block(current_len + 1 , self.links().address, data)
        assert hashify(New_Block.address).starts_with("0" * DIFFICULTY), "INVALID Block" 
        self.links.append(New_Block)   

        
class Block:
    """
    Defines a single block object to add to the blockchain given information about the previous
    block in the chain
    """ 
    def __init__(self, index, previous, data): 
        self.index = index 
        self._timestamp = time.time()
        self._previous = previous
        self.data = data
        self.address, self.nonce = mine(DIFFICULTY, str(self.index + self._timestamp)
                                        + str(data) + str(previous))

        
def mine(diff, input_str):
    """
    Takes in an integer difficulty and string. Incremements an nonce until
    the resulting hash has a number of leading 0's equal to difficulty. 
    Returns: address 
    """
    prefix = "0" * diff
    nonce = 0
    address = hashify(input_str, nonce)
    
    while not address.startswith(prefix):
        address = hashify(input_str, nonce)
        nonce += 1
        
    return address, nonce

def hashify(input_str, nonce):
    return hashlib.sha512(str(input_str) + str(nonce)).hexdigest()


def genesis_block(data):
    """
    Create the first block in a chain
    """
    stuff = 1

def random_string(size=10):
    rand_str = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(size))
    return rand_str

Test_Block = Block(1,200020, "Kendra Rocks")
print(Test_Block.address)

