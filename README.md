# Shared Task on Cross-Lingual Morphological Analysis

__The test input forms have now been released!__ Check the directory `test`.

We introduce the task of cross-lingual morphological analysis. Given a word in an unknown related language, for example "navifraghju" ("shipwreck" in Corsican), a human speaker of several related languages is able to deduce that it is a noun in the singular by making deductions from similar words, for example: "naufragi" (Catalan), "naufragio" (Spanish, Italian), "naufrágio" (Portuguese) and "naufrage" (French). In this task we invite participants to create computational models which will be able to do the same. Two language families are represented, Romance (fusional morphology) and Turkic (agglutinative morphology). 

## Tracks

We present two tracks: a closed track (1) and a semi-closed one (2).

**Track 1** Competitors get annotated data from related languages and learn
a model which can analyse unseen target language forms. In addition,
competitors are allowed to use the input forms in the test set when training their system.

**Track 2** Competitors get annotated data from related languages as well as an unannotated plain text corpus in the target language. They learn
a model which can analyse unseen target language forms. In addition,
competitors are allowed to use the input forms in the test set when training their system.

We encourage participants to provide thorough error analysis.

## Timeline

* Training set release: February 5, 2019
* Test set release: March 5, 2019
* Submissions due: ~~March 8, 2019~~ __EXTENSION: March 13, 2019 (23:59 UTC-12)__
* Results announced: ~~March 12, 2019~~ March 17, 2019 

On February 5, we release training sets for the Romance languages (Catalan, French, Italian, Portuguese, Spanish) and the Turkic languages (Bashkir, Kazakh, Kyrgyz, Tatar, Turkish). We also release development sets for the Romance language Asturian and the Turkic language Crimean Tatar. In addition, we release unannotated corpora for Asturian and Crimean Tatar.

On March 5, we release additional test sets for two surprise languages. Additionally, we release unannotated corpora for both of the surprise languages. Competitors then train systems on the related language training sets for track 1 and the related language training set and unannotated data for track 2. They then submit their test set predictions. We will be evaluating system performance on the surprise language test sets.   

__The test input forms have now been released!__ Check the directory `test`.

