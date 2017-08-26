import minimalmodbus

class ClassName(minimalmodbus.Instrument):
	"""Instrument class for Red Lion PAX2C

	Args:
        * portname (str): port name
        * slaveaddress (int): slave address in the range 1 to 247

    """

	def __init__(self, portname, slaveaddress):
		minimalmodbus.Instrument.__init__(self, portname,, slaveaddress)

	def get_pv(self):
		return self.read_register(1,1)

	def get_active_sp(self):
		return self.read_register(2,1)

	def set_active_sp(self, value):
		self.write_register(2, NEW_TEMPERATURE, 1)

	def get_sp1(self):
		return self.read_register(3,1)

	def get_sp2(self):
		return self.read_register(4,1)

	def alarm_1_value(self):
		return self.read_register(6,1)

	def reset_alarm(self):
		self.write_register(23,1,0)
		
