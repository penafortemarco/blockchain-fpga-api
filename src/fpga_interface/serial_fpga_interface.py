# serial_fpga_interface.py
import serial

"""To Do
Receber da serial o resultado e ver se esta correto!!!
"""

STD_SERIAL_PORT = '/dev/tty'
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

        if loopback:
            self._port_instance = serial.serial_for_url('loop://', baudrate, timeout=timeout)
        else:
            self._port_instance = serial.Serial(port, baudrate, timeout=timeout)


    def __exit__(self): self.close()


    def close(self):
        if self._port_instance and self._port_instance.is_open: self._port_instance.close()


    def bin_write(self, buffer) -> int | None:
        if not isinstance(buffer, (bytes, bytearray, memoryview)):
            raise TypeError("Error (TypeError): bin_write expects byte-like buffer")
        return self._port_instance.write(buffer)


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
            self._port_instance.write("")

            if verbose: print(f"Sending {data_size} bytes of data...")
            self._port_instance.write(data)
            if verbose: print(f"Data sent! Waiting FPGA response...")

        except serial.SerialException as e:
            print()

        finally:
            return 0