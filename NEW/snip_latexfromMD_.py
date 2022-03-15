
def extract_md_quotes (file_path):
   """
   -----------------------
   |  EXTRACT MARKDOWN QUOTES      
   -----------------------
'```quote
|   This will get extracted
|   into a single list item.
|```
   -----------------------
   """
   import re

   file_ = open (file_path , "r")
   data = file_.read()

   re_pattern = \
   "(?<=```quote\n).*\n*.*\n*.*(?=\n*```)"
   
   quotes = re.findall (re_pattern , data)

   print (str(len(quotes)) + \
      " quotes extracted")
   for quote in quotes:
      print(quote)
      
   return quotes
   
# Runnng code ---
\
   extract_md_quotes("/Users/joshsteinbecker/\
   jts_project/CovidCVRisks.md")




def extract_md_latex (file_path):

   """
   -----------------------
   |  EXTRACT MARKDOWN LATEX      
   -----------------------
   Output >>> List of Latex Lines
   """
   import re

   file_ = open (file_path , "r")
   data = file_.read()

   re_pattern = "\$\$.*\$\$?"
   snipper = re.findall (re_pattern,  data)
   file_.close()

   print (str(len(snipper)) + " quotes extracted:")
   for snip in snipper:
      print (snip)
   return snipper


