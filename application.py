from typing import List

class Application:
    ciphertexts: List # ciphertext imported from genCipherMsgs.py
    keys: List        # keys values for each column  
    plaintexts: List  # list of resulting partially decoded messages
    
    def __init__(self, file):
        self.ciphertexts = self.import_ciphertext(file)
        self.keys = ['' for _ in range(len(self.ciphertexts[0]))]
        self.plaintexts = [('_' * len(self.ciphertexts[0])) for _ in range(len(self.ciphertexts))]
        print(self.ciphertexts)

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
        pass
        