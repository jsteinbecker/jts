
def reverseSequence (seq: str):
   revs = seq[::-1]
   return revs



l_ = 'acgt'
l = [l_] * 3
x = [ i+j+k for i, j, k in l_]
def main():
   rev= reverseSequence ('actggtca')
   return rev
