ONMTPREPROCESS=~/OpenNMT-py/preprocess.py

datasets:onmt-data/roa-track1-src-train.txt onmt-data/trk-track1-src-train.txt \
onmt-data/roa-track1.train.1.pt onmt-data/roa-track2.train.1.pt \
onmt-data/trk-track1.train.1.pt onmt-data/trk-track2.train.1.pt

onmt-data/%-track1-src-train.txt: train/%-uncovered
	python3 scripts/generate_onmt_data.py $* 1
	python3 scripts/generate_onmt_data.py $* 2

onmt-data/%.train.1.pt: onmt-data/%-src-train.txt
	python3 $(ONMTPREPROCESS) -train_src $< -train_tgt onmt-data/$*-tgt-train.txt \
                                  -valid_src onmt-data/$*-src-dev.txt -valid_tgt onmt-data/$*-tgt-dev.txt \
                                  -save_data onmt-data/$*
trainmodels:
	sbatch baseline/train-roa-track1.sh
	sbatch baseline/train-roa-track2.sh
	sbatch baseline/train-trk-track1.sh
	sbatch baseline/train-trk-track2.sh

testmodels:
	sbatch baseline/test-roa-track1.sh
	sbatch baseline/test-roa-track2.sh
	sbatch baseline/test-trk-track1.sh
	sbatch baseline/test-trk-track2.sh

testresults:results/roa-track1-dev-covered.sys results/roa-track2-dev-covered.sys \
results/trk-track1-dev-covered.sys results/trk-track2-dev-covered.sys

results/roa-track%-dev-covered.sys: onmt-data/roa-track%-src-dev.txt.nbest.out
	cat $^ | python3 scripts/get-analyses.py 0.6 2 dev/roa-covered > $@

results/trk-track%-dev-covered.sys: onmt-data/trk-track%-src-dev.txt.nbest.out
	cat $^ | python3 scripts/get-analyses.py 0.1 1 dev/trk-covered > $@

