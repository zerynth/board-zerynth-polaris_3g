from base import *
from devices import *

class Polaris3GDFU(Board):

    @staticmethod
    def match(dev):
        return dev["vid"]=="0483" and dev["pid"]=="DF11"

    def reset(self):
        pass

    def burn(self,bin,outfn=None):
        fname = fs.get_tempfile(bin)
        info("dfustm32l4","-d",self.vid+":"+self.pid,"-a","0","-s","0x08000000:leave","-D",fname)
        res,out,err = proc.runcmd("dfustm32l4","-d",self.vid+":"+self.pid,"-a","0","-s","0x08000000:leave","-D",fname,outfn=outfn)
        fs.del_tempfile(fname)
        if res:
            return False,out
        return True,out
    
    def __init__(self,info={},dev={}):
        super().__init__(info,dev)
        self._info["name"] = "Polaris3G DFU"
        