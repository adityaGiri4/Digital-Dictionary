import requests
import json
import fileInsert

def run():
    print("This is a Digital Mini Dictionary")
    word = input("Enter your word: \n")
    fileInsert.fileInsert(word)
    try:
        try:
                rawData = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}")
                data = rawData.text
                dataDict = json.loads(data)
                display_data = dataDict[0]["meanings"][0]["definitions"][1]["definition"]
                print(f"The meaning of {word} is :-\n{display_data}\n")
        except:
            print("No meaning found......")
        try:
            print(f'''Sentence of {word} is:-\n{dataDict[0]["meanings"][0]["definitions"][3]["example"]}''')
        except:
            print("No Examples found.....")
    except:
        print("You may be offline, please check your connection")
    


run()
