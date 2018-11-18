import operator

y = open(r"C:\Users\wesam\Desktop\test_file.txt")
text = y.read()
y.close()

def start(text):
    wordlist = []
    for word in text.lower().split():
        wordlist.append(word)
    list_cleaner(wordlist)

def list_cleaner(wordlist):
    cleanlist=[]
    for item in wordlist:
        symbols = ".,\"()_-"
        for i in range(0, len(symbols)):
            item=item.replace(symbols[i], "")
        if len(item) > 0:
            cleanlist.append(item)
    word_counter(cleanlist)


def word_counter(cleanlist):
    counter={}
    for word in cleanlist:
        if word in counter:
            counter[word]+=1
        else:
            counter[word]=1
    for (key, value) in sorted(counter.items(), key=operator.itemgetter(1)):
        print (key, value)
start(text)
