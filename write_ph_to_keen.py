import minimalmodbus
import supmeaph
import keen

from keenVariables import *

phController = supmeaph.SupmeaPH('/dev/ttyS0',2)

mashTemp = phController.get_temp()
mashTemp = round(float(mashTemp/10), 2)

keen.add_event("mash_temp", {
	"temp": mashTemp
	})

mashPH = phController.get_ph()
mashPH = round(float(mashPH)/100, 2)

keen.add_event("mash_ph", {
	"ph": mashPH
	})
