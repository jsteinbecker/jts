x='gcactagctttgataggggcgggcgtg'

def ntCenter(seq,nts,displaytype = True):
    """FUNCTION WILL RETURN AN ARRAY WITH VALUES:
    
         - NUCLEOTIDE, 
         - AVERAGE POSITION IN CHAIN, AND 
         - % DISTANCE TO THE TRUE CENTER
    """
    centers = []

    for nt in nts:
        ind = []
        
        for i in range(len(seq)):
            if seq[i] == nt:
                ind.append(i)

        center = sum(ind)/len(ind)
        center = int(center)

        dist = round(((0.5 * len(seq)) - center) / len(seq),2)
        centers.append([nt,center,dist])

    if displaytype == True:
        out = ""
        for x in centers:

            print(f'{x[0]}: Center= {x[1]}, {int(x[2]*100)}% from true center')
            
    if displaytype == False:

        return centers

if __name__ == "__main__":
    ntCenter(x,'acgt')