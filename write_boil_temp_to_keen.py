#!/usr/bin/env python

import EurothermP116
import minimalmodbus
import supmeaph
from keenVariables import *

tempController = EurothermP116.EurothermP116('”/dev/ttyAMA0″',1)

phController = supmeaph.supmeaph('”/dev/ttyAMA0″',2)

#Get HLT/Boil temp
boilTemp = tempController.get_pv()
boilSetTemp = tempController.get_sp()

keen.add_event("boil_temp", {
	"temp": boilTemp,
	"setTemp": boilSetTemp
	})

#Get Mash Tun temp
mashTemp = phController.get_temp()

keen.add_event("mash_temp", {
	"temp": mashTemp
	})

#Get Mash Tun PH
mashPH = phController.get_ph()

keen.add_event("mash_ph", {
	"ph": mashPH
	})


