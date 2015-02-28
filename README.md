# Nilan (R) modbus communication bringup
That project is supposed to provide software for basic communication with nilan heatpumps, containing the cts-602 control board.

## Software PreRequirements
pytho packages: pyserial, minimalmodbus
installation with pip: pip install pyserial minimalmodbus

## Hardware PreRequiremnts
An RS485 to USB dongle, because Nilan is using modbus on top of the physical RS485 layer.
