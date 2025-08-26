# src/core/block.py

from time import time
from hashlib import sha256

HEX64 = 64
STD_DIFFICULTY = 8

class Block:
    """
    Block representations class

    """

    def __init__ (
        self,
        prev_block_hash: str,        
        merkle_root: str = "",
        timestamp: int = int(time()),
        difficulty: int = 0,
        nonce: int = 0,
        data: str = "",
    ):
        """
        - prev_block_hash: is padded auto
        - merkle_root: can be passed if previously calculated, else is the hash of data
        - timestamp: defaults to int(time())
        - difficulty: number of '0' in HEX needed to header's hash be valid
        - nonce: defaults to 0
        - data: string
        
        - Serialization: uses json.dumps() with sort_keys=True to ensure 
        deterministic hashing across identical block data.
        """


        if not all(c in "0123456789ABCDEF" for c in prev_block_hash):
            raise ValueError("Error (ValueError): prev_block_hash must be a 64-hex string")

        l = len(prev_block_hash) 
        if l != 64:
            prev_block_hash = (64 - l)*"0" + prev_block_hash

        self.prev_block_hash = prev_block_hash

        self.merkle_root = merkle_root or sha256(data.encode()).hexdigest()
        
        self.timestamp = timestamp

        self.difficulty = difficulty

        self.nonce = nonce

        self.data = data


    def get_block_header(self):
        """
        Returns the block header in a bytes-like type
        """
        return f"{self.prev_block_hash}{self.merkle_root}{self.timestamp}{self.difficulty}{self.nonce}".encode()


    def get_block_hash(self):
        """
        Returns the block sha256 hash in hexadecimal encoding.
        """
        return sha256(self.get_block_header()).hexdigest()
    
