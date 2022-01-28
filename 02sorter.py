inp = open('v01.txt', 'r')
out = open('s01.txt', 'w')

lines = inp.readlines()
lines.sort()
for line in lines:
    out.write(line)

inp.close()
out.close()