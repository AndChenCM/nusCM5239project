# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 15:00:35 2022

@author: e0732571
"""

# convert sdf to smiles

from rdkit import Chem
from rdkit.Chem.ChemUtils import SDFToCSV
f = open( 'out.csv', 'w' )
suppl = Chem.SDMolSupplier( 'Structures.sdf' )
SDFToCSV.Convert( suppl, f )
f.close()











