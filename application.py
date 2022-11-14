from typing import List

class Application:
    ciphertexts: List # ciphertext imported from genCipherMsgs.py
    key: List         # keys values for each column  
    plaintexts: List  # list of resulting partially decoded messages
    
    def __init__(self, file):
        self.ciphertexts = self.import_ciphertext(file)
        self.key = ['' for _ in range(len(self.ciphertexts[0]))]
        self.plaintexts = [('_' * len(self.ciphertexts[0])) for _ in range(len(self.ciphertexts))]
        self.compare()

    
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
        for i in range(len(self.ciphertexts)):
            for j in range(0, len(self.ciphertexts[0]), 2):
                c1 = self.ciphertexts[i][j:j+2]
                for k in range(len(self.ciphertexts)):
                    c2 = self.ciphertexts[k][j:j+2]
                    result = self.calculate_XOR(c1, c2)
                    if result > 0 and result < 65:     # not a whitespace
                        break
                    if k == len(self.ciphertexts) - 1: # made it to the end
                        self.calculate_key(c1, j)
                    
                
    
    # perform XOR and returns the decimal ASCII value 
    def calculate_XOR(self, c1, c2):      
        c1, c2 = chr(int(c1, 16)), chr(int(c2, 16))
        res = ord(c1) ^ ord(c2)
        return res
    
    
    # calculates the key of the i-th column
    def calculate_key(self, c, i):
        self.key[i] = ord(' ') ^ ord(chr(int(c, 16)))
        print(self.key)