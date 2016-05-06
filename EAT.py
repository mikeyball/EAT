import sys
def main():
    text = loadFile()
    average = averageNumberOfWords(text)

    print ("Average number of words per sentence: ", int(average))
    if average>10:
        print ("There is room for improvement!")
    else:
        print ("Great job!")


def averageNumberOfWords(text):
    sentences = splitBySeparators(text)

    num = 0
    for s in sentences:
        num = num + calcWords(s)

    return num / len(sentences)



def calcWords(sentence):
    sentence = clearSentence(sentence)
    count = 0
    for w in sentence.split(" "):
        if len(w)>2:
            count = count + 1
    return count


def clearSentence(sentence):
    separators = ['.', ',', '!', '?', ':', ';', ')', '(', ',', '\'', '"', '/', '%', '$', '@', '#']
    for sp in separators:
        sentence = sentence.replace(sp, '')
    return sentence


def splitBySeparators(str):
    separators =['.', '?', '!', ';']
    start = 0
    s_split = []
    for i in range(len(str)):
        if str[i] in separators:
            s_split.append(str[start:i])
            start = i + 1

    return s_split

def loadFile():

    fileName = sys.argv[1]
    try:
        file = open(fileName)
    except:
        print("Please enter file in .txt format!")
    return file.read()


main()