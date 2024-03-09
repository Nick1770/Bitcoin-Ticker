#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2017-18 Richard Hull and contributors
# See LICENSE.rst for details.
# Additions by Nick DiSisto

import requests
from os import device_encoding
from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.virtual import viewport
from luma.core.legacy import text, show_message
from luma.core.legacy.font import proportional, CP437_FONT, TINY_FONT, SINCLAIR_FONT, LCD_FONT
import time

# Create matrix device
serial = spi(port=0, device=0, gpio=noop())
device = max7219(serial, cascaded=24 , block_orientation=-90, rotate=2)
print("Printing Bitcoin and Ethereum prices")

while True:
    try:
        # Fetch coin prices
        bdata = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin%2Cethereum%2Cbinancecoin%2Cripple%2Cdogecoin%2Cuniswap%2Cthe-graph%2Csafemoon-2%2Ccrypto-com-chain%2Csafuu&vs_currencies=usd")
        bjson = bdata.json()

        # Print coin prices to console
        print("Bitcoin $" + str (bjson['bitcoin']['usd']))
        print("Ethereum $" + str (bjson['ethereum']['usd']))
        print("BNB $" + str (bjson['binancecoin']['usd']))
        print("XRP $" + str (bjson['ripple']['usd']))
        print("Dogecoin $" + str (bjson['dogecoin']['usd']))
        print("Uniswap $" + str (bjson['uniswap']['usd']))
        print("Crypto.com Coin $" + str (bjson['crypto-com-chain']['usd']))
        print("The Graph $" + str (bjson['the-graph']['usd']))
        print("SafeMoon $" + str (bjson['safemoon-2']['usd']))
        print("SAFUU $" + str (bjson['safuu']['usd']))

        # Print message to LED
        show_message(device, "Bitcoin $" + str (bjson['bitcoin']['usd']) + "          " +\
            "Ethereum $" + str (bjson['ethereum']['usd']) + "          " +\
            "BNB $" + str (bjson['binancecoin']['usd']) + "          " +\
            "XRP $" + str (bjson['ripple']['usd']) + "          " +\
            "Dogecoin $" + str (bjson['dogecoin']['usd']) + "          " +\
            "Uniswap $" + str (bjson['uniswap']['usd']) + "          " +\
            "Crypto.com Coin $" + str (bjson['crypto-com-chain']['usd']) + "          " +\
            "The Graph $" + str (bjson['the-graph']['usd']) + "          " +\
            "SafeMoon $" + str (bjson['safemoon-2']['usd']) + "          " +\
            "SAFUU $" + str (bjson['safuu']['usd']) + "          " ,\
            fill="white", font=proportional(LCD_FONT), scroll_delay=0.04)

    except Exception as e:
        print(f"An error occurred: {e}")
        print("Waiting 60 seconds before trying again...")
        time.sleep(60)
