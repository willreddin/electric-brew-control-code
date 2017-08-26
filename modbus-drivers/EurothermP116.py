import minimalmodbus

class EurothermP116(minimalmodbus.Instrument):

	def __init__(self, portname, slaveaddress):
		minimalmodbus.Instrument.__init__(self, portname, slaveaddress)

	def get_pv(self):
		"""Return temp from boil controller"""
		return self.read_register(1,1)

	def get_sp(self):
		"""Return set point from boil controller"""
		return self.read_register(2,1)

	def set_sp():
		return self.write_register(2,1)