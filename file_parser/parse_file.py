filename = "test.txt"

import os
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, filename)

print("Filename :")
print("\t"+filename)

f = open(filename)

Line = f.readline().rstrip()
print("Text:")
print("\t"+Line)
sub_text = Line.split(sep=":")

for idx,valx in enumerate(sub_text):
    if(idx==0):
        print("\nKey: \t"+valx,end="")
    elif(idx==1):
        print("\nVal: \t"+valx,end="")
f.close()