#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2017-18 Richard Hull and contributors
# See LICENSE.rst for details.
# Additions by Nick DiSisto

import re
import time
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
print("Nick is Awesome!")

# start demo
msg ="Nick is Awesome!"
while(1):
	print(msg)
	#Displays msg in all 4 fonts at differnt speeds
	show_message(device, msg, fill="white", font=proportional(CP437_FONT),scroll_delay = 0.02)
	show_message(device, msg, fill="white", font=proportional(SINCLAIR_FONT),scroll_delay = 0.03)
	show_message(device, msg, fill="white", font=proportional(LCD_FONT),scroll_delay = 0.04)
	show_message(device, msg, fill="white", font=proportional(TINY_FONT),scroll_delay = 0.04)
	with canvas(device) as draw:
		text(draw, (0, 0), msg, fill="white", font=proportional(LCD_FONT))

