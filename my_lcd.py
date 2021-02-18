import utime

from machine import I2C
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd

I2C_ADDR     = 0x27
I2C_NUM_ROWS = 4
I2C_NUM_COLS = 20

i2c = I2C(0, sda=machine.Pin(0), scl=machine.Pin(1), freq=400000)
lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)

#my custom display commands
#clear screen
lcd.clear()
lcd.move_to(5,0)
lcd.putstr("Howdy")
lcd.move_to(2,1)
lcd.putstr("Tinkernerdz!")
utime.sleep(2)
lcd.clear()
lcd.custom_char(0, bytearray([0x03,
  0x04,
  0x0A,
  0x10,
  0x14,
  0x0B,
  0x04,
  0x03]))
lcd.custom_char(1, bytearray([0x1C,
  0x1B,
  0x15,
  0x0F,
  0x0B,
  0x14,
  0x1B,
  0x1C]))
lcd.custom_char(2, bytearray([0x18,
  0x04,
  0x0A,
  0x01,
  0x05,
  0x1A,
  0x04,
  0x18]))
lcd.custom_char(3, bytearray([0x07,
  0x1B,
  0x15,
  0x1E,
  0x1A,
  0x05,
  0x1B,
  0x07]))
lcd.move_to(0,0)
lcd.putchar(chr(0))
lcd.move_to(1,0)
lcd.putchar(chr(2))
lcd.move_to(2,0)
lcd.putchar(chr(1))
lcd.move_to(3,0)
lcd.putchar(chr(3))
utime.sleep(5)
