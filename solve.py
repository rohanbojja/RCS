import kociemba
con={"W":"F","O":"L","G":"D","R":"R","Y":"B","B":"U"}
def conv(k):
	j=""
	for i in range(0,len(k)):
		j+=con[k[i]]
	return j
k=raw_input("Input the cube colors in give order of their center face color: Blue(B)->Red(R)->White(W)->Green(G)->Orange(O)->Yellow(Y)\n")
k=k.upper()
t=""
try:
	t=str(kociemba.solve(conv(k)))
except ValueError as err:
	print "Wrong input or unsolvable"
if t!="":
	print t