Unannotated data for the test languages is available [here](http://ilazki.thinkgeek.co.uk/~spectre/wikipedia-data-test.tar.bz2).

## Submission 

Please, name your tagged test sets in the following way: `roa-uncovered.N.TEAM` and `trk-uncovered.N.TEAM`. Here `N`is the track number and `TEAM` is your team name. Send your output files to vardial2019cma 'at' gmail 'dot' com at the latest March 8, 23:59 UTC-12. Please, indicate your name and team name in the email message.

## Data Formats

### Uncovered data

We provide fully annotated _uncovered_ training and development sets for the
target language and related languages. Below, you can see an example
of the data format from `train/roa-uncovered`:

```
por    marido      marido      NOUN    Gender=Masc|Number=Sing
por    dependem    depender    VERB    Mood=Ind|Number=Plur|Person=3|Tense=Pres|VerbForm=Fin
cat    carener     carener     ADJ     Gender=Masc|Number=Sing
cat    carener     carener     NOUN    Gender=Masc|Number=Sing
spa    depender    depender    VERB    VerbForm=Inf
ast    adoptó      adoptar     VERB    Aspect=Perf|Mood=Ind|Number=Sing|Person=3|Tense=Past|VerbForm=Fin
ast    roques      roca        NOUN    Gender=Fem|Number=Plur
```

Each line consists of five TAB separated fields (language code, word
form, lemma, POS, morphological features). Since every word form can
correspond to multiple analyses, a word form like "carener" can occur
on several lines with different POS and morphological features.

### Covered data

We also provide _covered_ data sets which are used as input data for
the analysis system during development and testing. Here each word
form occurs exactly once and the lemma, POS and morphological features
fields are empty. This is an example from `dev/roa-uncovered`

```
ast	otomana      _    _    _
ast	franxes      _    _    _
ast	amosaben     _    _    _
ast	principiu    _    _    _
```

When your system fills in analyses, you should output one line for
each analysis (the order of the output lines will not affect the
evaluation script). For example, these are the corresponding lines
from the file `dev/roa-uncovered`

```
ast    otomana      otomán       ADJ     Gender=Fem|Number=Sing
ast    otomana      otomanu      NOUN    Gender=Fem|Number=Sing
ast    otomana      otomanu      ADJ     Gender=Fem|Number=Sing
ast    franxes      franxa       NOUN    Gender=Fem|Number=Plur
ast    amosaben     amosar       VERB    Aspect=Imp|Mood=Ind|Number=Plur|Person=3|Tense=Past|VerbForm=Fin
ast    principiu    principiu    NOUN    Gender=Masc|Number=Sing
```

### Raw text data

For track 2, there is raw text data (produced from Wikipedia dumps) available [here](http://cl.indiana.edu/~ftyers/shared-task/wikipedia-data.tar.bz2). You may use it to e.g. train embeddings, or for other purposes.

### Universal dependencies treebanks

#### Romance

* [UD_French-FTB](http://github.com/UniversalDependencies/UD_French-FTB)
* [UD_French-GSD](http://github.com/UniversalDependencies/UD_French-GSD)
* [UD_French-ParTUT](http://github.com/UniversalDependencies/UD_French-ParTUT)
* [UD_French-PUD](http://github.com/UniversalDependencies/UD_French-PUD)
* [UD_French-Sequoia](http://github.com/UniversalDependencies/UD_French-Sequoia)
* [UD_French-Spoken](http://github.com/UniversalDependencies/UD_French-Spoken)
* [UD_Italian-ISDT](http://github.com/UniversalDependencies/UD_Italian-ISDT)
* [UD_Italian-ParTUT](http://github.com/UniversalDependencies/UD_Italian-ParTUT)
* [UD_Italian-PoSTWITA](http://github.com/UniversalDependencies/UD_Italian-PoSTWITA)
* [UD_Italian-PUD](http://github.com/UniversalDependencies/UD_Italian-PUD)
* [UD_Italian-VIT](http://github.com/UniversalDependencies/UD_Italian-VIT)
* [UD_Portuguese-Bosque](http://github.com/UniversalDependencies/UD_Portuguese-Bosque)
* [UD_Portuguese-GSD](http://github.com/UniversalDependencies/UD_Portuguese-GSD)
* [UD_Portuguese-PUD](http://github.com/UniversalDependencies/UD_Portuguese-PUD)
* [UD_Spanish-AnCora](http://github.com/UniversalDependencies/UD_Spanish-AnCora)
* [UD_Spanish-GSD](http://github.com/UniversalDependencies/UD_Spanish-GSD)
* [UD_Spanish-PUD](http://github.com/UniversalDependencies/UD_Spanish-PUD)

#### Turkic

* [UD_Turkish-BOUN](http://github.com/UniversalDependencies/UD_Kazakh-KTB)
* [UD_Turkish-BOUN](http://github.com/UniversalDependencies/UD_Turkish-BOUN)
* [UD_Turkish-IMST](http://github.com/UniversalDependencies/UD_Turkish-IMST)
* [UD_Turkish-PUD](http://github.com/UniversalDependencies/UD_Turkish-PUD)


### Bilingual dictionaries

Bilingual dictionaries from the Apertium project that have been preprocessed into tabular format can be 
found under [supplementary data](supplementary-data/).

## Language codes

### Romance languages (`roa`)

| Code | Language      |
|------|---------------|
| ast  | Asturian      |
| cat  | Catalan       |
| fra  | French        |
| ita  | Italian       |
| por  | Portuguese    |
| spa  | Spanish       |
| ???  | Surprise Language |

### Turkic languages (`trk`)

| Code | Language      |
|------|---------------|
| bak  | Bashkir       |
| crh  | Crimean Tatar |
| kaz  | Kazakh        |
| kir  | Kyrgyz        |
| tat  | Tatar         |
| tur  | Turkish       | 
| ???  | Surprise Language |

## Baseline

### Baseline System

The baseline system formulates morphological analysis as a characterlevel string transduction task. It is implemented using [OpenNMT](http://opennmt.net/) and uses an LSTM
encoder-decoder model with attention for performing the
string transduction. The model is trained to translate input word forms like "así" (1st person singular past perfect of "asir" [to grab] or the adverb "así" [such] in Spanish) into output analyses:
```
así+ADV
asir+Aspect=Perf|Mood=Ind|Number=Sing|Person=1|Tense=Past|VerbForm=Fin
```
As the example demonstrates, the model needs to be able to generate multiple output analyses
given an input word form. This is accomplished by extracting several output candidates from the model using beam search and selecting the most probable candidates as
model outputs. 

The number of outputs from beam search is controlled by a probability threshold hyperparameter `p`. We extract the least number of top scoring candidates whose combined
probability mass is greater than `p`. Additionally, we restrict the maximal number of
output candidates using a single hyperparameter `N`. The hyperparamaters `p` and `N`
are tuned on the development data.

We use the same baseline model for both tracks 1 and 2. This means that the unannotated corpus data is not utilized in any way.

The baseline system is documented in:

```
@InProceedings{W19-0301,
  author = 	"Silfverberg, Miikka
		and Tyers, Francis",
  title = 	"Data-Driven Morphological Analysis for Uralic Languages",
  booktitle = 	"Proceedings of the Fifth International Workshop on Computational Linguistics for Uralic Languages",
  year = 	"2019",
  publisher = 	"Association for Computational Linguistics",
  pages = 	"1--14",
  location = 	"Tartu, Estonia",
  url = 	"http://aclweb.org/anthology/W19-0301"
}
```

### Running the Baseline System

The current baseline scripts are aimed for a system running [lmod](https://www.tacc.utexas.edu/research-development/tacc-projects/lmod) and [slurm](https://slurm.schedmd.com/). You will probably need to modify the scripts to suit your system.

To build datasets for OpenNMT, run: 
```
make datasets
```

To build baseline models, run:
```
make trainmodels
```
You need to wait until the models are trained. After that, you can test models, by running:
```
make testmodels
make testresults
```

Now you should have the output files for the Asturian and Crimean Tatar development data in the directory `results`:
```
results/roa-track1-dev-covered.sys
results/roa-track2-dev-covered.sys
results/trk-track1-dev-covered.sys
results/trk-track2-dev-covered.sys
```

### Baseline Results for Development Data

These are baseline results on the Asturian and Crimean Tatar development data. Since we use the same baseline system for tracks 1 and 2, the baseline F1-score is the same for both tracks. 

```
$ python3 scripts/eval_tabular.py results/roa-track1-dev-covered.sys dev/roa-uncovered 
Recall for analysis: 43.33
Precision for analysis: 42.57
F1-score for analysis: 42.94

Recall for lemma: 60.60
Precision for lemma: 55.91
F1-score for lemma: 58.16

Recall for tag: 59.50
Precision for tag: 60.13
F1-score for tag: 59.81

$ python3 scripts/eval_tabular.py results/trk-track1-dev-covered.sys dev/trk-uncovered 
Recall for analysis: 31.24
Precision for analysis: 38.44
F1-score for analysis: 34.47

Recall for lemma: 56.30
Precision for lemma: 59.06
F1-score for lemma: 57.65

Recall for tag: 38.52
Precision for tag: 47.35
F1-score for tag: 42.48
```
