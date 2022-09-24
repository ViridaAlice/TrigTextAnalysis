import os

def main():
    stripped_text = open('split_text.txt', 'r')
    
    noViol_sentences = open('marked_text_none.txt', 'w')
    physViol_sentences = open('marked_text_physical.txt', 'w')
    emoViol_sentences = open('marked_text_emotional.txt', 'w')
    psychViol_sentences = open('marked_text_psychological.txt', 'w')
    psychAndphysViol_sentences = open('marked_text_psychAndphys.txt', 'w')
    psychAndemoViol_sentences = open('marked_text_psychAndemo.txt', 'w')
    physAndemoViol_sentences = open('marked_text_physAndemo.txt', 'w')
    physEmoPsychViol_sentences = open('marked_text_physEmoPsych.txt', 'w')
    
    strippedLines = stripped_text.readlines()
  
    # Strips the newline character
    for line in strippedLines:
        characterisation = line.split("{")
        if len(characterisation) == 2:
            tagList = characterisation[1].split(",")
            phys, psych, emot = False, False, False
            if any(tag.strip("}").strip() == "physical_violence: y" for tag in tagList):
                phys = True
            if any((tag.strip("}").strip() == "emotional_violence: y" or \
                tag.strip("}").strip() == "emotional_violence: y}") for tag in tagList):
                emot = True
            if any(tag.strip("}").strip() == "psychological_violence: y" for tag in tagList):
                psych = True
            if not phys and not psych and not emot:
                noViol_sentences.write(characterisation[0]+"\n")
            if phys and not psych and not emot:
                physViol_sentences.write(characterisation[0]+"\n")
            if not phys and psych and not emot:
                psychViol_sentences.write(characterisation[0]+"\n")
            if not phys and not psych and emot:
                emoViol_sentences.write(characterisation[0]+"\n")
            if phys and not psych and emot:
                psychAndemoViol_sentences.write(characterisation[0]+"\n")
            if phys and psych and not emot:
                psychAndphysViol_sentences.write(characterisation[0]+"\n")
            if phys and not psych and emot:
                physAndemoViol_sentences.write(characterisation[0]+"\n")
            if phys and psych and emot:
                physEmoPsychViol_sentences.write(characterisation[0]+"\n")
            


            """
            tagged = False
            if tagList[0].strip("}").strip() == "physical_violence: y" and \
                tagList[1].strip("}").strip() == "psychological_violence: n" and \
                tagList[2].strip("}").strip() == "emotional_violence: n":
                    physViol_sentences.write(characterisation[0]+"\n")
                    tagged = True
            if tag.strip("}").strip() == "emotional_violence: y" or tag.strip("}").strip() == "emotional_violence: y}":
                emoViol_sentences.write(characterisation[0]+"\n")
                tagged = True
            if tag.strip("}").strip() == "psychological_violence: y":
                psychViol_sentences.write(characterisation[0]+"\n")
                tagged = True
            if tagged == False:
                noViol_sentences.write(characterisation[0]+"\n")
            """


if __name__ == "__main__":
    main()
