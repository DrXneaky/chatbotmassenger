import os,time
import random
import sys
from textblob import TextBlob


#CONSTANTES
##########################################


supcom_descriptionIn = ['supcom description']
greetIn = ['hello','hithere','whats up']
nameIn = ['chesmek','chesmik','esmek']
supcom =['supcom',"sup'com",'supcom?',"sup'com?",'supcom.',"sup'com.",'supcom!',"sup'com!"]
first_greetin_message='first greeting message : welcome hope you enjoy '

supcom_descriptionOut = ['supcom description ']
nameOut = ["my name is sup'bot "]
greetOut = ['hello ','hi there ','whats up ']



#INITIALISATION
##################################################
respond_already=False




#FONCTIONS
#####################################################
def supcom_in_sentence(words):
        spcm= False
        for word in words :
                if word in supcom :
                        spcm=True
        return spcm
        
                        




#PROGRAMME PRINCIPALE
##################################################


while True:
        resp=''
        sentence = input()
        
                
        sentence_with_blob=TextBlob(sentence)
        words=sentence.split()

        '''check if the user is asking about supcom or something else and generate a response based on that'''
                
        

        print (supcom_in_sentence(words))
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
                for word in words:
                        if word in nameIn :
                                resp= resp +(random.choice(nameOut))
                                break

                for word in words:
                        if word in nameIn :
                                resp= resp +(random.choice(nameOut))
                                break
                for word in words:
                        if word in nameIn :
                                resp= resp +(random.choice(nameOut))
                                break

                for word in words:
                        if word in nameIn :
                                resp= resp +(random.choice(nameOut))
                                break
                for word in words:
                        if word in nameIn :
                                resp= resp +(random.choice(nameOut))
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



###############################################################
                                















        
