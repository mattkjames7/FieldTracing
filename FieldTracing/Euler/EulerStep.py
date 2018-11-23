import numpy as np


def EulerStep(x0,dt,fv,direction=1.0):
	'''
	This Function will take a step in the direction of the field at the
	point x0.
	
	
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

	x1 = x0 + dt*v0[:,0]
	
	return x1
	
