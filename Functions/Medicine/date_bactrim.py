program_title = """
===============================================
DATE BACTRIM 
-----------------------------------------------
(SULFAMETHOXAZOLE/TRIMETHOPRIM) 
       - - - - - - - - -
FOR IV USE IN DEXTROSE 5% WATER
===============================================
"""


def date_bactrim(drugmL,bagmL):
   """\
   drugmL : ML of Bactim Solution
   bagmL  : ML of D5W Container for Dilution
   --------
   returns: (Conc, Rx, BUD)
   """
   drug = drugmL
   bag = bagmL

   tmp = drug * 16
   total_vol = drug + bag
   conc = round(tmp / total_vol, 2)

   return str(conc) + "mg TMP/mL"



single_line = "---------------------------------------------"
double_line = "============================================="



def main():
   print (program_title)
   drug = int(input("VOLUME OF STOCK SMZ/TMP (ML): "))
   bag  = int(input("VOLUME OF IVPB D5W BAG  (ML): "))
   answer = date_bactrim(drug,bag)
   print (single_line)
   print (answer)
   print (double_line)

if __name__ == '__main__':
   main()

  