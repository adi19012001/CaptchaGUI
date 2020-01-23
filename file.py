# file handling in python

# creating file
f=open("File.txt","w")
print(f)

# writing inside the file
f=open("File.txt","w")
f.write("File handling in python")

# reading from file
f=open("File.txt","r")
print(f.read())

# number of characters to be printed
f=open("File.txt","r")
print(f.read(10))

# appending the data
f=open("File.txt","a")
f.write(". It is very useful.")

f=open("File.txt","r")
print(f.read())

#readline fumction
f=open("File.txt","r")
print(f.readlines())
f.close()

# variable declaration
"In %d days we made %f million %s."%(34,6.1,'dollars')

# spaces
"%5d"%(7) #5 is no. of spaces

# making a file as directory
#f=open("D:\python\File")
#f.write("This file is a directory now")
#f.close()

# pickilng
import pickle
f=open("test.pck","wb")
#dump method
pickle.dump(12.3,f)
pickle.dump([1,2,3],f)

f=open("test.pck","rb")
a=pickle.load(f)
b=pickle.load(f)
print(type(a), "\n", type(b))
print(a,"\n",b)
f.close()
