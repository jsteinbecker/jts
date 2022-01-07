def findHighlight (filestr):
      file = open(filestr,"r")

      r = file.read()
      x = re.findall("\=\(.*\)\=",r)
      return x