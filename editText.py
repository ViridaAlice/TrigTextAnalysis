# Written by Alice Elisabeth Rahn, M-Nr: 122592
# Identifying Triggering Content in Literary Media 
# Magdalena Wolska, SS 2022, University Weimar

import os
import nltk

nltk.download('punkt')

def handAnnotation(analyseText):
    """
    Prints the text analyseText Sentence by sentence to the cmd line and allows easy user annotation
    """
    fp = open("spacy/split_data.txt", 'a', encoding="UTF-8")
    for item in analyseText:
        print("\n"+item+"\n")
        fp.write(item+" {physical_violence: "+input("Does this excerpt contain physical violence? (Kicking, Slapping, Choking...)")+
                 ", emotional_violence: "+input("Does this excerpt contain emotional abuse? (Isolation, Victim blaming, Jealousy...)")+
                 ", psychological_violence: "+input("Does this excerpt contain psychological abuse? (Gaslighting, Coercion, Guilt-tripping...)")
                 +"}\n")
    
def main():
    tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
    
    # Read Data provided in file data_to_analyse.txt
    fp = open("spacy/data_to_be_analysed.txt", 'r', encoding="UTF-8")
    data = fp.read()
    analyseText = tokenizer.tokenize(data)
    
    #Alternative usage: Print every sentence in cmd-line for hand-annotation
    #handAnnotation(analyseText)

    fp = open("spacy/split_data.txt", "w+", encoding="utf-8")

    for item in analyseText:
        fp.write(item+"\n")
        
if __name__ == "__main__":
    main()
