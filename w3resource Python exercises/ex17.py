def make_bold(fn): ##defines the make bold as function
	def wrapped(): ##defines wrapped
		return "<b>" + fn() + "</b>" ##returns the <b> and </b> between the function
	return wrapped ##returns wrapped

def make_italic(fn): ##defines the make italic as function
	def wrapped(): ##defines wrapped
		return "<i>" + fn() + "</i>" ##returns the <i> and </i> between the function
	return wrapped ##returns wrapped

def make_underline(fn): ##defines the make underline as function
	def wrapped(): ##defines wrapped
		return "<u>" + fn() + "</u>" ##returns the <u> and </u> between the function
	return wrapped ##returns wrapped
@make_bold ##makes bold
@make_italic #makes italic
@make_underline ##makes underline
def hello(): ##defines hello
	return "hello world" ##returns hello world
print(hello()) ##prints the hello string
