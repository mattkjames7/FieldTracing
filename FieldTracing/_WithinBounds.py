import numpy as np

def _GetBoundsFunction(Bounds,xdim):
	'''
	Returns function which can check if the trace is still within the 
	required bounds.
	
	'''
	btype = 'none'
	if Bounds != None:
		if callable(Bounds):
			btype='func'
		elif np.size(Bounds[0]) == xdim and np.size(Bounds[1]) == xdim:
			btype = 'vector'
		elif np.size(Bounds[0]) == 1 and np.size(Bounds[1]) == 1:
			btype = 'range'
			
			
	def _WithinBounds(x):
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
