import os
import nltk

nltk.download('punkt')

def main():
    tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
    fp = open("data_to_analyse.txt", 'r')
    data = fp.read()
    split_text = '\n\n'.join(tokenizer.tokenize(data))
    i = 0
    fp = open("split_text_data.txt", 'a')
    analizeText = tokenizer.tokenize(data)
    """
    for item in analizeText:
        print("\n"+item+"\n")
        fp.write(item+" {physical_violence: "+input("Does this excerpt contain physical violence? (Kicking, Slapping, Choking...)")+
                 ", emotional_violence: "+input("Does this excerpt contain emotional abuse? (Isolation, Victim blaming, Jealousy...)")+
                 ", psychological_violence: "+input("Does this excerpt contain psychological abuse? (Gaslighting, Coercion, Guilt-tripping...)")
                 +"}\n")
        i +=1
    """
    for item in analizeText:
        fp.write(item+"\n")
        
if __name__ == "__main__":
    main()
