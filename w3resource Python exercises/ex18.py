mycode = 'print("hello world")' ##mycode defined as 'print("hello world")'
code = """
def multiply(x,y):
	return x*y

print('Multiply of 2 and 3 is: ', multiply(2,3))
"""
##up here defines code as code literally
exec(mycode) ##executes mycode
exec(code) ##executes code
