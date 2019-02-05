from sys import argv, stderr
from collections import defaultdict as dd

def readdata(fn):
    data = {"analysis":dd(set),"lemma":dd(set),"tag":dd(set)}
    for line in open(fn):
        line = line.strip('\n')
        if line:
            lan, wf, lemma, pos, msd = line.split('\t')
            data["analysis"][wf].add((lemma,pos,msd))
            data["lemma"][wf].add(lemma)
            data["tag"][wf].add((pos,msd))
    return data

if __name__=="__main__":
    if len(argv) != 3:
        print("USAGE: %s results/LAN-trackN-dev-covered.sys LAN-uncovered" % argv[0],file=stderr)
        exit(1)
    sysdata = readdata(argv[1])
    golddata = readdata(argv[2])
    for otype in ["analysis","lemma","tag"]:
        tp = 0
        fp = 0
        fn = 0 
        for wf in sysdata[otype]:
            tp += len(sysdata[otype][wf] & golddata[otype][wf])
            fp += len(sysdata[otype][wf] - golddata[otype][wf])
            fn += len(golddata[otype][wf] - sysdata[otype][wf])
        recall = tp/(tp+fn)
        precision = tp/(tp+fp)
        fscore = 2 * recall * precision / (recall + precision)
        print("Recall for %s: %.2f" % (otype,recall*100))
        print("Precision for %s: %.2f" % (otype,precision*100))
        print("F1-score for %s: %.2f" % (otype,fscore*100))
        print()
