#!/usr/bin/env python3 

##This script is used to split any sequnce into 60nt long multi-line sequences;

dna = "GATGGGATTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTCTAGAGCCACCGTCCAGGGAGCAGGTAGCTGCTGGGCTCCGGGGACACTTTGCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACGCTTCCCTGGATTGGCAGCCAGACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGCCCCCTCTGAGTCAGGAAACATTTTCAGACCTATGGAAACTACTTCCTGAAAACAACGTTCTGTCCCCCTTGCCGTCCCAAGCAATGGATGATTTGATGCTGTCCCCGGACGATATTGAACAATGGTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATGCCAGAGGCTGCTCCCCCCGTGGCCCCTGCACCAGCAGCTCCTACACCGGCGGCCCCTGCACCAGCCCCCTCCTGGCCCCTGTCATCTTCT"

import sys
#file = sys.argv[1]
#seq = open ("dna","r")
#for line in seq:

def format_sequence(line, line_length): ## the arguments here is depending on how many do you need to use in the funtion or in the command line;
	count = 0
	for letter in line:
		count+=1
		if count < line_length: #60:
			print (letter,end='')
		elif count==line_length: #60:
			print (letter)
		else:
			count = 0
	return ''
	#return(format_sequence(line))
#print(format_sequence(line))

#for letter in dna:
print(format_sequence(dna,60)) ##Here, don't need for loop for string input;

###############
import subprocess
output = subprocess.check_output('ls -l | grep python',shell = True)
str=output.decode('utf-8')
print (str)
###############
import argparse

parser = argparse.ArgumentParser(description="A test program that reads in some number of lines from an input file. The output can be screen or an output file")

parser.add_argument("FASTA", help="path to input fasta filename")

parser.add_argument("line_length", type=int, help="Max length to output per line: default 80nt")
#parser.add_argument("output", help="Min length to output")

args = parser.parse_args()

filename = args.FASTA
len = args.line_length
#out = args.output

#if args.line_length:
#	lines = args.line_length
#else:
#	lines = 80 #this means default is 80;

file=open(filename,"r")
##here, we can do anything that previously practised.
for line in file:
	#print(line)
	print(format_sequence(line,len))

############

