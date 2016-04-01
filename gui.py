from Tkinter import *
import tkMessageBox
import solve
c=[]
gi=-1
gj=-1
c.append(0)
c.append(1)
color={0:"blue",1:"red",2:"white",3:"green",4:"orange",5:"yellow"}
class App():
    def __init__(self, root):
        self.root = root

    def Function(self):
        self.grid = []
       	for i in range(3):
            row = []
            for j in range(0,3):
            	if i==1 and j==1:
            		row.append(Button(self.root,width=2,height=1,bg="blue",activebackground="blue",command=lambda i=i,j=j :self.Click1(i, j)))
                	row[-1].grid(row=i,column=j+3)
                else:
		            row.append(Button(self.root,width=2,height=1,command=lambda i=i,j=j :self.Click1(i, j)))
		            row[-1].grid(row=i,column=j+3)
            self.grid.append(row)
        for k in range(3,6):
            row1 = []
            for l in range(0,12):
				if k==4 and l==1:
					row1.append(Button(self.root,width=2,height=1,bg="orange",activebackground="orange",command=lambda k=k,l=l :self.Click1(k, l)))
					row1[-1].grid(row=k,column=l)
				elif k==4 and l==4:
					row1.append(Button(self.root,width=2,height=1,bg="white",activebackground="white",command=lambda k=k,l=l :self.Click1(k, l)))
					row1[-1].grid(row=k,column=l)
				elif k==4 and l==7:
					row1.append(Button(self.root,width=2,height=1,bg="red",activebackground="red",command=lambda k=k,l=l :self.Click1(k, l)))
					row1[-1].grid(row=k,column=l)
				elif k==4 and l==10:
					row1.append(Button(self.root,width=2,height=1,bg="yellow",activebackground="yellow",command=lambda k=k,l=l :self.Click1(k, l)))
					row1[-1].grid(row=k,column=l)
				else:
					row1.append(Button(self.root,width=2,height=1,command=lambda k=k,l=l :self.Click1(k, l)))
					row1[-1].grid(row=k,column=l)
            self.grid.append(row1)
        for m in range(6,9):
            row2 = []
            for n in range(0,3):
                if m==7 and n==1:
            		row2.append(Button(self.root,width=2,height=1,bg="green",activebackground="green",command=lambda m=m,n=n :self.Click1(m, n)))
                	row2[-1].grid(row=m,column=n+3)
                	c[1]+=1
                	c[1]=c[1]%6
                else:
		            row2.append(Button(self.root,width=2,height=1,command=lambda m=m,n=n :self.Click1(m, n)))
		            row2[-1].grid(row=m,column=n+3)   
            self.grid.append(row2)
    def Function2(self):
    	f=Button(self.root,width=10,height=1,text="Solve it!!",command=self.Click2)
        f.grid(row=15,column=3,columnspan=5)
    def Click2(self):
    	q=[]
    	for i in range(0,3):
    		for j in range(0,3):
    			q.append(str(self.grid[i][j]["bg"])[0].lower())
    	for m in range(3,6):
    		for n in range(6,9):
    			q.append(str(self.grid[m][n]["bg"])[0].lower())
    	for m in range(3,6):
    		for n in range(3,6):
    			q.append(str(self.grid[m][n]["bg"])[0].lower())
    	for k in range(6,9):
    		for l in range(0,3):
    			print str(self.grid[m][n]["bg"])
    			q.append(str(self.grid[k][l]["bg"])[0].lower())
    	for s in range(3,6):
    		for t in range(0,3):
    			q.append(str(self.grid[s][t]["bg"])[0].lower())	
    	for a in range(3,6):
    		for b in range(9,12):
    			q.append(str(self.grid[a][b]["bg"])[0].lower())    
    	res=''.join(q)
    	print res
    	tkMessageBox.showinfo( "Rubix Cube Solver",solve.result(res))
    def Click1(self, i, j):
    	c[0]+=1
    	k=c[0]%6
    	gi=i
    	gj=j
        self.grid[i][j]["bg"]=color[k]
        self.grid[i][j]["activebackground"]=color[k]

root = Tk()
root.title("Rubix Cube Solver")
app = App(root)
app.Function()
app.Function2()
root.mainloop()
