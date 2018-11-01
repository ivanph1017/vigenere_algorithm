#!/usr/bin/env python
import string

mykey="ULIMA"
input_text="SEGURIDAD DE SISTEMAS DE TI"
code_text="NOÑGRCÑIO DY DPETYWIE DY EP"

# Alphabet used as reference (M)
# ABCDEFGHIJKLMNÑOPQRSTUVWXYZ
source = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'
source = list(source)

# Key alphabet (K) shifted 1 position to the left
# BCDEFGHIJKLMNÑOPQRSTUVWXYZA
shift = 1
matrix = [ source[(i + shift) % 27] for i in range(len(source)) ]

def coder(thistext):
    ciphertext = []
    control = 0

    for x,i in enumerate(input_text.upper()):
        if i not in source: 
            #If the symbol is not in our reference alphabet, we simply print it
            ciphertext.append(i)
            continue
        else:
            #Wrap around the mykey string 
            control = 0 if control % len(mykey) == 0 else control 

            #Calculate the position C[i] = (M[i]+K[i]) mod len(M)
            result = (source.index(i) + matrix.index(mykey[control])) % 27

            #Add the symbol in position "result" to be printed later
            ciphertext.append(matrix[result])
            control += 1

    return ciphertext

def decoder(thistext):
    control = 0
    plaintext = []

    for x,i in enumerate(code_text.upper()):
        if i not in source: 
            #If the symbol is not in our reference alphabet, we simply print it
            plaintext.append(i)
            continue
        else:
            #Wrap around the mykey string 
            control = 0 if control % len(mykey) == 0 else control 

            #Calculate the position M[i] = (C[i]-K[i]) mod len(M)
            result = (matrix.index(i) - matrix.index(mykey[control])) % 27

            #Add the symbol in position "result" to be printed later
            plaintext.append(source[result])
            control += 1

    return plaintext

# Print results
print("Key: {0}".format(mykey))
print("\nDecode text:")
print("-> Input text: {0}".format(input_text))
print("-> Coded text: {0}".format(''.join(coder(input_text))))

# Print results
print("\nDecode text:")
print("-> Input text: {0}".format(code_text))
print("-> Decoded text: {0}".format(''.join(decoder(code_text)).lower()))
