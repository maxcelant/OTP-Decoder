from time import sleep
from typing import List

class Application:
    ciphertexts: List # Ciphertext imported from genCipherMsgs.py
    key: List         # Keys values for each column  
    plaintexts: List  # List of resulting partially decoded messages
    
    def __init__(self, file):
        self.ciphertexts = self.import_ciphertext(file)
        self.key = ['' for _ in range(len(self.ciphertexts[0]) // 2)]
        self.plaintexts = [['_' for _ in range(len(self.ciphertexts[0]) // 2)] for _ in range(len(self.ciphertexts))]
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
                    
    
    def compare(self):
        c = []
        
        # turns our 
        for text in self.ciphertexts:
            c.append([text[i] + text[i+1] for i in range(0, len(text), 2)])
        
        for i in range(len(c)):
            j = k = 0
            while j < len(c[0]):
                c1 = c[i][j]
                
                # We don't want to compare the row with itself
                if k == i and k + 1 < len(c):
                    k += 1
                
                c2 = c[k][j]
                res = self.calculate_XOR(c1, c2)
                # If the result is not a whitespace, skip it
                if res < 65 and res > 0:
                    j += 1
                    k = 0
                # If it is a (possible) whitespace, check all the rows in this column
                else:
                    k += 1
                
                # Key is found for this column, continue column index and reset row index
                if k == len(c):
                    self.calculate_key(c1, j)
                    j += 1   
                    k = 0
                     
    
    # Perform XOR and returns the decimal ASCII value 
    def calculate_XOR(self, c1, c2):      
        c1, c2 = chr(int(c1, 16)), chr(int(c2, 16))
        res = ord(c1) ^ ord(c2)
        return res
    
    
    # Calculates the key of the i-th column
    def calculate_key(self, c, i):
        if self.key[i] == '':
            self.key[i] = ord(' ') ^ ord(chr(int(c, 16)))
            
    
    def decode_text(self):
        for i, text in enumerate(self.ciphertexts):
            text = [text[i] + text[i+1] for i in range(0, len(text), 2)]
            for j in range(len(text)):
                if self.key[j] != '':
                    self.plaintexts[i][j] = self.get_letter(self.key[j], text[j])
                    

    def get_letter(self, key, cipher_letter):
        plaintext_letter = key ^ ord(chr(int(cipher_letter, 16)))
        return chr(plaintext_letter)
    
    
    def print(self):
        for text in self.plaintexts:
            print("".join(text))