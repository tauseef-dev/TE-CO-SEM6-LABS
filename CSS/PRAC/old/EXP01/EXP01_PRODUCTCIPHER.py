# NAME: TAUSEEF MUSHTAQUE ALI SHAIKH
# CLASS: TE-CO    ROLL-NO.: 18CO63
# EXPERIMENT NO. 01: PRODUCT CIPHER USING PYTHON.

import string

print("\n\t\t PRODUCT CIPHER \n")

k=int(input("ENTER A KEY VALUE:"))
d=input("ENTER A STRING: ")
ct = []
alphabets = string.ascii_uppercase
for j in d:
	b=j.upper()
	if b in alphabets and j.islower():
		e=(alphabets.index(b)+k)%26
		ct.append(alphabets[e].lower())
	elif b in alphabets and j.isupper():
		a=(alphabets.index(b)+k)%26
		ct.append(alphabets[a].upper())
	else:
		ct.append(" ")
        
matrix = [[False for i in range(len(ct))]
 for j in range(k)]

print("CIPHER TEXT: ",ct)
j=0
for i in range(len(ct)):
    matrix[j][i]=ct[i]
    if j == k - 1: 
        flag = False    
    elif j == 0: 
        flag = True
    if flag == True: 
        j = j + 1
    else: 
        j = j - 1 

answer=[]
for key in range(k):
    for text in range(len(ct)):
        if matrix[key][text]!=False:
            answer.append(matrix[key][text])

print("ENCRYPTED TEXT: ", answer)  


