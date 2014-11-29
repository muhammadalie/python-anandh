import os
def find_file( filenames):
    filenames.sort()
    for f in filenames:
        a=os.path.abspath(f)
        print a,"\n"

a=['1.txt','2.txt']
find_file(a)
