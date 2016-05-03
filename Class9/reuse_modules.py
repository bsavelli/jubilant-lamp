def func1():
	print "Hello World"

def func2(arg1='San Francisco', arg2='Dallas', arg3='Denver', arg4=None):
	if !arg4:
        print arg1, arg2, arg3
    else:
    	print arg1, arg2, arg3, arg4

class MyClass(object):
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def sum(self):
		return self.x + self.y

class NewClass(MyClass):
	def product(self):
		return self.x * self.y

def main():
	print "This module does something when the file is directly executed!"

if __name__ == "__main__":
	main()
	


'''how to use this program
#define the object
my_obj = reuse.MyClass(10, 17)

view individual elements
my_obj.x
my_obj.y

how to call the separate functions in the class
my_obj.sum()
my_obj.product()
'''
