import numpy as np
from .EulerStep import EulerStep
from .._WithinBounds import _GetBoundsFunction

def EulerTrace(x0,dt,f,n=1000,bounds=None,direction='both',Verbose=True):
	'''
	This function will trace along a field using the Eurler method - 
	bear in mind that this willnot do a very good job of tracing curved
	fields!
	
	Inputs
	======
	x0 : float
		Initial position vector.
	dt : float
		Step size.
	f : callable
	 	Callable function which will provide a field vector when
		given a positional vector.
	n : int
		Number of steps to trace (maximum).
	bounds : callable,float
		This can be one of four things
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
	Verbose : bool
		If True, progress will be displayed while tracing is done.
	direction : float,str
		Set to 1.0 for tracing in the direction of the field,
		or -1.0 to trace backwards. If set to 'both', then the field 
		will be traced in both directions.
			
	Returns
	=======
	x : float
		Array with shape (n,m), where n is the number of steps, m is
		the number of dimensions of x0.
	'''	
	def fv(p):
		'''
		Return a unit vector from the model.
		
		Input
		=====
		p : float
			Array containing a vector position.
			
		Return
		======
		v : float
			Unit vector at position p.
		'''
		v = f(p).flatten()
		vm = np.linalg.norm(v)
		return v/vm


	xd = np.size(x0)
	x1 = np.zeros((n,xd),dtype='float32')+np.float32(np.nan)

	WB = _GetBoundsFunction(bounds,xd)

			
	if direction == 'both':
		xtmp = np.copy(x0)
		mid = n//2
		x1[mid] = xtmp
		step = 0
		for i in range(mid,n):
			if Verbose:
				print("\rTracing Step {0} (Max = {1})".format(step+1,n),end='')
			xtmp = EulerStep(xtmp,dt,fv,1.0)
			x1[i] = xtmp	
			step += 1		
			if not WB(xtmp):
				break

		xtmp = np.copy(x0)
		for i in range(mid-1,-1,-1):
			if Verbose:
				print("\rTracing Step {0} (Max = {1})".format(step+1,n),end='')
			xtmp = EulerStep(xtmp,dt,fv,-1.0)
			x1[i] = xtmp	
			step += 1	
			if not WB(xtmp):
				break
		if Verbose:
			print('\nTotal Steps: {0}'.format(step))
	else:
		xtmp = np.copy(x0)
		x1[0] = xtmp
		step = 0
		for i in range(1,n):
			if Verbose:
				print("\rTracing Step {0} (Max = {1})".format(step+1,n),end='')
			xtmp = EulerStep(xtmp,dt,fv,direction)
			x1[i] = xtmp
			step += 1
			if not WB(xtmp):
				break	
		if Verbose:
			print('\nTotal Steps: {0}'.format(step))	
	return x1
