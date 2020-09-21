# Modification process

## Adding Papers into the repository

The README in the main folder is generated automatically with ```bibtex_to_md.py``` script and the bibtex file as database.

Therefore to add entries in the README, it is necessary to modify bibtex.bib and run:

```python
python scripts/bibtex_to_md.py
```
from the main folder with python 3.6.


## Improve a bib entry

The bib entry does not always contain natively all information necessary to generate the md file perfectly, it might be necessary to edit it manually to improve it (it does not affect the citation process if the bib entry is used as a reference in a scientific paper).

Here if we have a paper:

```
inproceedings{Doe20XXcontinual,
  title={Continual Lifelong Never Ending Learning in Open-Ended incremental environment},
  author={John Doe},
  booktitle={Internation Conference on Continual Learning and Lifelong Agent (ICCLLA)},
  year={20XX}
}
```

It can be manually edited to add an URL and some keywords that might help for automatic classification.

```
@inproceedings{Doe20XXcontinual,
  title={Continual Lifelong Never Ending Learning in Open-Ended incremental environment},
  author={John Doe},
  booktitle={Internation Conference on Continual Learning and Lifelong Agent (ICCLLA)},
  year={20XX},
  url={https://arxiv.org/abs/XXXX.XXXX},
  keywords={Rehearsal, Regularization}
}
```

The current list of keywords used is:
```python
["Classic","Survey","Influential","Regularization","Distillation","Rehearsal","Generative Replay","Dynamic Architecture","Hybrid","Meta-Continual Learning", "Continual-Meta Learning", "Reinforcement", "Generative Modeling","Applications"]
```


## Add a comment to a paper

To add a comment associated with a paper, you can create a @String line with the paper ID. For example, to add a comment to the paper Doe20XXcontinual you can add after the entry:

```
@String(Doe20XXcontinual="This paper introduce different strategies to learn continually in various environment")
```

NB: To keep the bibtex easy to use, we keep the entry and the string line close to each others

```
@inproceedings{Doe20XXcontinual,
  title={Continual Lifelong Never Ending Learning in Open-Ended incremental environment},
  author={John Doe},
  booktitle={Internation Conference on Continual Learning and Lifelong Agent (ICCLLA)},
  year={20XX},
  url={https://arxiv.org/abs/XXXX.XXXX},
  keywords={Rehearsal, Regularization}
}

@String(Doe20XXcontinual="This paper introduce different strategies to learn continually in various environment")
```
