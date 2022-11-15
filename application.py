from typing import List

class Application:
    ciphertexts: List # Ciphertext imported from genCipherMsgs.py
    key: List         # Keys values for each column  
    plaintexts: List  # List of resulting partially decoded messages
    
    def __init__(self, file):
        self.ciphertexts = self.import_ciphertext(file)
        self.key = ['' for _ in range(len(self.ciphertexts[0]) // 2)]
        self.plaintexts = [['_' for _ in range(len(self.ciphertexts[0]) // 2)] for _ in range(len(self.ciphertexts))]

    # Runs the functions that decipher the given text
    # And then display the finished product in the terminal
    def run(self):
        self.compare()
        self.decode_text()
        self.print()
    
    
    # Reads the ciphertext from the input file
    def import_ciphertext(self, file):
        try:
            f = open(file, "r")
            c = f.readlines()
            temp = []
            for cipher in c:
                temp.append(cipher.strip())
        except:
            print('Something went wrong reading the file')
        finally:
            f.close()
            
        return temp
                    
    
    # Compare the ciphertexts to try to find whitespaces
    # If we find a whitespace, we find the key for that column
    def compare(self):
        c = [] # temp variable
        
        # turns our cipher string into blocks of 1 hexadecimal
        for text in self.ciphertexts:
            c.append([text[i] + text[i+1] for i in range(0, len(text), 2)])
        
        # Compares each row with other rows
        for i in range(len(c)):
            j = k = 0
            # Compare the j-th column of the [i] and [k] rows
            while j < len(c[0]):
                c1 = c[i][j]
                
                # We don't want to compare the row with itself
                if k == i and k + 1 < len(c):
                    k += 1
                
                c2 = c[k][j]
                # Result will return an integer value
                res = self.calculate_XOR(c1, c2)
                # If the result is not a whitespace, skip it
                if res < 65 and res > 0:
                    j += 1
                    k = 0
                # If it is a (possible) whitespace, check all the rows in this column
                else:
                    k += 1
                
                # Key is found for this column, continue column index [j] and reset row index [k]
                if k == len(c):
                    self.calculate_key(c1, j)
                    j += 1   
                    k = 0
                     
    
    # Perform XOR and returns the decimal ASCII value 
    def calculate_XOR(self, c1, c2):      
        c1, c2 = chr(int(c1, 16)), chr(int(c2, 16)) # get the ASCII value for c1 and c2
        res = ord(c1) ^ ord(c2)                     # return the result of c1 XOR c2
        return res
    
    
    # Calculates the key of the i-th column
    def calculate_key(self, c, i):
        if not self.key[i]:
            # K[i] = (32 XOR c)
            self.key[i] = ord(' ') ^ ord(chr(int(c, 16)))
            
    
    # Creates the decoded plaintext from the given key
    def decode_text(self):
        for i, text in enumerate(self.ciphertexts):
            # Turns our cipher string into blocks of 1 hexadecimal 
            text = [text[i] + text[i+1] for i in range(0, len(text), 2)]
            for j in range(len(text)):
                # If the key at the j-th position exists...
                if self.key[j] != '':
                    self.plaintexts[i][j] = self.get_letter(self.key[j], text[j])
                    

    # Returns the ASCII character from the (k XOR c)
    def get_letter(self, key, cipher_letter):
        # Perform (k XOR c)
        plaintext_letter = key ^ ord(chr(int(cipher_letter, 16)))
        return chr(plaintext_letter)
    
    
    # Prints out the (mostly) legible plaintext
    def print(self):
        for text in self.plaintexts:
            print("".join(text))