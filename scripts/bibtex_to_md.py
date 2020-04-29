

from utils import generate_md_file
import bibtexparser

file_name = 'bibtex.bib'
with open(file_name) as bibtex_file:
    bibtex_str = bibtex_file.read()

bib_db = bibtexparser.loads(bibtex_str)

################################### Create Readme ####################################
def plot_titles(titles):
    return '\n' + "## " + titles[0] + '\n'

list_types = [["Classics", "Classic"],
               ["Surveys", "Survey", "survey"],
               ["Influentials", "Influential"],
               ["Regularization Methods", "Regularization"],
               ["Distillation Methods", "Distillation"],
               ["Rehearsal Methods", "Rehearsal"],
               ["Generative Replay Methods", "Generative Replay"],
               ["Dynamic Architectures or Routing Methods", "Architectures", "Dynamic Architecture"],
               ["Hybrid Methods", "Hybrid"],
               ["Meta-Continual Learning"],
               ["Continual-Meta Learning"],
               ["Lifelong Reinforcement Learning", "Reinforcement"],
               ["Continual Generative Modeling", "Generative Modeling"]]

generate_md_file(DB=bib_db, list_classif=list_types, key="keywords", plot_title_fct=plot_titles, filename= "Auto_README.md", add_comments=True)


