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
    
a = input('input:')
print(a)
s = set([1,2,3])
s1 = set([2,3])
s2 = {1,2,3}
d = set()
d.add(s)
d.add(s2)
d.add(s1)