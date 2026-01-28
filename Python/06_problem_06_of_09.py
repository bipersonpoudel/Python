lineno=1
f=open("log.txt","r")
line=f.readline()
if ("python" in line):
    print("Python is present in line no :",lineno)
   
else:
    print("python is not present")
    lineno+=1
f.close()