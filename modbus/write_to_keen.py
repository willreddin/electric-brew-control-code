#!/usr/bin/env python

import redlionPAX2C
import supmeaph
import keen

keen.project_id = "5946670495cfc96449fc36b2"
keen.write_key = "8B11486923BC787F6EAC3DC72FBF1C4414E3AA86AE074F12F17680B7E0689A947291C83062553B7EB17FC278A3740BDA2BCE994C3CBCB135035A3ADA03A6ED0C7373D4CFC1006D74F79455E7B7AA7D4E93892F059CA5CE89743051E159F88EE7"
keen.read_key = "5152D8ED91BE5277A812764FE1200A4D4981E0459A57BBEF5D27B257209ABDD9F159119716497F83F9C7A05D1A80F6617DF908B7F8C7EA35AD12BEC2DA7E42BCB2B86942686DDBA42F4F837C0B1550B5ED30F4212EDBB120C41F3DB359565ECA"

tempController = redlionPAX2C.redlionPAX2C('INSERTSERIALADDRESSHERE',1)

phController = supmeaph.supmeaph('INSERTSERIALADDRESSHERE',2)

#Get HLT/Boil temp
boilTemp = tempController.get_pv()
boilSetTemp = tempController.get_active_sp()

keen.add_event("boil_temp", {
	"temp": boilTemp,
	"setTemp": boilSetTemp
	})

#Get Mash Tun temp
mashTemp = phController.get_temp()

keen.add_event("mash_temp", {
	"temp": mashtemp
	})

#Get Mash Tun PH
mashPH = phController.get_ph()

keen.add_event("mash_ph", {
	"ph": mashPH
	})


