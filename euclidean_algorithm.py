import numpy as np

def GCD(a,b):
	'''Finds integers the greatest common divisor of (a,b) and u,v such that GCD(a,b) = ua + vb.'''
	x = max(abs(a),abs(b))
	y = min(abs(a),abs(b))

	a = x 
	b = y

	r = x % y
	q = [int((x-r)/y)]
	while r != 0: # loop for Euclidean Algorithm
		x = y 
		y = r 
		r = x % y
		q.append(int((x-r)/y))
	gcd = y
	u = np.zeros(len(q))
	v = np.zeros(len(q))
	u[0] = 0 
	u[1] = 1
	v[0] = 1
	v[1] = -q[0]
	for i in range(2,len(q)): # computes u,v
		u[i] = u[i-2] - q[i-1]*u[i-1]
		v[i] = v[i-2] - q[i-1]*v[i-1]
		#print('{} - {}*{} = {}'.format(u[i-2], q[i], u[i-1], u[i]))
	u = int(u[-1])
	v = int(v[-1])
	return(gcd, u,v)

if __name__ == '__main__':
	print(GCD(2458437443,903827662))