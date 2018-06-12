import os

def f_c(X):
	'''Always returns 4 no matter the parameter'''
	return 4

def f_x(x, a, b):
	'''Executes the formula (a*x + b) with the loaded parameters'''
	formula = a*x + b
	return formula

def sum(x):
	'''Executes the formula from f_x three times and returns their summary'''
	summary = f_x(x, 1, 1) + f_x(x, 2, 2) + f_x(x, 3, 3)
	return summary

if __name__ == '__main__':
	print(f_c(5))
	print(f_x(1, 2, 3))
	print(sum(4))
	