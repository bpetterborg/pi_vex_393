#
#	Motor control library for Vex 393s
#	Based on RPi.GPIO2
# 
#	Thanks to the RPi.GPIO2 devs, you guys are awesome!
#
#	TODO:
#		- figure out how to set different motor numbers/names
#		- parsing config file
#		- add more motor control functions
#		- 
#

import RPi.GPIO2 as GPIO	# gpio access
import json

from pi_vex_393.pi_vex_393 import PWM_FREQUENCY

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
			return status_info



# actually doing stuff with the motors.
class Motor:

	def __init__(self, current_status) -> None:
		self.currentStatus = current_status
		pass


	def getId(self, motor):
		# get the motor id from the config file
		self.motor = motor
		motor_id = GetConfig.motors(motor,'id')
		return motor_id


	def setup(self, motor):
		# setup the gpio pins
		self.motor = motor
		
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(GetConfig.motors(motor,'pin'), GPIO.OUT)
		
		# unsure if this would work for sending the current status
		self.current_status = GetConfig.status('setupGpio') + '' + GetConfig.motors(motor,'id')


	def spin(self, motor, speed):
		# spin the motor at a speed, represented by a percentage
		self.motor = motor
		self.speed = speed

		# 2 to 1.5 is forward, 1.5 to 1 is reverse
		# 100 to 0 is forward, 0 to -100 is reverse

		FWD_DC = GetConfig.motor(self.motor, 'motorLimits[0]')
		NEU_DC = GetConfig.motor(self.motor, 'motorLimits[1]')
		RVS_DC = GetConfig.motor(self.motor, 'motorLimits[2]')


		# if the motor is reversed, rerverse the speed
		if GetConfig.motor(self.motor, 'reversed')	== True:
			self.speed = -self.speed
		
		else: 
			pass


		# convert a percentage to a duty cycle
		if speed < 100:
			duty_cycle = FWD_DC

		elif speed > -100:
			duty_cycle = RVS_DC
		
		elif abs(speed) > 100:
			return 'Speed too high/low, range is 0 to 100'

		elif speed > 0:			
			# some real wacky formatting :)
			duty_cycle = ((( FWD_DC - NEU_DC ) / 100 ) * self.speed) + NEU_DC
				
		elif speed < 0:
			# unsure if this will work for other PWM motors
			duty_cycle = ((( NEU_DC - RVS_DC ) / 100 ) * self.speed) + NEU_DC

		elif speed == 0:
			duty_cycle = NEU_DC
	
		# send motor pwm signal
		motor_pin = GetConfig.motors(self.motor, 'pin')
		PWM_FREQUENCY = GetConfig.motors(self.motor, 'pwmFrequency')

		GPIO.pwm(motor_pin, PWM_FREQUENCY).start(duty_cycle)
		self.current_status = GetConfig.statusMessages('motor_spinning')
		
		
	def stop(self, motor):
		# stop the motor
		self.motor = motor
		

	def cleanGpio(self):
		# dump everything with gpio
		GPIO.cleanup()
		self.current_status = GetConfig.status('cleanGpio')


	def currentStatus(self):
		# most recent status message is stored as a variable. 
		return self.current_status