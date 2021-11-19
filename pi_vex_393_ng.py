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
	def statusMessages(self, var_index):
		
		self.var_index = var_index

		# open the file
		with open("status_messages.json", "r") as status_config_file:
			
			status_config = json.load(status_config_file)
			status_info = status_config[self.var_index]
			return status_config



# actually doing stuff with the motors.
class Motor:

	def getId(self, motor):
		# get the motor id from the config file
		self.motor = motor
		motor_id = GetConfig.motors(motor,'id')
		return motor_id

	def setup(self, motor):
		# setup the gpio pins
		# maybe need to create a motor object??
		self.motor = motor
		
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(GetConfig.motors(motor,'pin'), GPIO.OUT)
		return GetConfig.status('setupGpio') + '' + GetConfig.motors(motor,'id')

	#def spin(self, motor, speed):
		# spin the motor at a speed, represented by a percentage
	#	self.motor = motor
	#	self.speed = speed

		
	def cleanGpio(self):
		GPIO.cleanup()
		return GetConfig.status('cleanGpio') 		# test that this actually works