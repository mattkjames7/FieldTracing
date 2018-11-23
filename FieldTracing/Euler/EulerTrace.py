import numpy as np
from .EulerStep import EulerStep
from .._WithinBounds import _GetBoundsFunction

def EulerTrace(x0,dt,fv,n=1000,bounds=None,direction=1.0):
	'''
	This function will trace along a field using the Eurler method - 
	bear in mind that this willnot do a very good job of tracing curved
	fields!
	
	Inputs:
		x0: Initial position vector.
		dt: Step size.
		f: 	Callable function which will provide a field vector when
			given a positional vector.
		n:	Number of steps to trace (maximum).
		bounds: This can be one of four things
				1. None - there are no bounds in this case, the trace
				will continue until the number of steps hits the maximum.
				2. callable - a function which will accept the position
				vector and return either True to continue, or False to
				halt the trace.
				3. tuple - containing two vectors with the same number 
				of elements as x0, the first (second) element of this
				tuple describes the lower (upper) limit for each 
				dimension of x. The trace will continue as long as 
				bounds[0][i] < x[i] < bounds[1][i], for all i.
				4. Range - list, array or tuple with two elements, 
				where the first (second) element describes the minimum 
				(maximum) value for any element of x. The trace 
				continues as long as bounds[0] < x[i] < bounds1[1], for
				all i.
		direction: Set to 1.0 for tracing in the direction of the field,
			or -1.0 to trace backwards. If set to 'both', thent he field 
			will be traced in both directions.
			
		Returns:
			Array with shape (n,m), where n is the number of steps, m is
			the number of dimensions of x0.
	'''	
	x1 = np.zeros((n,np.size(x0)),dtype='float32')

	xd = np.size(x0)

	WB = _GetBoundsFunction(bounds,xd)

			
	if direction == 'both':
		xtmp = np.copy(x0)
		mid = n/2
		x1[mid] = xtmp
		for i in range(mid+1,n):
			xtmp = EulerStep(xtmp,dt,fv,1.0)
			x1[i] = xtmp		
			if not WB(xtmp):
				break

		for i in range(mid-1,0,-1):
			xtmp = EulerStep(xtmp,dt,fv,-1.0)
			x1[i] = xtmp	
			if not WB(xtmp):
				break
	else:
		xtmp = np.copy(x0)
		x1[0] = xtmp
		for i in range(1,n):
			xtmp = EulerStep(xtmp,dt,fv,direction)
			x1[i] = xtmp
			if not WB(xtmp):
				break		
	return x1
