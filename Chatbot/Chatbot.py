import numpy as np
import re
from Responses_data import Responses
# np.random.seed(1)

def keywordsending(user):
    # now i need to all knd of data checking 
    # print(user)
    #first i need to remove the spaces from text 
    real_text=re.sub(r'[^a-zA-Z]', '', user)
    #i am gonna loop all over the characters and find the sub stringa and all the ppossible wyay 
    result='No'
    for i in range ( len(real_text)):
        for j in range(i+1,len(real_text)+1):
           
            new_string=real_text[i:j]
            result=keywordchceking(new_string)
            if(result!='No'):#something is wrong here

                # print(i,j)
                # print(result,"vsdkh")
                return result

    return 'No'
def keywordchceking(real_text):
    # m=re.search(real_text,r"games_  2")

    word=list(Responses.keys())

    for bigword in range(0,len(word)):
        for eachword in range(0,len(word[bigword])):
            # print(word[bigword][smallword]) now i have every key word acces
            wording=re.sub(r'[^a-zA-Z]', '', word[bigword][eachword]) 
            check=re.search(real_text,wording)
            # print(wording)

            if((check!=None)&(len(real_text)>=3) ):#this condition needs a proper fix 
                # print(word[bigword][eachword])
                return(word[bigword][eachword])
           
            
    return 'No'
    
    #here i need to check every possible way to see the sting 
    pass    
    
    
Rand_func=lambda x:np.random.randint(0,len(x))
#i need a first responce for hi 
R1=["Hi!!!, ","Hello, Welcome!!","Hey Their how is your day going?"]
R2=["How can i serve you today?","Is thier anything i can help you with today","How can i help you today",
                   "What bring you today?","What are we learning today"]

print("""\n\n\t\t\t CHATBOT!!!\n\n\n""")
print(R1[Rand_func(R1)])
# print(f"{R2[Rand_func(R2)]}\nBy-->\n")
# Responses = {
#     ("play game", "start game", "let's play"): ["Ok!", "Let's go!", "Game started!"],
#     ("wahtsapp", "hello", "hey"):["Hi!!!, ","Hello, Welcome!!","Hey Their how is your day going?"]
   
# }
all_keys=Responses.keys()
# print(all_keys)
done=set()
while True:
    user=input("Enter what you want:").lower()
    result=keywordsending(user)
    
    if (result!='No'):
        # print(result)
        for key,value in Responses.items():
            # if(key in done):
            #     print("Already responded!!!")
            #     break
            
            if   result in key :
                print(value[Rand_func(value)])
                done.add(key)
        pass
    
    else:
        print("Invalid responce")
        
        pass
     
    
    

# if('NO'=='NO'):
#     print("fkfjndhji")
# user="gabjwjfkgame"
# keywordsending(user)


#gona have to rewrite the complete function and then boom
# while True :
#     for key,value in Responses.items():

#         # if (any(word in user for word in key)): even if the single letter macthe swe will get this output
#         user=input("Enter what you want:").lower()
#         done=set()
#         if (keywordsending(user) !='NO'):# i can work so much on the user data which is typed and full fill th eresponce 
#             if(key in done):# here also i need to add another function to baalnce out everthing to makw them good
#                 print("Already done")
#                 break
#                 # print(Responses[key])
                
#             print(f"{np.random.choice(value)}")#it is working but the responce is being with all th ekeys
#             done.add(key)
#             break
#         else:
#             print("Invalid responce!!!!")

    
    
           
        

