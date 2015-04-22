# Nilan (R) modbus communication bringup
That project is supposed to provide software for basic communication with nilan heatpumps, containing the cts-602 control board.

## Software PreRequirements
pytho packages: pyserial, minimalmodbus

installation with pip: pip install pyserial minimalmodbus

## Hardware PreRequiremnts
An RS485 to USB dongle, because Nilan is using modbus on top of the physical RS485 layer.

# Connection description
HAZARD NOTE:
If you dont know how to carefully deal with electricity stop here. 
High voltage danger! No warranties.

The cts-602 is inside the heatpump, and the correct connectors are on the
lower left corner on the circuit board (see picture). 
The pins on the RS485 connector have the following order: 

Pin 1	12 VDC output
Pin 2	COM1- RS 485 A - Modbus
Pin 3	COM1 - RS 485 B - Modbus
Pin 4	COM2 - RS 485 A - User panel
Pin 5	COM2 - RS 485 B - User panel
Pin 6	Ground
As you would find it in the MOD-BUS-CTS602-GB.pdf manual.

For the modbus connection you need the pins 2,3,6. 
In the picture pins two and three are not connected.
