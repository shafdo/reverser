
import sys


class Main():
    def __init__(self):
        if len(sys.argv) == 1:
            user_para = input("Write text here: ")
            words = user_para.split(" ")
            words = (words[::-1])
            print(' '.join(words))

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
 python reverser.py Hello world      prints "World Hello"
 python reverser.py -f <File Name>   Reads from file and print reverse
 python reverser.py --help           Show help (-h/--help)
'''
        print(h)





run = Main()



