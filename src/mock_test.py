import sys
from src.test import MockNode

DEFAULT_BAUDRATE = 9600
DEFAULT_TIMEOUT = 1

if len(sys.argv) < 2:
    print("Usage: test.py <PORT>")
    exit()

PORT = sys.argv[1]

mock_node = MockNode(PORT, DEFAULT_BAUDRATE, DEFAULT_TIMEOUT)

mock_node.open()

while(mock_node.is_readable()):
    mock_node.wait_until_syn()




