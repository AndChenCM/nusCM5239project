# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 15:45:33 2022

@author: Chen Mingan

Credit to: https://drzinph.com/rdkit_2d-descriptors-in-python-part-4/
"""

import pandas as pd
from rdkit import Chem
from rdkit.Chem import Descriptors
from rdkit.ML.Descriptors import MoleculeDescriptors

class RDKit_2D:
    def __init__(self, smiles):
        self.mols = [Chem.MolFromSmiles(i) for i in smiles]
        self.smiles = smiles
        
    def compute_2Drdkit(self, name):
        rdkit_2d_desc = []
        calc = MoleculeDescriptors.MolecularDescriptorCalculator([x[0] for x in Descriptors._descList])
        header = calc.GetDescriptorNames()
        for i in range(len(self.mols)):
            ds = calc.CalcDescriptors(self.mols[i])
            rdkit_2d_desc.append(ds)
        df = pd.DataFrame(rdkit_2d_desc,columns=header)
        df.insert(loc=0, column='smiles', value=self.smiles)
        df.to_csv(name[:-4]+'_RDKit_2D.csv', index=False)

def main():
    filename = 'smiles1.csv'  # path to your csv file
    df = pd.read_csv(filename, encoding='cp1252')  # read the csv file as pandas data frame
    smiles = [i for i in df['smiles'].values]  

    ## Compute RDKit_2D Fingerprints and export a csv file.
    RDKit_descriptor = RDKit_2D(smiles)        # create your RDKit_2D object and provide smiles
    RDKit_descriptor.compute_2Drdkit(filename) # compute RDKit_2D and provide the name of your desired output file. you can use the same name as the input file because the RDKit_2D class will ensure to add "_RDKit_2D.csv" as part of the output file.

if __name__ == '__main__':
    main()
    











