"""
#############
GENERATOR: 
AVALIABLE DOSES FOR INTRAVENOUS VANCOMYCIN
#############
"""

def main(): 
   doses = [x for x in range(500, 2001, 250)]
   print(doses)
   return doses



if __name__ == '__main__':
   main()