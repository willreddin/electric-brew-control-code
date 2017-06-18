import minimalmodbus

class SupmeaPH200(minimalmodbus.Instrument):
	"""Instrument class for Supmea PH2oo controller

	Args:
        * portname (str): port name
        * slaveaddress (int): slave address in the range 1 to 247

    """

    def __init__(self, portname, slaveaddress):
    	minimalmodbus.Instrument.__init__(self, portname, slaveaddress)

    def get_ph(self):
    	"""Return PH value"""
    	return self.read_register(1,2)

    def get_temp(self):
    	"""Return temp from controller"""
    	return self.read_register(2,1)

    def get_ORP(self):
    	"""Return ORP value"""
    	return self.read_register(3,0)