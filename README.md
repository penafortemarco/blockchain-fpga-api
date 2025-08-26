# Flask API

In order to test the FPGA implementation of validation protocols, communication must be easily established between preprogrammed _Test Nodes_ and the _FPGA Node_. As a first step, we might delegate the work of peer-to-peer communication to a Flask App, to avoid doing it by hand in SystemVerilog. 
This architecture is inspired by the following [paper](https://onlinelibrary.wiley.com/doi/abs/10.1155/2021/9918697). The Flask application corresponds to the _on-chain_ component, while the FPGA Node represents the _off-chain_ component.

## Node Structure

### on-chain (Flask API)
The Flask App is the _on-chain_ component of our Node. It has the purpose of combine the votes into a single message.

### off-chain (FPGA)  
A node is a member in the structure of a blockchain network.
The FPGA component will validate the votes with and will submit a new block


### Test Nodes (Python)
 Here, the test nodes represented by the `TestNode` class, which can be instantiated to vote on proposals (blocks). 
A vote has the following simple structure:
```
{
    "node_public_address": str,
    "vote_proposal": str | int (?),
    "vote_value": str | int (?),
    "vote_signature": str
}
```



## Protocol Implementation
2 Nodes (Miner vs Voter)?
1 Node with two parts?
All in FPGA, Flask just to emulate other Nodes?
## Running

### Communication
The FPGA component acts as a server at the start of communication.
The Node initiates it by sending:
- the ASCII bytes "SYN"
- followed by a 4-byte integer that indicates how many bytes the Node 
  will send over the connection
- and then expects to receive "ACK" from the FPGA before the timeout elapses

The FPGA has a fixed (processing) timeout to send its computation response. 
When the response is ready, the FPGA initiates the communication by sending:
- the ASCII bytes "SYN"
- followed by the 4-byte integer that indicates how many bytes the FPGA 
  will send over the connection
- and then expects to receive "ACK" from the Node before the timeout elapses

## Testing
To ensure a testing of the program logic, we can use a mock_node, in
the mock_test.sh script