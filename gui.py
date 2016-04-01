from Tkinter import *
c=[]
c.append(0)
color={0:"blue",1:"red",2:"white",3:"green",4:"orange",5:"yellow"}
class App():
    def __init__(self, root):
        self.root = root

    def Function(self):
        self.grid = []
        for i in range(3):
            row = []
            for j in range(3):
                row.append(Button(self.root,width=2,height=1,command=lambda i=i,j=j :self.Click1(i, j)))
                row[-1].grid(row=i,column=j)
            self.grid.append(row)
        for k in range(3,6):
            row1 = []
            for l in range(12):
                row1.append(Button(self.root,width=2,height=1,command=lambda k=k,l=l :self.Click1(k, l)))
                row1[-1].grid(row=k,column=l)
            self.grid.append(row1)
        for m in range(6,9):
            row2 = []
            for n in range(3):
                row2.append(Button(self.root,width=2,height=1,command=lambda m=m,n=n :self.Click1(m, n)))
                row2[-1].grid(row=m,column=n)   
            self.grid.append(row2)
       # h=Butto(self.rnoot,width=2,height=5,    
    def Click1(self, i, j):
    	c[0]+=1
    	k=c[0]%6
        self.grid[i][j]["bg"]=color[k]

root = Tk()
app = App(root)
app.Function()

root.mainloop()
