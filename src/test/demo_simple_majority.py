from src.core import Blockchain
from src.fpga_interface import SerialFPGAInterface
from src.test import StaticNode

def demo_simple_majority(n: int = 200, blockchain = Blockchain()):
    """
    In this demo, we are a mining node that will receive 'n' votes, and we need
    to produce a valid block with each TODO 
    """

    test_nodes = [StaticNode() for _ in range(n)]
    
    fpga = SerialFPGAInterface(loopback=True)
    
    fpga.bin_write(b"SYN")      # Initial message
    buffer = fpga.bin_read(3)
    print(buffer.decode())


    fpga.bin_write(n.to_bytes())    # Number of nodes
    buffer = fpga.bin_read(3)
    print(int.from_bytes(buffer))

    for t_node in test_nodes:
        fpga.bin_write(t_node.public_address.encode())
        buffer = fpga.bin_read(64)
        print(f"Pub: {buffer.hex()}")
        fpga.bin_write(t_node.test_vote(test_nodes))
        buffer = fpga.bin_read(64)
        print(f"Vot: {buffer.hex()}")
        print("---")