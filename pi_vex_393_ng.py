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

# returns config files as dictionary
class GetConfig:

	# get motors config
	def motor(self, object_index, var_index):
		
		self.object_index = object_index
		self.var_index = var_index

		# open the file
		with open("motors.json", "r") as motor_config_file:
			motor_config = json.load(motor_config_file)
			motor_info = motor_config[self.object_index][self.var_index]
			return motor_info

	# get status message config
	def statusMessages(self, object_index, var_index):
		
		self.object_index = object_index
		self.var_index = var_index

		# open the file
		with open("status_messages.json", "r") as status_config_file:
			
			status_config = json.load(status_config_file)
			status_info = status_config[self.object_index][self.var_index]
			return status_config



# actually doing stuff with the motors.
class Motor:

	def testModule():
		return 'Module working probably'

	def getMotorId(self, motor):
		# get the motor id from the config file
		self.motor = motor
		motor_id = GetConfig.motors(motor,'motorId')
		return motor_id


	#def spin(self, motor, dutyCycle):
		# do fun math on the duty cycle to get it as a percentage
		#return GetConfig.status('motor_spinning') + id

		# get config 
		



	def cleanGpio(self):
		GPIO.cleanup()
		return GetConfig.status('cleanGpio') 		# test that this actually works