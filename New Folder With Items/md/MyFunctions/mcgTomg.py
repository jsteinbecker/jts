# Function Converts Micrograms to Milligrams
def mcg_to_mg (mcg):
      ug = mcg
      mg = ug / 1000
      out = str(mg) + " mg (" + str(ug)+ " µg)"
      return out

# mcg_to_mg(6000)
