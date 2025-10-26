import numpy as np
import re
from Responses_data import Responses

def keywordsending(user):
    real_text = re.sub(r'[^a-zA-Z]', '', user)
    result = 'No'
    for i in range(len(real_text)):
        for j in range(i + 1, len(real_text) + 1):
            new_string = real_text[i:j]
            result = keywordchceking(new_string)
            if (result != 'No'):
                return result
    return 'No'

def keywordchceking(real_text):
    word = list(Responses.keys())

    for bigword in range(0, len(word)):
        for eachword in range(0, len(word[bigword])):
            wording = re.sub(r'[^a-zA-Z]', '', word[bigword][eachword])
            check = re.search(real_text, wording)

            if ((check != None) & (len(real_text) >= 3)):
                return (word[bigword][eachword])
    return 'No'

Rand_func = lambda x: np.random.randint(0, len(x))

R1 = ["Hi!!!, ", "Hello, Welcome!!", "Hey Their how is your day going?"]
R2 = ["How can i serve you today?", "Is thier anything i can help you with today", "How can i help you today",
      "What bring you today?", "What are we learning today"]

print("""\n\n\t\t\t CHATBOT!!!\n\n\n""")
print(R1[Rand_func(R1)])
all_keys = Responses.keys()
done = set()
while True:
    user = input("Enter what you want:").lower()
    result = keywordsending(user)

    if (result != 'No'):
        for key, value in Responses.items():
            if (key in done):
                print("Already responded!!!")
                break

            if result in key:
                print(value[Rand_func(value)])
                done.add(key)
                break
    else:
        print("Invalid responce")