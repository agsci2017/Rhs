import tkinter # note that module name has changed from Tkinter in Python 2 to tkinter in Python 3

#    http://effbot.org/tkinterbook/

parent = tkinter.Tk()
parent.geometry("550x450")

parentfont={}
parentfont['name']="Liberation Mono"
parentfont['size']=14
parentfont['bold']="bold" #"bold"

########################################
#           GUI API(TKINTER)           #
########################################

def hs(s,arg1=None,arg2=None,arg3=None):
	if s=='button':
		return tkinter.Button(parent, text = "Hello")
	
	if s=='title':
		parent.title(arg1)
		return
	
	if s=='label':
		label = tkinter.Label( parent, relief = tkinter.FLAT )
		return label
		
	if s=="entry":
		if not arg1:
			arg1=20
		return tkinter.Entry(parent, width=arg1)
	
	if s=="textarea":
		if not arg1:
			arg1=60
		if not arg2:
			arg2=20
		return tkinter.Text(parent, width=arg1, height=arg2)
		
	if s=="listbox":
		return tkinter.Listbox(parent, height=18)

	if s=='label wrap':
		if not arg2:
			arg2=20
		arg1.configure(wraplength=arg2)
		return

	if s=='place':
		#print(arg2[0],arg2[1])
		#авто-определитель, если вдруг не тупл
		arg1.place(x=arg2[0],y=arg2[1])
		return

	if s=='width':
		arg1['width']=arg2
		return
		
	if s=='height':
		arg1['height']=arg2
		return

	if s=='text':
		if type(tkinter.Text(parent))==type(arg1):
			hs('delete text',arg1)
			arg1.insert(tkinter.INSERT, arg2)
		elif type(tkinter.Entry(parent))==type(arg1):
			arg1.delete(0,tkinter.END)
			arg1.insert(tkinter.END, arg2)
		else:
			arg1["text"]=arg2
		
		return
	
	if s=="var":
		return tkinter.StringVar()
	
	if s=="set":
		arg1.set(arg2)
		return

	if s=="get":
		return arg1.get()
	
	if s=="entry bind":
		arg1.bind('<Key-Return>', arg2) #assign function
		return
	
	if s=="assign":
		arg1["textvariable"]=arg2  #assign double variable to an entry
		return

	
	if s=='set bg':
		if not arg2:
			arg2='green'
		arg1.configure(background=arg2) #green

	#buttons only
	if s=='command' or s=='set command' or s=="set function" or s=="set callback":
		arg1['command']=arg2
		return
	
	if s=="text?":
		return str(arg1.get())
	
	if s=='use font':
		pass
		return
	
	if s=='focus':
		arg1.focus_set()
		return
	
	if s=='font size':
		parentfont['size']=arg2
		arg1.configure(font=(parentfont['name'],parentfont['size'], parentfont['bold']))
		return
	
	if s=='font name':
		parentfont['name']=arg2
		arg1.configure(font=(parentfont['name'],parentfont['size'], parentfont['bold']))
		return
	
	if s=='font bold':
		parentfont['bold']='bold'
		arg1.configure(font=(parentfont['name'],parentfont['size'], parentfont['bold']))
		return
	if s=='font normal':
		parentfont['bold']='normal'
		arg1.configure(font=(parentfont['name'],parentfont['size'], parentfont['bold']))
		return

	if s=='justify':
		if arg2=='center':
			arg1['justify']=tkinter.CENTER
		if arg2=='left':
			arg1['justify']=tkinter.LEFT
		return
	
	if s=='delete text':
		if type(arg1)==type(tkinter.Entry(parent)):
			arg1.delete(0, END)
		else:
			arg1.delete('1.0',tkinter.END)
		return
	
	if s=='get clipboard':
		return parent.clipboard_get()
	
	if s=='after' or s=="timer":
		#milliseconds, function
		parent.after(arg1, arg2) #arg2=func
		return
	
	if s=='delete':
		arg1.destroy()
		return
	
	if s=="quit":
		parent.quit()
		return
	
	if s=="listbox insert":
		L.insert(tkinter.END, arg1)
		return
	
	if s=='end':
		parent.mainloop()
		return
	
	print('ERR: no function '+s)




########################################
#            SNIPPET CLASS             #
########################################

class Sample:
	
	def __init__(self, sentences, snippet):
		
		self.inputs=[]
		
		#создаем список предложений, которым соответствует один сниппет
		for s in sentences:
			self.inputs.append( s.split(" ") )
		
		self.snippet = snippet
		
		self.lastRequest = None
	
	
	
	def fits(self, req):
		request=set( req.split(" ") ) #набор слов запроса

		found=False
		
		for sent in self.inputs: #для каждого из возможных предложений
			if (len(request.intersection(set(sent))) == len(request)):
				found=True
				self.lastRequest = request
		
		return found
	
	def getSnippet(self):
		return self.snippet.strip()
		
	def getSet(self):
		for sent in self.inputs: #для каждого из возможных предложений
			if (len(self.lastRequest.intersection(set(sent))) == len(self.lastRequest)):
				return str(" ".join(sent))


#считываем базу сниппетов
gSnippets=[]
def ev(a,b):
	gSnippets.append(Sample(a, b))


# ~ exec(open("./snippets.py").read())

########################################
#               SNIPPETS               #
########################################

# 1) использовать синонимы
# 2) порядок слов не имеет значения


ev(["head","first"], """
v[1]
""")

ev(["tail","except first"], """
#except first element
	v[-1]
	v[2:length(v)]
""")

ev(["last"], """
v[length(v)]
""")

