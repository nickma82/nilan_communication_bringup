# Reference: http://pythonhosted.org/pyModbusTCP/quickstart/index.html#utils-module-modbus-data-mangling
from pyModbusTCP.client import ModbusClient
from pyModbusTCP import utils

c = ModbusClient(host="192.168.1.35", port=502, unit_id=30, auto_open=True)
c.open()
if not c.is_open():
	raise Exception("could not connect")

list_16_bits = c.read_input_registers(211, 2)
list_32_bits = utils.word_list_to_long(list_16_bits)


c.close()
