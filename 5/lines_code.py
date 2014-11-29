import os
def find_file( ):
	cwd=os.getcwd()
    	for f in os.listdir(cwd):
		if(os.path.isfile(f)==True):
			count=0
			for line in open(f):
	      			count+=1
  			print f ,count,"\n"

find_file()
