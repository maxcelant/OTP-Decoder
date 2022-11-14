import sys
from application import Application 

def main():
    try:
        file = sys.argv[1]
        app = Application(file)
    except:
        print('Error occured, no file given')


if __name__ == '__main__':
    main()