import minimalmodbus

class SupmeaPH( minimalmodbus.Instrument):
    
    def __init__(self, portname, slaveaddress):
        minimalmodbus.Instrument.__init__(self, portname, slaveaddress)
    
    def get_ph(self):
        """Return PH value"""
        return self.read_register(0,0)
    
    def get_temp(self):
        """Return temp from controller"""
        return self.read_register(1,0)
    
    def get_ORP(self):
        """Return ORP value"""
        return self.read_register(2,0)
        
    
    

