import yaml
import random as rnd
from yaml import load, dump, Loader, Dumper

data = """
Crucial Mutation for Murine Suceptibility, SARS2[S] : N501
Base-Length of SARS2 Genome : 29000
Baltimore Class III : +ssRNA
"""

yml_dict = yaml.load(data, Loader=Loader)

question_list = list(yml_dict)
answer_list   = list(yml_dict.values())

def askQ ():
    maxval = len(question_list) -1
    r = rnd.randint(0, maxval)
    print("-"*50)
    print("Question:",question_list[r])
    input("Enter to reveal")
    print("Answer:",answer_list[r])
    print("-"*50)
    askQ()


if __name__ == "__main__":
    askQ()