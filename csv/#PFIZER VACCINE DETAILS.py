#PFIZER VACCINE DETAILS

#DATA
d = [["Length of NT Seq.", 4284],
["Mass of ADP",427.20]
]

Length_of_NT_Sequence = 4284
      #<src> World Health Organization (WHO) (September 2020). "Messenger RNA encoding the full-length SARS-CoV-2 spike glycoprotein" (DOC). WHO MedNet. Archived from the original on 5 January 2021. Retrieved 6 January 2022.

Mass_of_ADP = 427.20 #Daltons

Mass_of_single_mRNA = Length_of_NT_Sequence * Mass_of_ADP
      # 1830124.8 Daltons

#Conversion Factor
Dalton_to_Microgram = 1.661 * 10 ** -18

Adolescent_Dose_Pfizer_mcg = 10 # µg
Adolescent_Dose_Pfizer_da = Adolescent_Dose_Pfizer_mcg / Dalton_to_Microgram
Adolescent_Dose_Pfizer_da # = 6.020469596628536e+18


no_rnaCopies_Pfr_KidDose = Adolescent_Dose_Pfizer_da / Mass_of_single_mRNA
no_rnaCopies_Pfr_KidDose # = 3,289,649,753,190.895



d_display = ""
for x in d:
      d_display = d_display + str(x[0]) + "\n    :" + str(x[1]) + "\n\n"
print(d_display)