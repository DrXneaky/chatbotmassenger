import os,time
import random
import sys
from textblob import TextBlob
from base import *




#INITIALISATION
############################################
respond_already=False




#FONCTIONS
############################################
def supcom_in_sentence(words):
        spcm= False
        for word in words :
                if word in supcom :
                        spcm=True
        return spcm


        
                        




#PROGRAMME PRINCIPALE
############################################


while True:
        resp=''
        sentence = input()
        d=''
        
                
        sentence_with_blob=TextBlob(sentence)
        words=sentence.split()

        '''check if the user is asking about supcom or something else and generate a response based on that'''
                
        

        if sentence == '':
                print ('=> Nice meeting you')
                time.sleep(4)
                os.system("sudo shutdowwn -h now")
        else:
                        
       
                if respond_already==False:
                        resp= first_greetin_message
                        respond_already=True

                
                for word in words:
                        if word in nameIn :
                                resp= resp +(random.choice(nameOut))
                                break
                        
                

        
                if supcom_in_sentence(words):
                        for word in words:
                                if word in supcom_descriptionIn :
                                        resp= resp +supcom_descriptionOut
                                        d='done'
                                        break
                        if d!='done':
                                resp=resp+ "chet7eb ta3raf 3al sup'com?"

                for word in words:
                        if word in complementIn :
                                resp= resp +(random.choice(complement_response))
                                break
                for word in words:
                        if word in regime_etudeIn :
                                resp= resp +(random.choice(regime_etudeOut))
                                break
        
                for word in words:
                        if word in greetIn  :
                                if  resp == first_greetin_message :
                                        resp= resp+ '\n'
                                else:
                                        resp= resp +(random.choice(greetOut))
                                break

                if resp=='' or resp==first_greetin_message  :
                        print("i didn't understand you")
                else :
                        print (resp)



###############################################
                                















        
