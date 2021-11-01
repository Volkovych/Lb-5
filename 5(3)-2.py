import csv
import sys
print("Група-1")
filename = "first.txt"
text_file=open("first.txt", "r")
reader=csv.reader(text_file, delimiter="\t")
for str in reader:
    print(str)
text_file.close()

print("Група-2")
filename = "second.txt"
text_file=open("second.txt", "r")
reader=csv.reader(text_file, delimiter="\t")
for str in reader:
    print(str)
text_file.close()
    
