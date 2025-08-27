from src.core import Blockchain
from src.fpga_interface import SerialFPGAInterface
from src.test import StaticNode


def demo_simple_majority(n: int = 200, blockchain = Blockchain()):
    """
    In this demo, we are a mining node that will receive 'n' votes, and we need
    to produce a valid block with each TODO 
    """

    test_nodes = [StaticNode() for _ in range(n)]
    
    fpga = SerialFPGAInterface("/dev/pts/7")

    try:
        fpga.open()
    except:
        print("Serial open fucked up")
        exit()

    fpga.bin_write(b"SYN")          # Initial message

    fpga.bin_write(n.to_bytes())    # Number of nodes
    i=0
    for t_node in test_nodes:
        i += 1
        print(i)
        if fpga.bin_write(t_node.public_address.encode()) == 0:
            print("Obs", i)
        if fpga.bin_write(t_node.test_vote(test_nodes)) == 0:
            print("Obs2", i)