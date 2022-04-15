def  fileInsert(word):
    with open("dataWords.txt", 'a') as fileHandle:
        fileHandle.write(f"Word searched is {word}\n")
