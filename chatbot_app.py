import os,time
import random
import sys


nameIn = ['what is yourname','whats your name','your name?']
greetIn = ['hello','hi there','whats up']
birth = ['what is your date of birth','date of birth?']


nameOut = ['my name is supbot']
greetOut = ['hello','hi there','whats up']



sentence = input('=>')
words = sentence.split()
for word in words:
        if word.lower() in greetIn:
                print ('=>' + random.choice(greetOut))
	




