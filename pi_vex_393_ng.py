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
		# turns the percentage into a duty cycle
		self.motor = motor
		self.speed = speed

		#spinMotor = GPIO.PWM(gcm(motor, 'pin'), gcm(motor, 'pwmFrequency')).start('duty_cycle')

		speed = self.speed 

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


		if abs(speed) > 100:
			return 'Speed too high/low, range is 0 to 100'

		elif speed > 0:			
			# some real wacky formatting :)
			# also I have no idea if this will work. should test w/ calculator.
			duty_cycle = ((( FWD_DC - NEU_DC ) / 100 ) * abs(speed)) + NEU_DC
				
		elif speed < 0:
			# unsure if this will work for other PWM motors
			# this is non-working, test this and find a solution
			duty_cycle = ((( NEU_DC - RVS_DC ) / 100 ) * speed) + NEU_DC

		elif speed == 0:
			duty_cycle = NEU_DC
	

		# still need to actually send the pwm signal to the motor.
		

	def cleanGpio(self):
		# dump everything with gpio
		GPIO.cleanup()
		self.current_status = GetConfig.status('cleanGpio')


	def currentStatus(self):
		# most recent status message is stored as a variable. 
		return self.current_status