# src/core/blockchain.py

from .block import Block
from .pow import validate_pow

class Blockchain:
    """
    Blockchain class
    """

    def __init__ (self, chain: list[Block] = []):
        self.chain = chain or [self._genesis()]
    
    
    @classmethod
    def _genesis(cls) -> Block:
        return Block(prev_block_hash = "", data="I am")
    

    def add_block(self, block: Block) -> "Blockchain":
        self.chain.append(block)
        return self
    

    def check_block(self, index = -1) -> bool:
        if index == 0:
            return (
                self.chain[0].prev_block_hash == '' 
                and validate_pow(self.chain[0])
            )
        
        current_block = self.chain[index]
        past_block = self.chain[index - 1]
        return (
            current_block.prev_block_hash == past_block.get_block_hash()
            and validate_pow(current_block)
        )
