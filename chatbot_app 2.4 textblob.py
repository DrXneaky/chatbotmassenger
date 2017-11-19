import os,time
import random
import sys
from textblob import TextBlob
from base import *


#CONSTANTES
##########################################

complementIn=['ma7lek',':*','n7ebek']
regime_etudeIn=['na9raw','le9raya','l9raya','el9raya','9raya','chna9raw']
supcom_descriptionIn = ['a7kili','chnya','a7kilna','pourquoi']
greetIn = ['ahla','salut','hello','hi']
nameIn = ['chesmek','chesmik','esmek']
supcom =['supcom',"sup'com",'supcom?',"sup'com?",'supcom.',"sup'com.",'supcom!',"sup'com!",'supco',"sup'co"]
first_greetin_message='first greeting message : welcome hope you enjoy '

complement_response=['thanks']
supcom_descriptionOut = 'supcom description '
nameOut = ["my name is sup'bot "]
greetOut = ['hello ','hi there ','whats up ']
regime_etudeOut=['na9raw barcha7ajet fe supcom...']





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

def response_genrator (messageIn,messageOut):
        fck=resp
        for word in words:
                if word.lower() in messageIn :
                        fck= fck +(random.choice(messageOut))
                        break
        return fck

def test (resp):
        if resp=='' or resp==first_greetin_message or variable_for_test==True:
                return False
        else:
                return True

                        




#PROGRAMME PRINCIPALE
############################################


while True:
        resp=''
        sentence = input()
        d=''
        f=''
        variable_for_test=False
                
        sentence_with_blob=TextBlob(sentence)
        words=sentence.split()

        '''check if the user is asking about supcom or something else and generate a response based on that'''
                
        

        if sentence == '':
                print ('=> Nice meeting you')
                time.sleep(4)
                os.system("sudo shutdowwn -h now")
        else:
                        
       
                if not respond_already:
                        resp= first_greetin_message
                        respond_already=True


                for word in words:
                        if word.lower() in greetIn  :
                                variable_for_test=True
                                if  resp == first_greetin_message :
                                        resp= resp+ '.'
                                else:
                                        resp= resp +(random.choice(greetOut))
                                        
                                break

                if not test(resp):
                        resp=response_genrator(nameIn,nameOut)
                        

                if not test(resp):
                        if supcom_in_sentence(words):
                                for word in words:
                                        if word.lower() in supcom_descriptionIn :
                                                resp= resp +supcom_descriptionOut
                                                d='done'
                                                break

                                if d!='done':
                                        if not test(resp):
                                                if resp==response_genrator(regime_etudeIn,regime_etudeOut):
                                                        f='done'

                                                

                                elif f=='done':
                                        resp=resp+ "chet7eb ta3raf 3al sup'com?"
                if not test(resp):
                        resp=response_genrator(regime_etudeIn,regime_etudeOut)

                if not test(resp):
                        resp=response_genrator(complementIn,complement_response)
        
                        

                if resp=='' or resp==first_greetin_message:
                        print("i didn't understand you")
                else :
                        print (resp)



###############################################
                                















        
