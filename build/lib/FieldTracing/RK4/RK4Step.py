import numpy as np


def RK4Step(x0,dt,fv,direction=1.0):
	'''
	This Function returns the step taken along the field provided by the
	function 'fv' using the Runge-Kutta 4th order method.
	
	Inputs:
		x0: initial location vector.
		dt: Step size.
		fv: Callable function which provides a field vector given a 
			positional vector.
		direction: direction in which to trace, +1.0 will trace along 
		the field direction, -1.0 will trace in the opposite direction.
		
	Returns:
		new positional vector of the same form as x0.		
	
	'''
	v0 = direction*fv(x0)
	v1 = direction*fv(x0 + 0.5*dt*v0[:,0])
	v2 = direction*fv(x0 + 0.5*dt*v1[:,0])
	v3 = direction*fv(x0 + dt*v1[:,0])
	x1 = x0 + dt*(v0[:,0] + 2.0*v1[:,0] + 2.0*v2[:,0] + v3[:,0])/6.0
	return x1
	
