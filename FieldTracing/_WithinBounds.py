import numpy as np

def _GetBoundsFunction(bounds,xdim):
	'''
	Returns function which can check if the trace is still within the 
	required bounds.
	
	Inputs
	======
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
	xdim : int
		The number of dimensions of the vectors
		
	Returns
	=======
	_WithinBounds : callable
		Function which accepts a vector and returns True or False,
		depending on whether that vector is within the trace bounds.
	
	'''
	btype = 'none'
	if bounds != None:
		if callable(bounds):
			btype='func'
		elif np.size(bounds[0]) == xdim and np.size(bounds[1]) == xdim:
			btype = 'vector'
		elif np.size(bounds[0]) == 1 and np.size(bounds[1]) == 1:
			btype = 'range'
			
			
	def _WithinBounds(x):
		'''
		Determine whether a vector is within bounds.
		
		Inputs
		======
		x : float
			Vector position.
		
		Returns
		=======
		wb : bool
			True if x is within bounds, False otherwise.
		
		'''
		
		if np.any(x == np.nan):
			return False
		
		if btype == 'func':
			if bounds(x) == False:
				return False
		elif btype == 'vector':
			if (x < bounds[0]).any() or (x > bounds[1]).any():
				return False
		else:
			R = np.linalg.norm(x)
			if R < bounds[0] or R > bounds[1]:
				return False
		return True
					
	return _WithinBounds
