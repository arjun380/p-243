from web3 import Web3
from web3.middleware import geth_poa_middleware

API_url = 'https://mainnet.infura.io/v3/ec5qcb117dc468c9f3ee9a84a02fe98'
web3 = Web3(Web3.HTTPProvider(API_url))

Block_data = web3.eth.get_block(latest)
print('Block data:',latest)


transaction = web3.eth.get_block_transaction_count(13042315)
print('Number of trasnsactions are:',transaction)

transaction_fee = web3.eth.fee_history(4,'latest',None)
print('Number of trasnsactions history are:',transaction_fee)