import kociemba
con={"W":"F","O":"L","G":"D","R":"R","Y":"B","B":"U"}
def conv(k):
	j=""
	for i in range(0,len(k)):
		j+=con[k[i]]
	return j

def result(k):
	k=k.upper()
	t=""
	try:
		t=str(kociemba.solve(conv(k)))
	except (ValueError,KeyError):
		return "Wrong input or unsolvable Cube"
	if t!="":
		return t

