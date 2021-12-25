#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2017-18 Richard Hull and contributors
# See LICENSE.rst for details.

import re
import time
import requests
import argparse
from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.virtual import viewport
from luma.core.legacy import text, show_message
from luma.core.legacy.font import proportional, CP437_FONT, TINY_FONT, SINCLAIR_FONT, LCD_FONT



# create matrix device (cascaded referes to number of matrix displays)
serial = spi(port=0, device=0, gpio=noop())
device = max7219(serial, cascaded=24 , block_orientation=-90, rotate=2)
print("Printing Bitcoin and Ethereum prices")

# starts here
while(1):

  #Bitcoin
  bdata = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd")
	bjson = bdata.json()
  print("Bitcoin $" + str (bjson['bitcoin']['usd']))
  
  #Ethereum
  edata = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=usd")
  ejson = edata.json()
  print("Ethereum $" + str (ejson['ethereum']['usd']))
    
  #Dogecoin
	ddata = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=dogecoin&vs_currencies=usd")
	djson = ddata.json()
	print("Dogecoin $" + str (djson['dogecoin']['usd']))

	#Uniswap
	udata = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=uniswap&vs_currencies=usd")
	ujson = udata.json()
	print("Uniswap $" + str (ujson['uniswap']['usd']))

	#The Graph
	gdata = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=the-graph&vs_currencies=usd")
	gjson = gdata.json()
	print("The Graph $" + str (gjson['the-graph']['usd']))

	#NuCypher
	ndata = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=nucypher&vs_currencies=usd")
	njson = ndata.json()
	print("NuCypher $" + str (njson['nucypher']['usd']))

	#Safemoon
	sdata = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=safemoon&vs_currencies=usd")
	sjson = sdata.json()
	print("SafeMoon $" + str (sjson['safemoon']['usd']))
    
  #WadzPay
	sdata = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=wadzpay-token&vs_currencies=usd")
	sjson = sdata.json()
	print("WadzPay $" + str (sjson['wadzpay-token']['usd']))


	# Print message to LED
	show_message(device, "Bitcoin $" + str (bjson['bitcoin']['usd']) + "          " + "Ethereum $" + str (ejson['ethereum']['usd']) + "          " + "Dogecoin $" + str (djson['dogecoin']['usd']) + "          " + "Uniswap $" + str (ujson['uniswap']['usd']) + "          " + "The Graph $" + str (gjson['the-graph']['usd']) + "          " + "NuCypher $" + str (njson['nucypher']['usd']) + "          " + "SafeMoon $" + str (sjson['safemoon']['usd']), fill="white", font=proportional(LCD_FONT),scroll_delay = 0.04)
