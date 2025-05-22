from ecdsa import SigningKey, SECP256k1
from hashlib import sha256
from ..core import Blockchain, Block

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
        private_address: str = '',
        public_address: str = '',
    ):
        
        if(not (private_address or public_address)):
            priv_key = SigningKey.generate(SECP256k1)
            self.private_address = priv_key.to_string().hex()
            self.public_address = priv_key.get_verifying_key().to_string().hex()
        
        else:
            self.private_address = private_address
            self.public_address = public_address 
        

    def mine(self, block: Block, difficulty: int) -> Block:
        while not block.validate_pow(difficulty):
            block.nonce += 1
        return block
    

    def test_mine_and_check(self):
        blockchain = Blockchain(difficulty=4)
        b = Block(blockchain.chain[0].get_block_hash())
        b = self.mine(b, 4)
        blockchain.add_block(b)
        print(blockchain.check_block(1))

    """
    Selects a random node from 'options' using the modulus between a node own
    public_address (just for test purposes) and the lenght of 'options'.
    The vote is hashed (sha256) because votes need to be 32-bytes.
    """
    def test_vote(self, options: list["StaticNode"]):
        selected_node = options[int(self.public_address, 16) % len(options)]
        return sha256(selected_node.public_address.encode()).digest()