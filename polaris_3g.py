from base import *
from devices import *

class Polaris3G(Board):

    @staticmethod
    def match(dev):
        return dev["vid"]=="0483" and dev["pid"] in "5740" and dev.get("sid")=="POLARIS10V3G"

    def reset(self):
        import time
        conn = ConnectionInfo()
        conn.set_serial(self.port,**self.connection)
        conn.baudrate = 2400
        ch = Channel(conn)
        try:
            ch.open(timeout=2)
            ch.close()
        except:
            pass
        time.sleep(0.5) # wait to get CDC port after reset

    def burn(self,bin,outfn=None):
        return False,"Must be put in DFU mode first!"

    def put_dfu(self, outfn=None):
        # put in dfu mode
        conn = ConnectionInfo()
        conn.set_serial(self.port, **self.connection)
        conn.baudrate = 1200
        ch = Channel(conn)
        try:
            ch.open(timeout=2)
            ch.close()
        except:
            pass
        return True, ''
