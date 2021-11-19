# pi_vex_393

Control Vex 393 motors with a Raspberry Pi. 

You can use this to replace a Cortex with a Pi. While it is untested, it 
should work with other SOCs that work with RPi.GPIO2. Be sure to set the 
motors correctly. 

This should also work with motor controllers similar to the Vex MC29, that
use PWM to control speed/direction.

~~Currently this only works with 2 motors at a time but I will
probably fix that in the future.~~ Currently working on the fix and numerous other fixes/improvements in `pi_vex_393_ng.py`.