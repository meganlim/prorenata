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


<html>
  <head>
    <link rel="stylesheet" href="https://pyscript.net/alpha/pyscript.css" />
    <script defer src="https://pyscript.net/alpha/pyscript.js"></script>
  </head>
  <body>
      <py-env>
      - rdkit
      </py-env>
    <py-script>

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
      print('hello world')

    </py-script>

    <!-- <py-script src="cardio/test.py"></py-script> -->
  </body>
</html>
