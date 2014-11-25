# -*- coding: utf-8 -*-

print "Type the filename :"
filename = raw_input(">")
print "The band above Fermi:"
N = int(raw_input(">"))
M = 16+104*(N-4)-1

txt = open(filename,'r')

for i in range(0,M):
    txt.readline()
b0 = txt.readline()
[b0x,b0y,b0z] = b0.split('  ')
b0y = float(b0y)

for j in range(0,103):
	txt.readline()
b1 = txt.readline()
[b1x,b1y,b1z] = b1.split('  ')
b1y = float(b1y)

for k in range(0,103):
	txt.readline()
b2 = txt.readline()
[b2x,b2y,b2z] = b2.split('  ')
b2y = float(b2y)

for l in range(0,103):
	txt.readline()
b3 = txt.readline()
[b3x,b3y,b3z] = b3.split('  ')
b3y = float(b3y)

for m in range(0,103):
	txt.readline()
a0 = txt.readline()
[a0x,a0y,a0z] = a0.split('  ')
a0y = float(a0y)

for n in range(0,103):
	txt.readline()
a1 = txt.readline()
[a1x,a1y,a1z] = a1.split('  ')
a1y = float(a1y)

for o in range(0,103):
	txt.readline()
a2 = txt.readline()
[a2x,a2y,a2z] = a2.split('  ')
a2y = float(a2y)

for p in range(0,103):
	txt.readline()
a3 = txt.readline()
[a3x,a3y,a3z] = a3.split('  ')
a3y = float(a3y)

print "Gamma"
print N,'-',N-1,'->', a0y-b3y
print N,'-',N-2,'->', a0y-b2y
print N,'-',N-3,'->', a0y-b1y
print N,'-',N-4,'->', a0y-b0y
print N+1,'-',N-1,'->', a1y-b3y
print N+1,'-',N-2,'->', a1y-b2y
print N+1,'-',N-3,'->', a1y-b1y
print N+1,'-',N-4,'->', a1y-b0y
print N+2,'-',N-1,'->', a2y-b3y
print N+2,'-',N-2,'->', a2y-b2y
print N+2,'-',N-3,'->', a2y-b1y
print N+2,'-',N-4,'->', a2y-b0y
print N+4,'-',N-1,'->', a3y-b3y
print N+4,'-',N-2,'->', a3y-b2y
print N+4,'-',N-3,'->', a3y-b1y
print N+4,'-',N-4,'->', a3y-b0y


# 读中点
txt2 = open(filename,'r')
MM = 66+104*(N-4)-1

for i in range(0,MM):
    txt2.readline()
b0 = txt2.readline()
[b0x,b0y,b0z] = b0.split('  ')
b0y = float(b0y)

for j in range(0,103):
	txt2.readline()
b1 = txt2.readline()
[b1x,b1y,b1z] = b1.split('  ')
b1y = float(b1y)

for k in range(0,103):
	txt2.readline()
b2 = txt2.readline()
[b2x,b2y,b2z] = b2.split('  ')
b2y = float(b2y)

for l in range(0,103):
	txt2.readline()
b3 = txt2.readline()
[b3x,b3y,b3z] = b3.split('  ')
b3y = float(b3y)

for m in range(0,103):
	txt2.readline()
a0 = txt2.readline()
[a0x,a0y,a0z] = a0.split('  ')
a0y = float(a0y)

for n in range(0,103):
	txt2.readline()
a1 = txt2.readline()
[a1x,a1y,a1z] = a1.split('  ')
a1y = float(a1y)

for o in range(0,103):
	txt2.readline()
a2 = txt2.readline()
[a2x,a2y,a2z] = a2.split('  ')
a2y = float(a2y)

for p in range(0,103):
	txt2.readline()
a3 = txt2.readline()
[a3x,a3y,a3z] = a3.split('  ')
a3y = float(a3y)

print "Mid"
print N,'-',N-1,'->', a0y-b3y
print N,'-',N-2,'->', a0y-b2y
print N,'-',N-3,'->', a0y-b1y
print N,'-',N-4,'->', a0y-b0y
print N+1,'-',N-1,'->', a1y-b3y
print N+1,'-',N-2,'->', a1y-b2y
print N+1,'-',N-3,'->', a1y-b1y
print N+1,'-',N-4,'->', a1y-b0y
print N+2,'-',N-1,'->', a2y-b3y
print N+2,'-',N-2,'->', a2y-b2y
print N+2,'-',N-3,'->', a2y-b1y
print N+2,'-',N-4,'->', a2y-b0y
print N+4,'-',N-1,'->', a3y-b3y
print N+4,'-',N-2,'->', a3y-b2y
print N+4,'-',N-3,'->', a3y-b1y
print N+4,'-',N-4,'->', a3y-b0y

# 读Z点
txt3 = open(filename,'r')
MZ = 116+104*(N-4)-1

for i in range(0,MZ):
    txt3.readline()
b0 = txt3.readline()
[b0x,b0y,b0z] = b0.split('  ')
b0y = float(b0y)

for j in range(0,103):
	txt3.readline()
b1 = txt3.readline()
[b1x,b1y,b1z] = b1.split('  ')
b1y = float(b1y)

for k in range(0,103):
	txt3.readline()
b2 = txt3.readline()
[b2x,b2y,b2z] = b2.split('  ')
b2y = float(b2y)

for l in range(0,103):
	txt3.readline()
b3 = txt3.readline()
[b3x,b3y,b3z] = b3.split('  ')
b3y = float(b3y)

for m in range(0,103):
	txt3.readline()
a0 = txt3.readline()
[a0x,a0y,a0z] = a0.split('  ')
a0y = float(a0y)

for n in range(0,103):
	txt3.readline()
a1 = txt3.readline()
[a1x,a1y,a1z] = a1.split('  ')
a1y = float(a1y)

for o in range(0,103):
	txt3.readline()
a2 = txt3.readline()
[a2x,a2y,a2z] = a2.split('  ')
a2y = float(a2y)

for p in range(0,103):
	txt3.readline()
a3 = txt3.readline()
[a3x,a3y,a3z] = a3.split('  ')
a3y = float(a3y)

print "Z"
print N,'-',N-1,'->', a0y-b3y
print N,'-',N-2,'->', a0y-b2y
print N,'-',N-3,'->', a0y-b1y
print N,'-',N-4,'->', a0y-b0y
print N+1,'-',N-1,'->', a1y-b3y
print N+1,'-',N-2,'->', a1y-b2y
print N+1,'-',N-3,'->', a1y-b1y
print N+1,'-',N-4,'->', a1y-b0y
print N+2,'-',N-1,'->', a2y-b3y
print N+2,'-',N-2,'->', a2y-b2y
print N+2,'-',N-3,'->', a2y-b1y
print N+2,'-',N-4,'->', a2y-b0y
print N+4,'-',N-1,'->', a3y-b3y
print N+4,'-',N-2,'->', a3y-b2y
print N+4,'-',N-3,'->', a3y-b1y
print N+4,'-',N-4,'->', a3y-b0y





