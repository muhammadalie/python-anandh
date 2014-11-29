def grep(n, filenames):
    for f in filenames:
        for line in open(f):
            if  len(line)>11:
                print line,

a=['1.txt','2.txt']
grep('ali',a)
