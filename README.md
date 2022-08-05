## Bitcoin-Ticker

This project was built with a raspberry pi zero w, a few [[dot matrix displays](https://www.amazon.com/HiLetgo-MAX7219-Arduino-Microcontroller-Display/dp/B07FFV537V/ref=sr_1_10?crid=12JF67LIYCAFN&keywords=dot+matrix+display&qid=1654813940&sprefix=dot+matrix+display%2Caps%2C89&sr=8-10)], and a 3D printed case. Refer to this chart for a [[wiring diagram](https://media.discordapp.net/attachments/741501177560039424/1005160146370039879/Screen_Shot_2022-08-05_at_1.06.35_PM.png)]

Code modifications and 3D printed case was made by [[Nick DiSisto](https://www.linkedin.com/in/nick-disisto-4111291ba/)].
### Prerequisites

Here are a few things you will need before installation. You may be asked to type Y or N during installation.

  ```sh
  sudo apt install python3-pip
  ```
  ```sh
  sudo apt-get install python3-bs4
  ```
  ```sh
  sudo apt install git
  ```
  
  

### Installation



1. Run this command once all pre-requisites are installed
   ```sh
   sudo usermod -a -G spi,gpio pi
   ```
2. Next you'll need this
   ```sh
   sudo apt install build-essential python3-dev python3-pip libfreetype6-dev libjpeg-dev libopenjp2-7 libtiff5
   ```
3. Along with...
   ```sh
   sudo python3 -m pip install --upgrade luma.led_matrix
   ```
4. You'll need clone this repository
   ```sh
   git clone https://github.com/Nick1770/Bitcoin-Ticker.git
   ```
5. You'll need to enable SPI on the raspberry pi
   ```sh
   sudo raspi-config
   ```
Select Interfacing Options, then Select SPI, Finally Select Yes


### First Run
1. Navigate to the correct directory
   ```sh
   cd Bitcoin-Ticker
   ```
2. To see avalibale scrips use this
   ```sh
   ls
   ```
3. To run the main script use
   ```sh
   python3 Ticker.py
   ```
4. Enjoy! If you need to end the script press "ctrl" + "c"
   
   
<p align="right">(<a href="#top">back to top</a>)</p>
