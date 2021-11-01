from operator import itemgetter 
output=[]
for i in open("C:\\Users\\Volkovych\\Desktop\\ICS-170578\\first.txt"):
    output.append([i.split(None, -1)[0], i.split(None, -1)[1], float(i.split(None, -1)[2])])
    output= sorted(output, key=itemgetter(2) )
    print(output)
