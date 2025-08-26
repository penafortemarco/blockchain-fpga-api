import serial

class MockNode:

    def __init__(
        self,
        port: str,
        baudrate: int,
        timeout: int,
    ):
        self.port = port
        self.baudrate = baudrate
        self.timeout = timeout
    

    def open(self):
        try:
            self.serial_instance = serial.Serial(
                self.port,
                self.baudrate,
                timeout=self.timeout
            )
        except serial.SerialException as e:
            print("Serial fucked up!")
            exit()

    def close(self): self.serial_instance.close()

    def is_readable(self) -> bool:
        return self.serial_instance.readable()
    
    def wait_until_syn(self):
        i = self.serial_instance.read_until(b"SYN", None)
        print(i)
        
        