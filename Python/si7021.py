"""
SI7021 humidity and temperature sensor
Technical notes of commands and operation and from:
https://www.silabs.com/documents/public/data-sheets/Si7021-A20.pdf

 Author : Howard Webb
 Date   : 06/20/2018
 
"""

import RPi.GPIO as GPIO
import time
from I2CUtil import I2C, bytesToWord
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)
GPIO.output(7, GPIO.LOW)

print("Pin 7 is now low")


# Device I2C address
addr = 0x40
rh_no_hold = 0xF5      # Use and do own time hold
previous_temp = 0xE0   # Works but should not use

rh_hold = 0xE5         # Not used
temp_hold = 0XE3       # Not used
temp_no_hold = 0xF3    # Use but do own hold
temp_from_rh = 0xE0    # Not used
reset_cmd = 0xFE       # Available
write_reg_1 = 0xE6     # Not used
read_reg_1 = 0xE7      # Not used
# Heater control
write_heater_reg = 0x51 # Not doing callibration and fancy stuff at this time
read_heater_reg = 0x11  # ditto
# Unique ID for this chip
read_id_1_1 = 0xFA     # Available option
read_id_1_2 = 0x0F     # Available option
read_id_2_1 = 0xFC     # Available option
read_id_2_2 = 0xC9     # Available option
# Firmware revision
firm_rev_1_1 = 0x84
firm_rev_1_2 = 0x88

class SI7021(object):

   def __init__(self):
      self._addr = addr
      self._i2c = I2C(addr)
 
   def calc_humidity(self, read):
      """Calculate relative humidity from sensor reading
           Args:
               read: the sensor value
           Returns:
               rh: calculated relative humidity
           Raises:
               None
      """
      rh = ((125.0*read)/65536.0)-6.0
      return rh

   def calc_temp(self, read):
      """Calculate relative humidity from sensor reading
           Args:
               read: the sensor value
           Returns:
               tempC: calculated temperature in Centigrade
           Raises:
               None
      """
      tempC = ((175.72*read)/65536.0)-46.85
      return tempC

 
   def get_humidity(self):
       """Get the humidity
           Args:
               None
           Returns:
               rh: calculated relative humidity
           Raises:
                None
       """
       #print ("\nGet Humidity - no hold split")
       msgs = self._i2c.msg_write([rh_no_hold])
       # need a pause here between sending the request and getting the data
       time.sleep(0.03)
       msgs = self._i2c.msg_read(3)
       if msgs == None:
           return None
       else:
           value = bytesToWord(msgs[0].data[0], msgs[0].data[1])
           rh = self.calc_humidity(value)
           return rh

   def get_tempC(self):
       """Get the temperature (new reading)
           Args:
               None
           Returns:
               tempC: calculated temperature in Centigrade
           Raises:
               None
       """
   #    print "\nGet Temp - no hold split"
       msgs = self._i2c.msg_write([temp_no_hold])
       # need a pause here between sending the request and getting the data
       time.sleep(0.03)
       msgs = self._i2c.msg_read(3)
       if msgs == None:
           return None
       else:
           value = bytesToWord(msgs[0].data[0], msgs[0].data[1])
           return self.calc_temp(value)

      
    
def test():
    """Test the SI7021 functions
        Args:
            None
        Returns:
            None
        Raises:
            None
   """
    si = SI7021()
   # print ("\nTest Humidity - split")
    rh = si.get_humidity()        
    if rh != None:
        print('Humidity : %.2f %%' % rh)
    else:
        print ("Error getting Humidity")

    #print ("\nTest Temp - split")
    temp = si.get_tempC()
    if temp == None:
        print( "Error getting Temp")
    else:        
        print('Temp C: %.2f C' % temp)        

if __name__ == "__main__":
    test()