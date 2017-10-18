#!/usr/bin/env python3

DNA ='AATTGGCCA'

count_A = DNA.count('A')

count_T = DNA.count('T')

number_of_AT = count_A + count_T

print ('there are', count_A, 'As in this DNA sequence')

print ('there are', count_T, 'Ts in this DNA sequence')

total_bases = len (DNA)

content_AT = number_of_AT/total_bases

print ('AT content of this DNA sequence is', content_AT)

#reversed_DNA = DNA.reverse () this line doesn't work;

Acomplemented_DNA = DNA.replace ('T','a')
Tcomplemented_DNA = Acomplemented_DNA.replace ('A','T')
Ccomplemented_DNA = Tcomplemented_DNA.replace ('C','g')
Gcomplemented_DNA = Ccomplemented_DNA.replace ('G','C')

print ('The cpmplemented sequence is', Gcomplemented_DNA)

#reversed_DNA = Gcomplemented_DNA[::-1]  this works!

reversed_DNA = ''.join (reversed(Gcomplemented_DNA)) ## this also works!

print ('The reversed complemented DNA sequence is', reversed_DNA)

position = DNA.find('TG')

Ecol1_seq = DNA[3:8]

print ('The position of TG in the sequence is', position)

print ('The sequence of EcolI is', Ecol1_seq)

