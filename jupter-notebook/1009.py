import sys
print(sys.argv)
infile = sys.argv[1]
print(infile)
# for line in open(infile):
#     print(line)
with open(infile,'r') as f:
    print(f)
    #print(f.read())
    #for line in f.read():  f.read()----string
    for line in f:
        print(line)
        print('----')
    
