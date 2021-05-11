

# file = open('name.txt','r')
#
# for f in file:
#     f = f.replace('\n','')
#     f = f.split('===')
#
#     error = open('name_123.txt', 'a+')
#     error.write(f[1] + '===' + f[2] + '\n')
#     error.close()


lines_seen = set() # holds lines already seen
outfile = open('name_421.txt', "w")
for line in open('name_321.txt', "r"):
    if line not in lines_seen: # not a duplicate
        outfile.write(line)
        lines_seen.add(line)
outfile.close()