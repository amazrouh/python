import json
from difflib import get_close_matches


data = json.load(open("data.json",'r'))

def Translate(word):
    word = word.lower()

    if word in data:
        return data[word]
    else:
        matches = get_close_matches(word, data.keys())
        if len(matches) > 0:
            answer = input("Do you mean %s instead" % matches[0] + " Y/N: ")
            if(str(answer).lower() == 'y'):
                return data[matches[0]]
            else:
                return "The word does not exist"
        else:
            return "The word does not exist"


word = input("enter the word: ")

output = Translate(word)
i = 1
print("output type : " + str(type(output)))

if type(output) == list:
    for item in output:
        print(str(i) + "-" + item)
        i += 1
else:
    print(output)


