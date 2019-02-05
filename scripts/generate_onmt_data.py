from sys import argv
from collections import defaultdict as dd
from random import shuffle

def readanalyses(data,track):
    analyses = {split:dd(set) for split in ['train','dev','test']}
    for split in ['train','dev']:

        fn = '%s/%s-uncovered' % (split, data)
        if split == 'train':
            fn = '%s/%s-uncovered' % (split, data)
        if split == 'test':
            fn = '%s/%s-covered' % (split, data)

        for line in open(fn):
            line = line.strip('\n')
            lan, wf, lemma, pos, msd = line.split('\t')
            lemma = ' '.join(lemma)
            wf = ' '.join(wf)
            msd = msd.split('|')
            a = '%s %s' % (lemma,
                           ' '.join(['+%s' % x for x in [pos] + msd + ["Language=%s" % lan]]))
            analyses[split][wf].add(a)
    return analyses

if __name__=='__main__':
    data = argv[1]
    track = int(argv[2])
    analyses = readanalyses(data,track)

    for split in ['train','dev','test']:
        src = open('onmt-data/%s-track%u-src-%s.txt' % (data,track,split),'w')
        tgt = open('onmt-data/%s-track%u-tgt-%s.txt' % (data,track,split),'w')
        
        split_analyses = list(analyses[split].items())
        shuffle(split_analyses)
        
        for wf, analysis in split_analyses:
            for a in analysis:
                print(wf,file=src)
                print(a,file=tgt)
                
