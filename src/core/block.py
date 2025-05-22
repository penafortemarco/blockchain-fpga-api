import json
from time import time
from hashlib import sha256

class Block:
    """
    Block representations class

    
    """
    def __init__ (
        self,
        prev_block_hash: str,        
        merkle_root: str = "",
        data: str = "",
        nonce: int = 0,
        timestamp: int = None,
    ):
        """
        - Params: 'nonce' and 'timestamp' default to 0 and current time. 
        'data' and 'merkle_root' are empty by default. 
        'prev_block_hash' is mandatory for a block in the chain.

        
        - Serialization: uses json.dumps() with sort_keys=True to ensure 
        deterministic hashing across identical block data.
        """
        self.prev_block_hash = prev_block_hash
        self.timestamp = timestamp if timestamp is not None else int(time())
        self.nonce = nonce
        self.merkle_root = merkle_root
        self.data = data

    def get_block_hash(self):
        """
        Returns the block hash (SHA256).
        """
        block_str = json.dumps(self.__dict__, sort_keys=True)
        return  sha256(block_str.encode()).hexdigest()
    
    def validate_pow(self, difficulty: int):
        """
        Returns True only if hash has the difficulty leading zeroes
        """
        block_hash = self.get_block_hash()
        return block_hash.startswith('0' * difficulty)
    
    def __repr__(self):
        """
        Block JSON string.
        """
        return json.dumps(self.__dict__, sort_keys=True)
    
