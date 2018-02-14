# oinCoin - simple blockchain

## What is it? 
The goal of this project is to create a blockchain project to learn more about how blockchains work. This project is not intented to grow into a useful project for others, rather it is for my own exploration of blockchain technologies. 

## Use of code
As of right now this is only a simple api for generating a blockchain. You can store a block of data in an oinCoin blockchain using the Chain object: 
New chain:
''' 
chain(<data>
'''
Add new block to chain:
'''
chain.new_link(<data>
'''
If you want to take a look at your data simply call: 
'''
print chain
''' 

Example usage:
'''
>>> test = oincoin.Chain("stuff")
>>> test.new_link("stuff2")
>>> print(test)
+-------+---------------+------------------------------------------------------+
| Index | Delta t (sec) |                       Address                        |
+=======+===============+======================================================+
| 0     | 0.000         | 000001d52e6ba0d08be3f8fd2d54a088568be43acb6bf56479ba |
|       |               | 5dc09efdd12b78d94e08aaaea77cf4141063244d9bc48801a582 |
|       |               | 84ab237709c95e8fd0829357                             |
+-------+---------------+------------------------------------------------------+
| 1     | 20.954        | 0000086b73d7238ec3755a07683a7281ff402aef8ef43b14f0d9 |
|       |               | cfe4c2067f323bc896a85d5da0789a4117037e0f61bf399bcf84 |
|       |               | f6531ad94d424472f5c47ba0                             |
+-------+---------------+------------------------------------------------------+
'''



## Potential Future uses
I hope to build this blockchain API out for use in the following potential projects:
-- Smart Contract builder web app
-- Crypto-Voting simulator web app 
# oinCoin- blockchain pigs
## What is it? 
The goal of this project is to create a blockchain themed around pigs

## Why?
I am pursuing this project as a way to explore blockchain technology, improve my python code, and hopefully build up to work on smart contracts and some other interesting blockchain technologies. 

## Notes:
This thing is not going to be a useful blockchain. It's for fun, not for any real world value
