import spacy
import classy_classification


def main():
    data = {}

    data["psychological"] = open('gt_data/marked_text_psychological.txt', "r").read().splitlines()
    data["emotional"] = open('gt_data/marked_text_emotional.txt', "r").read().splitlines()
    data["physical"] = open('gt_data/marked_text_physical.txt', "r").read().splitlines()
    data["none"] = open('gt_data/marked_text_none.txt', "r").read().splitlines()
    data["psych and physical"] = open('gt_data/marked_text_psychAndphys.txt', 'r').read().splitlines()
    data["psych and emotional"] = open('gt_data/marked_text_psychAndemo.txt', "r").read().splitlines()
    data["phys and emotional"] = open('gt_data/marked_text_physAndemo.txt', "r").read().splitlines()
    data["phys and emotional and psych"] = open('gt_data/marked_text_physEmoPsych.txt', "r").read().splitlines()

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

    with open ("gt_data/data_to_analyse.txt", "r") as f:
        text = f.read()

    sentences = sentence_model(text)

    final_data = []
    for sentence in sentences.sents:
        doc = nlp(sentence.text)
        final_data.append({"sentence": doc.text, "cats": doc._.cats})
    
    noViol_sentences = open('spacy/marked_text_none.txt', 'w')
    physViol_sentences = open('spacy/marked_text_physical.txt', 'w')
    emoViol_sentences = open('spacy/marked_text_emotional.txt', 'w')
    psychViol_sentences = open('spacy/marked_text_psychological.txt', 'w')
    psychAndphysViol_sentences = open('spacy/marked_text_psychAndphys.txt', 'w')
    psychAndemoViol_sentences = open('spacy/marked_text_psychAndemo.txt', 'w')
    physAndemoViol_sentences = open('spacy/marked_text_physAndemo.txt', 'w')
    physEmoPsychViol_sentences = open('spacy/marked_text_physEmoPsych.txt', 'w')

    for item in final_data:
        if item["cats"]["psychological"] > .8:
            psychViol_sentences.write("'"+item["sentence"].strip()+"': "+str(item["cats"])+"\n")
        if item["cats"]["emotional"] > .8:
            emoViol_sentences.write("'"+item["sentence"].strip()+"': "+str(item["cats"])+"\n")
        if item["cats"]["physical"] > .8:
            physViol_sentences.write("'"+item["sentence"].strip()+"': "+str(item["cats"])+"\n")
        if item["cats"]["none"] > .8:
            noViol_sentences.write("'"+item["sentence"].strip()+"': "+str(item["cats"])+"\n")
        if item["cats"]["psych and physical"] > .8:
            psychAndphysViol_sentences.write("'"+item["sentence"].strip()+"': "+str(item["cats"])+"\n")
        if item["cats"]["psych and emotional"] > .8:
            psychAndemoViol_sentences.write("'"+item["sentence"].strip()+"': "+str(item["cats"])+"\n")
        if item["cats"]["phys and emotional"] > .8:
            physAndemoViol_sentences.write("'"+item["sentence"].strip()+"': "+str(item["cats"])+"\n")
        if item["cats"]["phys and emotional and psych"] > .8:
            physEmoPsychViol_sentences.write("'"+item["sentence"].strip()+"': "+str(item["cats"])+"\n")
            


if __name__ == "__main__":
    main()
