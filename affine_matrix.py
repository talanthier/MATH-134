import numpy as np
import string

enciphered_message = list(open('sec_5_enciphered_message.txt', 'r').read()) # reads in our enciphered message from text file

alphabet = list(string.ascii_uppercase)
alphabet.extend([' ',',','.','?']) # adds ` ` `,` `.`and `?` to our alphabet

letters_to_num_dict = dict(zip(alphabet, np.arange(30))) # dictionary from letters to elements in Z/30Z
num_to_letters_dict = {v: k for k, v in letters_to_num_dict.items()}


enc_num = list(map(letters_to_num_dict.get, enciphered_message))

A = np.array([[14,5],[3,11]]) # computed in earlier problem
A_inv = (-11*np.array([[11,-5],[-3,14]]))%30 # computed by hand in Z/30Z

enc_num = np.reshape(enc_num, [2, int(len(enc_num)/2)], 'F')
# puts enciphered message units into 2 x length(enc_num) matrix

message_num = np.dot(A_inv,enc_num)
message_num = message_num.flatten('F') % 30 # flattens our matrix to 1-d array

msg = ''
msg = msg.join(map(num_to_letters_dict.get, message_num)) # maps message_num back to our alphabet

print(msg)
