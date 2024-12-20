#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2017-18 Richard Hull and contributors
# See LICENSE.rst for details.
# Additions by Nick DiSisto Copyright (c) 2024

import requests
import socket
from os import device_encoding
from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.virtual import viewport
from luma.core.legacy import text, show_message
from luma.core.legacy.font import proportional, CP437_FONT, TINY_FONT, SINCLAIR_FONT, LCD_FONT
import time
from datetime import datetime

# Give the pi time to boot
time.sleep(60)

# Create matrix device
serial = spi(port=0, device=0, gpio=noop())
device = max7219(serial, cascaded=24 , block_orientation=-90, rotate=2)

# Get the IP address of the wlan0 interface
def get_ip_address(ifname):
    import fcntl
    import struct
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15].encode('utf-8'))
    )[20:24])

ip_address = get_ip_address('wlan0')
print(f"Device WLAN0 IP address: {ip_address}")
show_message(device, f"Device WLAN0 IP address: {ip_address}", fill="white", font=proportional(LCD_FONT),scroll_delay = 0.06)
print("Printing Bitcoin and Ethereum prices")

def is_within_time_range():
    # Get the current time
    current_time = datetime.now().time()

    # Define the start and end times (9:00 AM to 10:00 PM)
    start_time = datetime.strptime("09:00:00", "%H:%M:%S").time()
    end_time = datetime.strptime("22:00:00", "%H:%M:%S").time()

    # Check if the current time is within the defined range
    return start_time <= current_time <= end_time

while True:
    if is_within_time_range():
        try:
            # Fetch coin prices
            bdata = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin%2Cethereum%2Csolana%2Csui%2Chedera-hashgraph%2Ctron%2Cthe-open-network%2Cbinancecoin%2Cripple%2Cdogecoin%2Cuniswap%2Cthe-graph%2Csafemoon-2%2Ccrypto-com-chain%2Ctrust-wallet-token%2Cmister-miggles%2Csafuu&vs_currencies=usd")
            bjson = bdata.json()

            # Print coin prices to console
            print("Bitcoin $" + str(bjson['bitcoin']['usd']))
            print("Ethereum $" + str(bjson['ethereum']['usd']))
            print("Solana $" + str(bjson['solana']['usd']))
            print("Sui $" + str(bjson['sui']['usd']))
            print("Hedera $" + str(bjson['hedera-hashgraph']['usd']))
            print("BNB $" + str(bjson['binancecoin']['usd']))
            print("XRP $" + str(bjson['ripple']['usd']))
            print("Dogecoin $" + str(bjson['dogecoin']['usd']))
            print("Uniswap $" + str(bjson['uniswap']['usd']))
            print("TWT $" + str(bjson['trust-wallet-token']['usd']))
            print("Tron $" + str(bjson['tron']['usd']))
            print("Ton $" + str(bjson['the-open-network']['usd']))
            print("Cronos $" + str(bjson['crypto-com-chain']['usd']))
            print("The Graph $" + str(bjson['the-graph']['usd']))
            print("Miggles $" + str(bjson['mister-miggles']['usd']))
            print("SafeMoon $" + str(bjson['safemoon-2']['usd']))
            print("SAFUU $" + str(bjson['safuu']['usd']))

            # Print message to LED
            show_message(device, "Bitcoin $" + str(bjson['bitcoin']['usd']) + "          " + \
                        "Ethereum $" + str(bjson['ethereum']['usd']) + "          " + \
                        "Solana $" + str(bjson['solana']['usd']) + "          " + \
                        "Sui $" + str(bjson['sui']['usd']) + "          " + \
                        "Hedera $" + str(bjson['hedera-hashgraph']['usd']) + "          " + \
                        "BNB $" + str(bjson['binancecoin']['usd']) + "          " + \
                        "XRP $" + str(bjson['ripple']['usd']) + "          " + \
                        "Dogecoin $" + str(bjson['dogecoin']['usd']) + "          " + \
                        "Uniswap $" + str(bjson['uniswap']['usd']) + "          " + \
                        "TWT $" + str(bjson['trust-wallet-token']['usd']) + "          " + \
                        "Tron $" + str(bjson['tron']['usd']) + "          " + \
                        "Ton $" + str(bjson['the-open-network']['usd']) + "          " + \
                        "Cronos $" + str(bjson['crypto-com-chain']['usd']) + "          " + \
                        "The Graph $" + str(bjson['the-graph']['usd']) + "          " + \
                        "Miggles $" + str(bjson['mister-miggles']['usd']) + "          " + \
                        "SafeMoon $" + str(bjson['safemoon-2']['usd']) + "          " + \
                        "SAFUU $" + str(bjson['safuu']['usd']) + "          ", \
                        fill="white", font=proportional(LCD_FONT), scroll_delay=0.04)

        except Exception as e:
            print(f"An error occurred: {e}")
            print("Waiting 60 seconds before trying again...")
            time.sleep(60)
    else:
        print("It's not time yet")
        time.sleep(60)
