#
# Motor control library for Vex 393s
# Based on RPi.GPIO2
# 
# Thanks to the RPi.GPIO2 devs, you guys are awesome!
#
#	TODO:
#		- figure out how to set different motor numbers/names
#
#
#
#

import RPi.GPIO2 as GPIO	# gpio access
import json					# config files

class GetMotorConfig:
	
	def __init__(self) -> None:
		pass

	def read_config():
		json.loads(open('motors.json').read())

class GetStatusConfig:

	def __init__(self) -> None:
		pass

	def read_config():
		json.loads(open('status_messages.json').read())

class Motors:

	def __init__(self) -> None:
		pass

	def test_module(self):
		return 'Module working probably'

	def select_motor(self, motor):
		return f'Select motor {motor}'
