#
# Motor control library for Vex 393s
# Based on RPi.GPIO2
# 
# Thanks to the RPi.GPIO2 devs, you guys are awesome!
#
#	TODO:
#		- figure out how to set different motor numbers/names
#		- parsing config file
#		- add more motor control functions
#		- 
#

import RPi.GPIO2 as GPIO	# gpio access
import json					# config files

# open and read motor and status configs
class GetConfig:

	def __init__(self) -> None:
		pass

	def status(self, status_message):
		json.load(open('status_messages.jsonc').read())

	def motors():
		json.load(open('motors.jsonc').read())

# actually doing stuff with the motors.
class Motors:

	def __init__(self, motor) -> None:
		pass

	def testModule(self):
		return 'Module working probably'

	def selectMotor(self, motor):
		return f'Select motor {motor}' # change this to debug status json read thing
		motor_name = GetConfig.motors()["motor1"] # work on this to make it actually fetch motor name
	



# unused but saving for later

# just trying stuff for the multiple motor support
#motor_count = json.loads(open('motors.jsonc').read())['motor_count']
