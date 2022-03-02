"""==============================================================================
DATE BACTRIM ( SULFAMETHOXAZOLE/TRIMETHOPRIM ) FOR IV USE IN DEXTROSE 5% WATER
=============================================================================="""


def main():
   drug = int(input("VOLUME OF STOCK SMZ/TMP (ML): "))
   bag  = int(input("VOLUME OF IVPB D5W BAG  (ML): "))

   tmp = drug * 16
   total_vol = drug + bag
   conc = round(tmp / total_vol, 2)

   return str(conc) + "mg TMP/mL"


if __name__ == '__main__':
   main()