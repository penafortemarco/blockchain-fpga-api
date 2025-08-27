# serial_fpga_interface.py
import serial

"""To Do
Receber da serial o resultado e ver se esta correto!!!
"""

STD_SERIAL_PORT = '/dev/pts/4'
STD_SERIAL_BAUD_RATE = 9600
STD_SERIAL_TIMEOUT = 5

class SerialFPGAInterface:
    """
    Writable port for communication with FPGA
    - port (ex: COM1, /dev/ttyUSB0, ...)
    - baudrate (ex: 9600, 19200, 38400, ...)
    - timeout

    - virtual: when True, FPGAInterface will interact with a loop of itself. 
    Every 'write' will loopback and be instantly readable!
    """
    
    def __init__ (
        self,
        port: str = STD_SERIAL_PORT,
        baudrate: int = STD_SERIAL_BAUD_RATE,
        timeout: int = STD_SERIAL_TIMEOUT,
        
        loopback = False,
    ):
        self.port = port
        self.baudrate = baudrate
        self.timeout = timeout
        self.loopback = loopback

    def open(self): 
        if self.loopback:
            self._port_instance = serial.serial_for_url('loop://', self.baudrate, timeout=self.timeout)
        else:
            self._port_instance = serial.Serial(self.port, self.baudrate, timeout=self.timeout)


    def __exit__(self): self.close()


    def close(self):
        if self._port_instance and self._port_instance.is_open: self._port_instance.close()


    def bin_write(self, buffer) -> int | None:
        if not isinstance(buffer, (bytes, bytearray, memoryview)):
            raise TypeError("Error (TypeError): bin_write expects byte-like buffer")
        
        try:
            return self._port_instance.write(buffer)
        except serial.SerialException:
            return 0

    def bin_read(self, buffer_size) -> bytes:
        return self._port_instance.read(buffer_size)
    
    def send_and_recv(self, data: bytes, verbose: bool = False):
        """
        Sends the codified data to the FPGA over a serial connection and waits 
        for a response from the FPGA.
        - data: bytes, bytearray or memoryview
        - verbose: enables print statements for debug
        """
        
        if not isinstance(data, (bytes, bytearray, memoryview)):
            raise TypeError("Error (TypeError): bin_write expects byte-like buffer")

        data_size = len(data)

        try:
            self._port_instance.write(b"SYN")
            self._port_instance.write(b"")

            if verbose: print(f"Sending {data_size} bytes of data...")
            self._port_instance.write(data)
            if verbose: print(f"Data sent! Waiting FPGA response...")

        except serial.SerialException as e:
            print()

        finally:
            return 0