ONMTPREPROCESS=~/OpenNMT-py/preprocess.py

datasets:onmt-data/rom-track1-src-train.txt onmt-data/tur-track1-src-train.txt \
onmt-data/rom-track1.train.1.pt onmt-data/rom-track2.train.1.pt \
onmt-data/tur-track1.train.1.pt onmt-data/tur-track2.train.1.pt

onmt-data/%-track1-src-train.txt: train/%-uncovered
	python3 scripts/generate_onmt_data.py $* 1
	python3 scripts/generate_onmt_data.py $* 2

onmt-data/%.train.1.pt: onmt-data/%-src-train.txt
	python3 $(ONMTPREPROCESS) -train_src $< -train_tgt onmt-data/$*-tgt-train.txt \
                                  -valid_src onmt-data/$*-src-dev.txt -valid_tgt onmt-data/$*-tgt-dev.txt \
                                  -save_data onmt-data/$*
trainmodels:
	sbatch baseline/train-rom-track1.sh
	sbatch baseline/train-rom-track2.sh
	sbatch baseline/train-tur-track1.sh
	sbatch baseline/train-tur-track2.sh

testmodels:
	sbatch baseline/test-rom-track1.sh
	sbatch baseline/test-rom-track2.sh
	sbatch baseline/test-tur-track1.sh
	sbatch baseline/test-tur-track2.sh

testresults:results/rom-track1-dev-covered.sys results/rom-track2-dev-covered.sys \
results/tur-track1-dev-covered.sys results/tur-track2-dev-covered.sys

results/rom-track%-dev-covered.sys: onmt-data/rom-track%-src-dev.txt.nbest.out
	cat $^ | python3 scripts/get-analyses.py 0.6 2 dev/rom-covered > $@

results/tur-track%-dev-covered.sys: onmt-data/tur-track%-src-dev.txt.nbest.out
	cat $^ | python3 scripts/get-analyses.py 0.1 1 dev/tur-covered > $@

