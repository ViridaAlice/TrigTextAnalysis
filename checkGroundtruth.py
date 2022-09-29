# Written by Alice Elisabeth Rahn, M-Nr: 122592
# Identifying Triggering Content in Literary Media 
# Magdalena Wolska, SS 2022, University Weimar

def main():
    cat = "psychological"
    checkFile = open('spacy/marked_text_'+cat+'.txt', 'r', encoding="utf-8")

    checkedSet = []
    for line in checkFile:
        print("\n"+line.split(": {")[0].strip("'")+"\n")
        if input("Does this line contain "+cat +" abuse?") == "y":
            checkedSet.append(line.split(": {")[0].strip("'"))

    outfile = open('gt_data/marked_text_'+cat+'_corr.txt', 'a+', encoding="utf-8")
    for el in checkedSet:
        outfile.write(el+"\n")
            
if __name__ == "__main__":
    main()