ev(["append"], "append(v,0) #append 0 to vector")
ev(["interval"], "seq(1,10, length.out=1000)")
ev(["range"], "seq(1,10)")
ev(["reverse"], "rev( v )")
ev(["shuffle"], "sample(v)")
ev(["random choice", "random select"], "v <- sample(1:10000, 3) # choise any 3 elements")
ev(["filter vector"], """arr[arr>=2 & arr<10]""")
ev(["repeat","repeat element"], """rep("*",10) ## ********** """)


ev(["random unif","random uniform"], """
v <- runif(100)
# 100 numbers from [0.0 .. 1.0]
""")

ev(["random norm","random normal"], """
v <- rnorm(100, mean = 0, sd = 1)
## 100 numbers for mu=0, sigma=1""")


ev(["double to string"," int to string"], """
as.character(10.0)
paste(10.0)""")
ev(["string to double"], """as.double("2.5")""")
ev(["string to int"], """strtoi("2")""")

ev(["string contains", "contains"], """grepl("hello","hello world")""")
ev(["string catenate","vector to string"], """paste(c(1,2,3), collapse=",")""")



ev(["format"], """
format(10.1234123, digits=4, width=8)
# returns str
""")
ev(["float","round"], """round(x, 2) # 3.13 from 3.131313""")
ev(["ceil"], """ceiling(3.13) # 4""")


ev(["plot font size"], """plot(... cex=1.5, cex.lab=1.5, cex.main=1.5, cex.axis=1.5 ...)
##cex  - points
##main - title
##axis - tics""")


ev(["csv", 'read csv','read dataframe'], """dt <- read.table(file="file.csv", header=TRUE, row.names=1, sep=",", dec = ".") """)
ev(["write csv",'write dataframe'], """write.csv(dt, file="file.csv", header=TRUE, row.names=0, sep=",") """)
ev(["edit dataframe"], """edit(cars)""")

ev(["filter dataframe rows"], """cars[ cars$speed>20, ]""")

ev(["dataframe sort"], "df[order(df$x), ]")
ev(["dataframe create"], """
df <- data.frame(col1=sample(10), col2=NA)

# example
city <- c("Tampa","Seattle","Hartford")
zipcode <- c(33602,98104,06161)
addresses <- cbind(city,zipcode)""")

ev(["dataframe select column"], """
dt[, c("speed","dist")] #select by colname

dt[,1] #select by index

data$field

data[["field"]]

data[,"field"]""")

ev(["dataframe remove delete column"], """
data$size      <- NULL
data[["size"]] <- NULL
data[,"size"]  <- NULL""")

ev(["dataframe select row"], """dt[i,]""")

ev(["dataframe filter"], """
subset(mtcars, mpg>20, c("mpg", "hp"))

filter(mtcars, mpg>20)""")

ev(["dataframe add column field"], """
#если поле не было создано - создать поле(инициализация 0)
dt$num <- 0

#пример
cars$nf <- car$speed*cars$dist""")


ev(["func","function"], """fFunc <- function(a = 3, b = 6) {
   a * b
   print(a*b)
   NA
} """)


ev(["for dataframe rows row"], """for(i in 1:nrow(v)){ v[i,] }

# or
by(df, 1:nrow(df), function(row) dostuff)
""")
ev(["dataframe columns column names"], """colnames(dt) ## colnames(dt) <- c("sdf","fgh") """)
ev(["dataframe rows"], """df[566:570,]""")
ev(["for vector","for sequence"], """for (i in v){\n\n}\n""")
ev(["for dataframe column"], """for (elt in v$field){ }""")


ev(["install package","import","include"], """
install.packages("ggplot2")
install.packages("dplyr")

library(gglot)
library(dplyr)
""")

ev(["plot"], """
plot(mtcars$disp, mtcars$mpg, xlab="XLAB", ylab="YLAB", main="TITLE")
""")

ev(["plot png","save plot",'plot to file'], """
png(filename="file.png")
plot(...)
dev.off()
""")

ev(["plot pch", "plot markers"], """
pch=0,square
pch=1,circle
pch=2,triangle point up
pch=3,plus
pch=4,cross
pch=5,diamond
pch=6,triangle point down
pch=7,square cross
pch=8,star
pch=9,diamond plus
pch=10,circle plus
pch=11,triangles up and down
pch=12,square plus
pch=13,circle cross
pch=14,square and triangle down
pch=15, filled square blue
pch=16, filled circle blue
pch=17, filled triangle point up blue
pch=18, filled diamond blue
pch=19,solid circle blue
pch=20,bullet (smaller circle)
pch=21, filled circle red
pch=22, filled square red
pch=23, filled diamond red
pch=24, filled triangle point up red
pch=25, filled triangle point down red""")

ev(["plot type"], """
p 	points
l 	lines
o 	overplotted points and lines
b, c 	points (empty if "c") joined by lines
s, S 	stair steps
h 	histogram-like vertical lines
n 	does not produce any points or lines
""")





########################################
#                 GUI                  #
########################################

hs('title','R search')

v = hs('var')

I = hs("entry")
T = hs('textarea')

hs('place',I,(20,10))

hs('focus',I)

hs('place',T,(20,40))

hs('width',T,63)
hs('height',T,23)

def func(event):
	res=''
	for s in gSnippets:
		if s.fits(hs('get',v)):
			res+='============'+s.getSet()+'=============\n'
			res+=s.getSnippet()+'\n\n'
	hs('text',T, res)

hs('entry bind', I, func)

hs('assign',I,v)

hs('end')
