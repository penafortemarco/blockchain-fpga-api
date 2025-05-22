"""To Do
Receber da serial o resultado e ver se esta correto!!!
"""

SERIAL_PORT = '/dev/pts/5'
SERIAL_BAUD_RATE = 9600
SERIAL_TIMEOUT = 1

import serial
from flask import Flask
from .test_nodes import StaticNode

""" 
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>lOl</p>" 
"""

test_nodes = [StaticNode() for _ in range(5)]

ser = serial.Serial(SERIAL_PORT, SERIAL_BAUD_RATE, timeout=SERIAL_TIMEOUT)

for t_node in test_nodes:
    vote = t_node.test_vote(test_nodes)
    ser.write(vote)
    print(vote.hex())



