def GCD(a,b):
	'''Finds the Greatest Common Divisor of integers a,b using the Euclidean Algorithm.'''
	x = max(abs(a),abs(b))
	y = min(abs(a),abs(b))
	r = x % y
	while r != 0:
		#print('{} = q*{} + {}'.format(x,y,r))
		x = y 
		y = r 
		r = x % y
	return(y)

if __name__ == '__main__':
	print(GCD(2458437443,903827662))