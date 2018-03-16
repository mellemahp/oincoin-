from context import oincoin
import unittest


class TestFunctions(unittest.TestCase):
    """ Tests General purpose functions of the oincoin module"""
    def test_hashify(self):
        """Verifies sha256 hashing works properly
        Ensures that the SHA-256 output is equal to that of test vectors from:
        https://www.di-mgt.com.au/sha_testvectors.html
        """
        test_vectors = {"abc": "ddaf35a193617abacc417349ae20413112e6fa4e89a97ea20a9eeee64b55d39a2192992a274fc1a836ba3c23a3feebbd454d4423643ce80e2a9ac94fa54ca49f",
                        "": "cf83e1357eefb8bdf1542850d66d8007d620e4050b5715dc83f4a921d36ce9ce47d0d13c5d85f2b0ff8318d2877eec2f63b931bd47417a81a538327af927da3e",
                        "abcdbcdecdefdefgefghfghighijhijkijkljklmklmnlmnomnopnopq": "204a8fc6dda82f0a0ced7beb8e08a41657c16ef468b228a8279be331a703c33596fd15c13b1b07f9aa1d3bea57789ca031ad85c7a71dd70354ec631238ca3445"}

        for key, result in test_vectors.items():
            self.assertEqual(oincoin.hashify(key), result)

    def test_check_address(self):
        self.assertEqual(oincoin.check_address(oincoin.PREFIX), oincoin.PREFIX)
        print()
        with self.assertRaises(Exception):
            oincoin.check_address('111')

class TestBlocks(unittest.TestCase):
    def check_init(self):
        test_block = oincoin.Block.init(1,oincoin.PREFIX, "Test")

class TestChain(unittest.TestCase):

if __name__ == '__main__':
    unittest.main()
