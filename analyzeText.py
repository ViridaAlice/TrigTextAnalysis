# Written by Alice Elisabeth Rahn, M-Nr: 122592
# Identifying Triggering Content in Literary Media 
# Magdalena Wolska, SS 2022, University Weimar

import os

def main():
    # Read in hand-annotated split_data.txt as Input
    stripped_text = open('spacy/split_data.txt', 'r')
    
    # Open or create files for the (overlapping) categories as Output
    noViol_sentences = open('gt_data/marked_text_none.txt', 'a')
    physViol_sentences = open('gt_data/marked_text_physical.txt', 'a')
    emoViol_sentences = open('gt_data/marked_text_emotional.txt', 'a')
    psychViol_sentences = open('gt_data/marked_text_psychological.txt', 'a')
    psychAndphysViol_sentences = open('gt_data/marked_text_psychAndphys.txt', 'a')
    psychAndemoViol_sentences = open('gt_data/marked_text_psychAndemo.txt', 'a')
    physAndemoViol_sentences = open('gt_data/marked_text_physAndemo.txt', 'a')
    physEmoPsychViol_sentences = open('gt_data/marked_text_physEmoPsych.txt', 'a')
    
    strippedLines = stripped_text.readlines()
  
    # Evaluate hand-annotated Input and write sentences to respective files depending on their tags
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
            if not phys and psych and emot:
                psychAndemoViol_sentences.write(characterisation[0]+"\n")
            if phys and psych and not emot:
                psychAndphysViol_sentences.write(characterisation[0]+"\n")
            if phys and not psych and emot:
                physAndemoViol_sentences.write(characterisation[0]+"\n")
            if phys and psych and emot:
                physEmoPsychViol_sentences.write(characterisation[0]+"\n")
            

if __name__ == "__main__":
    main()
