import yaml
from yaml import load, dump, Loader, Dumper
doc = """
name: 'Josh'
  pos: 'Sr Acute Care Pharmacy Technician II'
  twc: 3.8 years

certs: 
  - CPhT
  - PhAT-CO
  - Chemo

"""
d = """
invoice: 34843
date   : 2001-01-23
bill-to: &id001
    given  : Chris
    family : Dumars
    address:
        lines: |
            458 Walkman Dr.
            Suite #292
        city    : Royal Oak
        state   : MI
        postal  : 48046
ship-to: *id001
product:
    - sku         : BL394D
      quantity    : 4
      description : Basketball
      price       : 450.00
    - sku         : BL4438H
      quantity    : 1
      description : Super Hoop
      price       : 2392.00
tax  : 251.42
total: 4443.52
comments:
    Late afternoon is best.
    Backup contact is Nancy
    Billsmer @ 338-4338.
"""


y = yaml.load(d,Loader=Loader)
print(yaml.dump(y['tax'],Dumper=Dumper) )
y['comments']

