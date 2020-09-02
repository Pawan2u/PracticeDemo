



def countUnique(sentence):
    sent=sentence.split(" ")
    words=[]
    for word in sent:
        if word not in words:
            words.append(word)
    return len(words) 
    





sentence="This is a pen and this pen is red"

print(countUnique(sentence))