# Bitcoin-Ticker
  Run these commands before hand
    sudo apt install python3-pip
    Y
    sudo apt-get install python3-bs4
    Y
    sudo apt install git
    Y
    sudo usermod -a -G spi,gpio pi
    sudo apt install build-essential python3-dev python3-pip libfreetype6-dev libjpeg-dev libopenjp2-7 libtiff5
    Y
    sudo python3 -m pip install --upgrade luma.led_matrix

  Also you need to enable SPI
    sudo raspi-config
      Select Interfacing Options
      Select SPI
      Yes
