f1=open('a.txt','r')
f2=open('b.txt','r')
a=f1.read()
b=f2.read()
f1.close()
f2.close()
f1=open('a.txt','w')
f2=open('b.txt','w')
f1.write(b)
f2.write(a)
f1.close()
f2.close()
print('file content swapping is done')
