import spacy
import classy_classification


def main():
    data = {}

    data["psychological"] = open('gt_data/marked_text_psychological.txt', "r").read().splitlines()
    data["emotional"] = open('gt_data/marked_text_emotional.txt', "r").read().splitlines()
    data["physical"] = open('gt_data/marked_text_physical.txt', "r").read().splitlines()
    data["none"] = open('gt_data/marked_text_none.txt', "r").read().splitlines()
    data["psych and physical"] = open('marked_text_psychAndphys.txt', 'r').read().splitlines()
    data["psych and emotional"] = open('marked_text_psychAndemo.txt', "r").read().splitlines()
    data["phys and emotional"] = open('marked_text_physAndemo.txt', "r").read().splitlines()
    data["phys and emotional and psych"] = open('marked_text_physEmoPsych.txt', "r").read().splitlines()

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

    with open ("data/data_to_analyse2.txt", "r") as f:
        text = f.read()

    sentences = sentence_model(text)

    final_data = []
    for sentence in sentences.sents:
        doc = nlp(sentence.text)
        final_data.append({"sentence": doc.text, "cats": doc._.cats})
    
    for item in final_data:
        if item["cats"]["psych and emotional"] > .8:
            print (item["sentence"].strip())
            print (item["cats"])
            


if __name__ == "__main__":
    main()
