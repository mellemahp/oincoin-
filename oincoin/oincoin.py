#!/usr/bin/env python3
'''

'''
import hashlib
import time
import string
import random
from texttable import Texttable

DIFFICULTY = 5 #set the number of leading 0's in valid address

class Chain:
    """ A structure that stores, creates, and validates blocks

    Structure that stores a number of blocks of data with unique hash addresses.
    The address of the newest block on the chain is used to generate the next block's
    address, linking all block's together. Blocks can store any data that can be
    coerced into a string.

    Attributes:
        links (list<Blocks<T>>): a list of Block objects that form the blockchain
    """

    def __init__(self, data):
        """ Creating a genesis block for the blockchain

        The first block in the chain is generated using a random string that
        stands in for a previous block's address. The length of the blockchain,
        the links of the chain, and a table representation of the blockchain can
        be called.

        Args:
           data - data that will be stored in the genesis block

        """
        self.links = [Block(0,random_string(),data)]
        self._table = Texttable() # initializing table for __repr__
        self._table.add_rows([['Index', 'Timestamp', 'Address'],
                             [self.links[0]._index,
                              self.links[0]._timestamp,
                              self.links[0].address]])

    def __len__(self):
        """ returns the number of blocks in the blockchain """
        return len(self.links)

    def __repr__(self):
        """ Returns a table (str) representation of the blockchain

        Provides an ascii string table in the form:

        +-------+-----------+---------------+
        | Index | Timestamp |    Address    |
        +=======+===========+===============+
        | <Int> | <f>e+09   | <Hex address> |
        .  ...  .   ...     .      ...      .
        .  ...  .   ...     .      ...      .
        .  ...  .   ...     .      ...      .
        +-------+-----------+---------------+

        Requires:
            Texttable object from texttable(1.2.1) package
        """

        return self._table.draw()

    def new_link(self, data):
        """ Creates a new block and adds it to the blockchain

        Generates a new block containing the input data, validates that the
        added new block's address conforms to the required number of leading 0s
        and

        Args:
            data <T>: some piece of data to be contained by a block

        Raises:
            "INVALID BLOCK": the number of leading 0's in the blocks address is
                             not at least DIFFICULTY (global <int>)

        """
        new_block = Block(len(self), self.links[len(self) - 1].address, data)
        check_address(new_block.address)
        self.links.append(new_block)
        self._table.add_row([new_block._index,
                            new_block._timestamp,
                            new_block.address])


class Block:
    """ Defines a single block of data with a valid address and metadata

    A single block of data to be added to a blockchain. Contains metadata about
    when the block was generated and a hex  address with DIFFICULTY (global <int>)
    leading 0's

    Note: All blocks other than the genesis block (index = 0 ) must have a previous
        index that meets the required ### of leading 0s
    """

    def __init__(self, index, previous, data):
        """ Creates a new block and initiates "mining" for an address

        Initializes block metadata (time, index, previous block's address) and
        data which is then combined into a string which will be hashed along with
        a nonce to create the block's address in the Block.mine() method.

        Args:
            index <int>: the position of the block in the blockchain
            previous <str>: the hex address of the previous block in the chain
            data <T>: the data you would like to attach to the block

        Raises:
            "INVALID ADDRESS": previous address does not have required # leading 0s

        """
        self._index = index
        self._timestamp = time.time()
        if self._index ==  0:
            self._previous = previous
        else:
            self._previous = check_address(previous)

        self.data = data
        self.nonce = 0
        self.input_str = str(self._index) + str(self._timestamp) + \
                         str(self._previous) + str(self.data)
        self.mine()

    def mine(self):
        """ Defines the proof of work function to find a valid block address

        Operates on a Block class. Incremements an nonce until
        the resulting hash has a number of leading 0's equal to difficulty.

        Initializes attributes:
            address <str> : hex address of the block
            nonce <int>: a number incremented to alter the hash

        """
        prefix = "0" * DIFFICULTY
        self.address = hashify(self.input_str + str(self.nonce))

        while not self.address.startswith(prefix):
            self.address = hashify(self.input_str + str(self.nonce))
            self.nonce += 1

        ## DEBUG ##
        print("Address mined for Block #: {}").format(self._index)
        ## END DEBUG ##


def hashify(input_str):
    """ Hashes an input *string* using the SHA512 hash function
    Args:
        input_str <str>: some string of arbitrary length to hash

    Returns:
        <str>: hashed value of the input string from SHA512 hash function

    """
    return hashlib.sha512(input_str).hexdigest()

def check_address(address):
    """ Checks that an address meets the required criteria
    Args:
        address <str>: a hex address converted to string
    Raises:
        "INVALID ADDRESS": Address does not have required ## of leading 0's
    """
    assert address.startswith("0" * DIFFICULTY),"INVALID ADDRESS"
    return address

def random_string(size=10):
    """ Generates a random string of length size

    Args:
        size <int>: defines the length of the random string to generate

    Returns:
        rand_str <str>: random string of ascii characters

    """
    rand_str = ''.join(random.choice(string.ascii_uppercase + string.digits)
                       for _ in range(size))
    return rand_str


def main():
    Test_Chain = Chain("stuffffz")
    for data in ['stuff','things','stuffthings','thingstuff','stuffthings']:
        Test_Chain.new_link(data)
    print(Test_Chain)

if __name__ == "__main__":
    main()
