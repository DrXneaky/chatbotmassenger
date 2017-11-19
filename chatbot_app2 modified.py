import os,time
import random
import sys


nameIn = ['what is yourname','whats your name','your name?','name']
greetIn = ['hello','hi there','whats up']
birth = ['what is your date of birth','date of birth?','birth']


nameOut = ['my name is supbot']
greetOut = ['hello','hi there','whats up']



sentence = input('=>')
words = sentence.split()
	
if sentence == '':
	print ('=> Nice meeting you')
	time.sleep(4)
	os.system("sudo shutdowwn -h now")
	
else :
        for word in words:
                if word.lower() in greetIn:
                        print ('=>' + random.choice(greetOut))
                elif word.lower() in nameIn :
                        print ('=>' + random.choice(nameOut))
                elif word.lower() in birth:
                        print ('=> i was born today')
                        
	
