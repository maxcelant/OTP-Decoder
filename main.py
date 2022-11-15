import sys
from application import Application 

'''
    - Massimiliano Celant (mc1189)
    - 11/14/2022
    - CSCE 3550
'''

def main():
    try:
        file_name = sys.argv[1]      # Get file name from command line
        app = Application(file_name) # Create instance
        app.run()                    # Run project
    except:
        print('ERROR: No text file with ciphertext information given as command line arguement')
        return
    
if __name__ == '__main__':
    main()