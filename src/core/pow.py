# src/core/blockchain.py

from .block import Block


def validate_pow(block: Block) -> bool:
    """
    Returns True if, and only if, hash has the difficulty leading zeroes
    """
    return block.get_block_hash().startswith('0' * block.difficulty)


def mine_block(block: Block) -> Block:
    while not validate_pow(block):
        block.nonce += 1
    return block
    