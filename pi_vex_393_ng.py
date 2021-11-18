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
import json


class GetConfig:

	def motor():
		
		with open("motors.json", "r") as motor_config_file:
			motor_config = json.load(motor_config_file)
			return motor_config

	def statusMessages():
		
		with open("status_messages.json", "r") as status_config_file:
			status_config = json.load(status_config_file)
			return status_config

# actually doing stuff with the motors.
class Motor:

	def __init__(self, motorId, dutyCycle) -> None:
		# may need to add varible for spin()
		self.motor = motorId
		self.dutyCycle = dutyCycle

	def testModule(self):
		return 'Module working probably'

	def selectMotor(self):
		return f'Select motor {self.motorId}' 		# change this to debug status json read thing
		motor_name = GetConfig.motors('motorId') 	# work on this to make it actually fetch motor name

	def spin(self, motorId, dutyCycle):
		# do fun math on the duty cycle to get it as a percentage
		return GetConfig.status('motor_spinning') + id

		# get config 
		# could probably be replaced with a tuple, would be much cleaner
		#FORWARD_DUTY_CYCLE_LIMIT = GetConfig.motors('forward_duty_cycle')
		#NEUTRAL_DUTY_CYCLE_LIMIT = GetConfig.motors('neutral_duty_cycle')
		#REVERSE_DUTY_CYCLE_LIMIT = GetConfig.motors('reverse_duty_cycle')

		#if FORWARD_DUTY_CYCLE_LIMIT > dutyCycle > NEUTRAL_DUTY_CYCLE_LIMIT:
		
		#elif REVERSE_DUTY_CYCLE_LIMIT < dutyCycle < NEUTRAL_DUTY_CYCLE_LIMIT:

		#elif dutyCycle = NEUTRAL_DUTY_CYCLE_LIMIT:
		#	return GetConfig.status('motor_stopped') + motorId + " 0"




	def cleanGpio(self):
		GPIO.cleanup()
		return GetConfig.status('cleanGpio') 		# test that this actually works