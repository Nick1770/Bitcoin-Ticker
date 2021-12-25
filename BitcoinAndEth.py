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



# create matrix device
serial = spi(port=0, device=0, gpio=noop())
device = max7219(serial, cascaded=8 , block_orientation=-90, rotate=2)
print("Printing Bitcoin and Ethereum prices")

# starts here
while(1):

	bdata = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd")
	bjson = bdata.json()
	print("Bitcoin $" + str (bjson['bitcoin']['usd']))

	edata = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=usd")
	ejson = edata.json()
	print("Ethereum $" + str (ejson['ethereum']['usd']))


	# Print message to LED
	show_message(device, "Bitcoin $" + str (bjson['bitcoin']['usd']), fill="white", font=proportional(LCD_FONT),scroll_delay = 0.04)
	show_message(device, "Ethereum $" + str (ejson['ethereum']['usd']), fill="white", font=proportional(LCD_FONT),scroll_delay = 0.04)


