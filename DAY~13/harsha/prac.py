import mmap

data = 'Harsha'

f = open("data.txt", "r+b")

mm = mmap.mmap(fileno=f.fileno(),length=0)

mm[0:len(data)] = data.encode('utf-8')

mm.close()

f = open("data.txt", "r")

print(f.read())