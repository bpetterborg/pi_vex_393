# 
#	Motor control library
#	Use to control Vex 393s with RPi.GPIO2
#	
#	TODO:
#		- Make a separate repo for this, put it on the PyPI
#			- Make it a submodule
#		- Fix pwm
#		- If duty cycle is set wrong, reject it
#



import RPi.GPIO2 as GPIO		# interface with the gpio/pwm

left_motor_pin = 16				# which pins to use, may need to set later
right_motor_pin = 20

REVERSE_DUTY_CYCLE_LIMIT = 1	# duty cycle forward/reverse/neutral limits
NEUTRAL_DUTY_CYCLE_LIMIT = 1.5	# may need to be tweaked on a per-motor
FORWARD_DUTY_CYCLE_LIMIT = 2	# maybe move this to a config file

NEUTRAL_DUTY_CYCLE_LIMIT = 0 		# default duty cycle for the pwm
right_motor_duty_cycle = 0
neutral_duty_cycle = 7

PWM_FREQUENCY = 50				# frequency of the pwm (hz)

# setup
GPIO.setmode(GPIO.BCM)					# may need to set this to BOARD is stuff isn't working
GPIO.setup(left_motor_pin, GPIO.OUT) 	# pin 16 is the left motor
GPIO.setup(right_motor_pin, GPIO.OUT) 	# pin 20 is the right motor

left_motor_pwm = GPIO.PWM(left_motor_pin, PWM_FREQUENCY).start(left_motor_duty_cycle)
right_motor_pwm = GPIO.PWM(right_motor_pin, PWM_FREQUENCY).start(right_motor_duty_cycle)

class Motors:

	# i think this is right??, unfamiliar with classes
	def __init__(self) -> None:
		pass


	def test_module(self):
		print('Module working')
		

	def stop(self):
		# stop the motors
		print('Stopping')
		left_motor_pwm.stop()
		right_motor_pwm.stop()


	def clean_gpio(self):
		# clean up the gpio
		print('Cleaning GPIO')
		GPIO.cleanup()	# resets gpio used to input



	# control left motor
	class Left:
		def __init__(self):
			pass


		def spin(self, duty_cycle):
			# spin the left motor
			
			# if this part doesn't work, probably use AND instead of double >
			# go forward
			if FORWARD_DUTY_CYCLE_LIMIT > duty_cycle > NEUTRAL_DUTY_CYCLE_LIMIT:
				left_motor_pwm(duty_cycle)
				print(f'Spinning left motor forwards with duty cycle {duty_cycle}')

			# if not then go backward
			elif REVERSE_DUTY_CYCLE_LIMIT < duty_cycle < NEUTRAL_DUTY_CYCLE_LIMIT:
				left_motor_pwm(duty_cycle)
				print(f'Spinning left motor reverse with duty cycle {duty_cycle}')

			# if not that return an error
			else: 
				return "Duty cycle set incorrectly"

		def stop(self):
			# stop the left motor
			print(f'Stopping left motor')
			left_motor_pwm.stop()


	# control right motor
	class Right:
		def __init__(self) -> None:
			pass

		def spin(self, duty_cycle):
			# go forward
			if FORWARD_DUTY_CYCLE_LIMIT > duty_cycle > NEUTRAL_DUTY_CYCLE_LIMIT:
				right_motor_pwm(duty_cycle)
				print(f'Spinning right motor forwards with duty cycle {duty_cycle}')

			# if not then go backward
			elif REVERSE_DUTY_CYCLE_LIMIT < duty_cycle < NEUTRAL_DUTY_CYCLE_LIMIT:
				right_motor_pwm(duty_cycle)
				print(f'Spinning right motor resverse with duty cycle {duty_cycle}')

			# if not that return an error.
			else: 
				return "Duty cycle set incorrectly"	# can i use a ValueError here?

		def stop(self):
			# stop right motor
			print(f'Stopping right motor')
			right_motor_pwm.stop()
			