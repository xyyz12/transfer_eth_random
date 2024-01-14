#!/usr/bin/python3

import sys
from web3 import Web3
from infuraUrl import infuraUrl

try:
	walletAddress = sys.argv[1]

except:
	walletAddress = ['0x2C2E5b824EA2BcE625943aF15e1bBD86630B37EF',
				'0xE26a48A2ea0e4ea26a87365cc2f743A05a31ff98',
                '0xeBac01E51b2FB9F84741A57706b0e4D174873471'
                  ]

w3 = Web3(Web3.HTTPProvider(infuraUrl))


def fetchETHBalance(walletAddress):
	balanceInWei = w3.eth.getBalance(walletAddress)
	balanceEth = float(Web3.fromWei(balanceInWei, 'ether'))
	addressBalance = {'address': walletAddress, 'balanceEth': balanceEth}
	return addressBalance

for address in walletAddress:
    balance = fetchETHBalance(address)
    print(f"钱包地址 {address} 的余额为: {balance}")


