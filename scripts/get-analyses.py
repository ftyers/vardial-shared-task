from sys import stdin, argv
from math import exp

def get_analysis(a):
    a = [c for c in a.split(' ') if c != '']
    letters = [c for c in a if c == '+' or c[0] != '+']
    tags = [c for c in a if c != '+' and c[0] == '+']

    pos = [t[1:] for t in tags if not '=' in t]
    if pos == []:
        pos = 'NOUN'

    msd = [t[1:] for t in tags if '=' in t and not 'Language' in t]
    if msd == []:
        msd = ['_']

    return (''.join(letters),pos[0],'|'.join(msd))

def read_analysis_set(f,analyses):
    read = 0
    input_wf = ''
    for line in f:
        line = line.strip('\n')
        if line.find('SENT') == 0:
            input_wf = ' '.join(eval(line[line.find(':')+1:])).replace(' ','')
            analyses[input_wf] = []
        if "BEST HYP:" in line:
            read = 1
            continue
        if read: 
            if line == '' or 'PRED AVG SCORE' in line:
                break
            ll, output = line.split('] [')
            ll = eval(ll + ']')[0]
            output = ' '.join(eval('[' + output))
            analyses[input_wf].append((exp(ll),get_analysis(output)))
    return read

def prune(analyses,th,maxnum):
    for wf in analyses:
        pruned_analyses = []
        cumul = 0
        for i, prob_a in enumerate(analyses[wf]):
            prob, a = prob_a
            if i >= maxnum:
                continue
            if cumul > th:
                break
            cumul += prob
            pruned_analyses.append(a)
        analyses[wf] = pruned_analyses

if __name__=='__main__':
    th = float(argv[1])
    maxnum = int(argv[2])
    analyses = {}
    while  read_analysis_set(stdin,analyses):
        pass
    prune(analyses,th,maxnum)
    testfile = open(argv[3])
    for line in testfile:
        line = line.strip('\n')
        if line:
            lan, wf, _, _, _ = line.split('\t')
            for a in analyses[wf]:
                print('\t'.join([lan,wf] + list(a)))
