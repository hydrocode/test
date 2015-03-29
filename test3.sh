#!/bin/bash
MIN=100
MAX=131
for j in 094 096 098 100 102 104 106
do
for((i=MIN;i<MAX;i++))
do
x=$[104*$i+116]
head -n $x $j.txt | tail -n 101 > a.hh
cat>python.py<<!
# -*- coding: utf-8 -*-
	
filename = r'a.hh'
alist = []
text = open(filename,'r').readlines()
alist = [line.strip( ).split()[1] for line in text]
blist = open('b_$i.hh', 'w')
for i in alist:
	blist.write(i)
	blist.write("\n")
blist.close()
!
python python.py
rm -r a.hh
done
paste b_*.hh > $j.dat
rm -r b_*.hh
rm -r python.py
done




