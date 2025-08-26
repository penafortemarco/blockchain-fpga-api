from ecdsa import SigningKey, SECP256k1
from hashlib import sha256
from time import time
from src.core import Blockchain, Block, mine_block

class StaticNode:
    """
    StaticNode can only share preprogrammed votes, and
    are made to be the simplest type of test nodes.

    Create the object defining (or not) private and
    public addresses, or the script will provide it.
    You can also pass a Blockchain object to provide
    past blockchain data.
    """

    def __init__ (
        self,
        private_address: str = "",
        public_address: str = "",
    ):
        
        if(not (private_address or public_address)):
            priv_key = SigningKey.generate(SECP256k1, hashfunc=sha256)
            priv_key.verifying_key
            self.private_address = priv_key.to_string().hex()
            self.public_address = priv_key.get_verifying_key().to_string().hex()
        
        else:
            self.private_address = private_address
            self.public_address = public_address 
        

 

    def test_mine_and_check(self):
        blockchain = Blockchain()
        b = Block(blockchain.chain[0].get_block_hash())
        b = mine_block(b)
        blockchain.add_block(b)


    """
    Selects a random node from 'options' using the modulus between a node own
    public_address (just for test purposes) and the lenght of 'options'.
    The vote is hashed (sha256) because votes need to be 32-bytes.
    """
    def test_vote(self, options: list["StaticNode"]):
        selected_node = options[int(self.public_address, base=16) % len(options)]
        return sha256(selected_node.public_address.encode()).digest()