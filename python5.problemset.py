#!/usr/bin/env python3

##This the answer to Q1 and Q2:

file = open ("Python_05.txt","r")
result = open ("Python_05_uc.txt","w")

for line in file:

	line = line.rstrip()

	new_line = line.upper()

	result.write(line+"\n")

	#print (line)

	#print (new_line)

result.close()

##This is the answer to Q3:

seq_read = open ("Python_05.fasta","r")

genes={}

#count=0
id=''
reversed_seq=''
for line in seq_read:
	line=line.strip()
	if '>' in line:
		id=line
		#header=id,"this is reversed complement seq"
	else:
		seq=line
		Acomplemented_DNA = seq.replace ('T','a')
		Tcomplemented_DNA = Acomplemented_DNA.replace ('A','T')
		Ccomplemented_DNA = Tcomplemented_DNA.replace ('C','g')
		Gcomplemented_DNA = Ccomplemented_DNA.replace ('G','C')
		reversed_seq = ''.join (reversed(Gcomplemented_DNA))
	genes[id]=reversed_seq
	
print(genes)

for key in genes:
	seq=genes[key]
	print(key,"\n",seq) ##this line can output the same sequence in the fasta file; 

####################

#this is the answer to Q4

fastq = open("Python_05.fastq","r")

count=0
list=[]
for line in fastq:
	line=line.rstrip()
	count+=1
	length=len(line)
	list.append(length)
print(count)

sum=0
for number in list:
	sum=number+sum
print(sum)
average_length=sum/count
print(average_length)

#######################
##this is answer to Q5:
all = open("alpaca_all_genes.tsv","r")
pigment = open("alpaca_pigmentation_genes.tsv","r")
stemcellproliferation = open("alpaca_stemcellproliferation_genes.tsv","r")
a={}
p={}
s={}
with open("alpaca_all_genes.tsv") as f:
	a = set([line.rstrip('\n') for line in f])
#	print(s)
with open("alpaca_pigmentation_genes.tsv") as f:
        p= set([line.rstrip('\n') for line in f])
#       print(s)
with open("alpaca_stemcellproliferation_genes.tsv") as f:
        s = set([line.rstrip('\n') for line in f])
#        print(s)

#alltest=set(line.strip()for line in open("alpaca_all_genes.tsv","r")	

#PIGMENT=set(line.strip()for line in open("alpaca_pigmentation_genes.tsv","r")

#print (s)

#print (a-p-s)
#print (a|p|s)
print (a^p^s)
