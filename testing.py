# some tests


# imports 
import pi_vex_393
from time import sleep
Motor = pi_vex_393.Motor()


# main stuff
try:
	print('Setup gpio')
	print(Motor.current_status())
	Motor.setup('left') 
	#Motor.setup('right')
	
	print('Attempting to spin left and right motors')
	Motor.spin('left', 100)
	#Motor.spin('right', 100)
	print(Motor.current_status())

	print('Sleeping for 4s')
	sleep(4)


	print('Setting duty cycle neutral')
	Motor.spin('left', 0)
	#Motor.spin('right', 0)

	print('Stopping motors.')
	Motor.stop('left')
	#Motor.stop('right')
	print(Motor.current_status())


except KeyboardInterrupt:
	print('\nInterrupted by user')
	exit()