from time import time
from . import Block

class Blockchain:
    """
    Blockchain class
    """

    def __init__ (
        self,    
        difficulty: int = 32,
        chain: list[Block] = None,
    ) -> None:
        self.difficulty = difficulty
        self.chain = chain if chain is not None else []
        if not self.chain:
            self.chain.append(self.genesis_block())
    
    @classmethod
    def genesis_block(cls) -> Block:
        return Block(prev_block_hash = '')
    
    def add_block(self, block: Block) -> "Blockchain":
        self.chain.append(block)
        return self
    
    def check_block(self, index = -1) -> bool:
        if index == 0:
            return (self.chain[0].prev_block_hash == '')
        
        current_block = self.chain[index]
        past_block = self.chain[index - 1]
        return (
            current_block.prev_block_hash == past_block.get_block_hash()
            and current_block.validate_pow(self.difficulty)
        )
