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

print("Sub text after splitting with \':\'",end="")
for x in sub_text:
    print("\n\t"+x,end="")
f.close()