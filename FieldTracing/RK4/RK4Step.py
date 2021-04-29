import numpy as np


def RK4Step(x0,dt,fv,direction=1.0):
	'''
	This Function returns the step taken along the field provided by the
	function 'fv' using the Runge-Kutta 4th order method.
	
	Inputs
	======
	x0 : float
		Initial location vector.
	dt : float
		Step size.
	fv : callable
		Callable function which provides a field vector given a 
		positional vector.
	direction : float
		Direction in which to trace, +1.0 will trace along 
		the field direction, -1.0 will trace in the opposite direction.
		
	Returns
	=======
	x1 : float
		New positional vector of the same form as x0.		
	
	'''
	v0 = direction*fv(x0)
	v1 = direction*fv(x0 + 0.5*dt*v0)
	v2 = direction*fv(x0 + 0.5*dt*v1)
	v3 = direction*fv(x0 + dt*v1)
	x1 = x0 + dt*(v0 + 2.0*v1 + 2.0*v2 + v3)/6.0
	return x1
	
