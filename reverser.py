#!/bin/python3
import sys
import time


class Main():
    def __init__(self):
        if len(sys.argv) == 1:

            try:
                for i in sys.stdin:
                    i = i.strip("\n")
                    temp = i.split(" ")
                    print(" ".join(temp[::-1]))
                    
            except:
                print("\n[-] Exiting ...\n")
                sys.exit()



        elif "-f" in sys.argv:
            file = sys.argv[sys.argv.index("-f")+1]
            try:
                with open(file,"r") as f:
                    data = f.read().split(" ")
                    print(' '.join(data[::-1]))

            except:
                print("[-] Unable To Read From File")
                sys.exit
                
        elif "-h" == sys.argv[1] or "--help" == sys.argv[1]:
            self.help()
                    
        else:
            text = sys.argv[1:]
            revtext = text[::-1]
            print(' '.join(revtext))
            


    def help(self):
        h = '''
 USAGE
 -----
 Linux:
    python3 reverser.py Hello world         Outputs "World Hello"
    python3 reverser.py -f <File Name>      Reads from file and print reverse
    python3 reverser.py --help              Show help (-h/--help)
  
    echo Hello World | python3 reverser.py  Piping to reverser


 Windows:
    python reverser.py Hello world          Outputs "World Hello"
    python reverser.py -f <File Name>       Reads from file and print reverse
    python reverser.py --help               Show help (-h/--help)

'''
        print(h)





run = Main()



