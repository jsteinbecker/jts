import re
import pandas as pd

text = "Symphony No. 8 -CT @Beethoven -m 1"
text2= "Symphony No. 5 -m 1 -VN @Beethoven"

class entry :

    def __init__ (self,inp:str):
        def movement (inp:str):
            re_movement = "(?<=-m ).*?(?= -|$)"
            result = re.findall(re_movement, inp)[0]
            return result
        def instrument (inp:str):
            instruments = {"-CT" : "Clarinet",
                        "-VN" : "Violin",
                        "-BC" : "Bass Clarinet",
                        "-CO" : "Cello",
                        "-OB" : "Oboe"}
            re_inst = '-\w{2}'

            result_i = str(re.findall(re_inst,inp)[0])
            result = instruments[result_i]
            return result
        def piece (inp:str):
            re_piece = '^.*?(?= -|$)'
            result = re.findall(re_piece, inp)[0]
            return result
        def composer (inp:str):
            re_composer = '(?<=@).*?(?= -|$)'
            result = re.findall(re_composer, inp)[0]
            return result
        self.m = movement(inp)
        self.i = instrument(inp)
        self.p = piece(inp)
        self.c = composer(inp)
        self.values = [self.c, self.p, self.m, self.i]

class log :
    def __init__(self):
        self.df = pd.DataFrame(columns=["cmpr","work","mvmt","inst"])

