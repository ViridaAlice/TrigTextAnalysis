# Written by Alice Elisabeth Rahn, M-Nr: 122592
# Identifying Triggering Content in Literary Media 
# Magdalena Wolska, SS 2022, University Weimar

import spacy
import classy_classification

def main():
    data = {}

    # Read in all categories together with their hand-annotated groundtruth data,
    # split by categories and mixes thereof
    data["psychological"] = open('gt_data/marked_text_psychological.txt', "r").read().splitlines()
    data["emotional"] = open('gt_data/marked_text_emotional.txt', "r").read().splitlines()
    data["physical"] = open('gt_data/marked_text_physical.txt', "r").read().splitlines()
    data["none"] = open('gt_data/marked_text_none.txt', "r").read().splitlines()
    data["psych and physical"] = open('gt_data/marked_text_psychAndphys.txt', 'r').read().splitlines()
    data["psych and emotional"] = open('gt_data/marked_text_psychAndemo.txt', "r").read().splitlines()
    data["phys and emotional"] = open('gt_data/marked_text_physAndemo.txt', "r").read().splitlines()
    data["phys and emotional and psych"] = open('gt_data/marked_text_physEmoPsych.txt', "r").read().splitlines()

    # Initalize Spacy Text Categorizer
    nlp = spacy.blank("en")
    nlp.add_pipe(
        "text_categorizer", 
        config={
            "data": data, 
            "model": "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2",
            "device": "cpu"
        }
    )  

    sentence_model = spacy.blank("en")
    sentence_model.add_pipe("sentencizer")

    # Read in external, untagged but split sentences as Input
    with open ("spacy/split_data.txt", "r", encoding="utf-8") as f:
        text = f.read()
    sentences = sentence_model(text)

    final_data = []
    for sentence in sentences.sents:
        doc = nlp(sentence.text)
        final_data.append({"sentence": doc.text, "cats": doc._.cats})
    
    # Append data to respective file depending on their category/-ies
    noViol_sentences = open('spacy/marked_text_none.txt', 'a+', encoding="utf-8")
    physViol_sentences = open('spacy/marked_text_physical.txt', 'a+', encoding="utf-8")
    emoViol_sentences = open('spacy/marked_text_emotional.txt', 'a+', encoding="utf-8")
    psychViol_sentences = open('spacy/marked_text_psychological.txt', 'a+', encoding="utf-8")
    psychAndphysViol_sentences = open('spacy/marked_text_psychAndphys.txt', 'a+', encoding="utf-8")
    psychAndemoViol_sentences = open('spacy/marked_text_psychAndemo.txt', 'a+', encoding="utf-8")
    physAndemoViol_sentences = open('spacy/marked_text_physAndemo.txt', 'a+', encoding="utf-8")
    physEmoPsychViol_sentences = open('spacy/marked_text_physEmoPsych.txt', 'a+', encoding="utf-8")

    # Thresholds for certain categories (sensitivity low for possible violence, higher for none)
    # Write results to respective file
    for item in final_data:
        if item["cats"]["psychological"] > .2:
            psychViol_sentences.write("'"+item["sentence"].strip()+"': "+str(item["cats"])+"\n")
        if item["cats"]["emotional"] > .2:
            emoViol_sentences.write("'"+item["sentence"].strip()+"': "+str(item["cats"])+"\n")
        if item["cats"]["physical"] > .2:
            physViol_sentences.write("'"+item["sentence"].strip()+"': "+str(item["cats"])+"\n")
        if item["cats"]["none"] > .8:
            noViol_sentences.write("'"+item["sentence"].strip()+"': "+str(item["cats"])+"\n")
        if item["cats"]["psych and physical"] > .2:
            psychAndphysViol_sentences.write("'"+item["sentence"].strip()+"': "+str(item["cats"])+"\n")
        if item["cats"]["psych and emotional"] > .2:
            psychAndemoViol_sentences.write("'"+item["sentence"].strip()+"': "+str(item["cats"])+"\n")
        if item["cats"]["phys and emotional"] > .2:
            physAndemoViol_sentences.write("'"+item["sentence"].strip()+"': "+str(item["cats"])+"\n")
        if item["cats"]["phys and emotional and psych"] > .2:
            physEmoPsychViol_sentences.write("'"+item["sentence"].strip()+"': "+str(item["cats"])+"\n")
            
if __name__ == "__main__":
    main()
