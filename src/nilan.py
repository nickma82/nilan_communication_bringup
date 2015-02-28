#!/usr/bin/env python

import minimalmodbus
import serial

__author__  = "Nick Ma"

class Nilan( minimalmodbus.Instrument ):
    """Instrument class for nilan heat pump. 
    communication via RS485 
    """
    
    HOLDINGREG_OFFSET = 10000

    def __init__(self, portname, slaveaddress=30):
        minimalmodbus.Instrument.__init__(self, portname, slaveaddress)

        self.serial.baudrate = 19200
        self.serial.parity = serial.PARITY_EVEN
        self.serial.timeout = 0.1

        self.mode = minimalmodbus.MODE_RTU
        
    
    def is_manual_loop1(self):
        """Return True if loop1 is in manual mode."""
        return self.read_register(273, 1) > 0
    
     
    def get_t11Top(self):
        """Return the setpoint (SP) target for loop1."""
        return self.read_register(211, numberOfDecimals=2, 
            signed=True, functioncode=4)
   
    def get_userVent(self):
        """This is a holding register -> functioncode=3"""
        return self.read_register(1003, numberOfDecimals=0, signed=False, functioncode=3) 

    def set_userVent(self, speed=2):
	if (speed<0) or (speed>4):
            return
        return self.write_register(1003, speed)

    
########################
## Testing the module ##
########################

if __name__ == '__main__':

    minimalmodbus._print_out( 'TESTING Nilan Connection')

    n = Nilan('/dev/ttyUSB0')
    n.debug = True
    print(n)

    ## starting demo
    minimalmodbus._print_out( 't11:                    {0}'.format(  n.get_t11Top()             ))
    minimalmodbus._print_out( 'userVentSet:             {0}'.format( n.get_userVent()       ))
    n.set_userVent()
    minimalmodbus._print_out( 'userVentSet:             {0}'.format( n.get_userVent()       ))
    
    minimalmodbus._print_out( 'DONE!' )

pass    
