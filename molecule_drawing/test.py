#!/Users/meganlim/anaconda_ete/envs/rdkit/bin/python

from rdkit import Chem
from rdkit.Chem import rdDistGeom
from rdkit.Chem import AllChem
from rdkit.Chem import rdMolAlign
from rdkit.Chem import Descriptors
from rdkit.Chem import Crippen
from rdkit.Chem import MolSurf
from rdkit.Chem.Draw import SimilarityMaps

smile = 'CC(=O)O'
mol = Chem.MolFromSmiles(smile)
