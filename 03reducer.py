inp = open('s01.txt','r')
out = open('r01.txt', 'w')

thisKey = ""
thisValue = 0.0

for line in inp:
 data = line.strip().split('\t')
 store, amount = data

 if store != thisKey:
   if thisKey:
     # output the last key value pair result
     out.write(thisKey + '\t' + str(thisValue)+'\n')

   # start over when changing keys
   thisKey = store
   thisValue = 0.0
 # apply the aggregation function
 thisValue += float(amount)
out.write(thisKey + "\t"+str(thisValue)+"\n")
inp.close()
out.close()