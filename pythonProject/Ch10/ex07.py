from typing import TextIO
from io import StringIO
import pprint

def read_molecule(reader):
    while True:
        # If there isn't another line, we're at the end of the file.
        line = reader.readline()
        if not line:
            return None

        if line.startswith('COMPND'):
            # Name of the molecule: "COMPND name"
            key, name = line.split()

            # Other lines are either "END" or "ATOM num atom_type x y z"
            molecule = [name]
            break
        # else:
        #     molecule = None

    reading = True
    while reading:
        line = reader.readline()
        if line.startswith('END'):
            reading = False
        elif not (line.startswith('CMNT') or line.isspace()):
            key, num, atom_type, x, y, z = line.split()
            if molecule == None:
                molecule = []
            molecule.append([atom_type, x, y, z])
    return molecule


def read_all_molecules(reader: TextIO) -> list:
    # The list of molecule information.
    result = []
    reading = True
    while reading:
        molecule = read_molecule(reader)
        if molecule:  # None is treated as False in an if statement
            result.append(molecule)
        else:
            reading = False
    return result


if __name__ == '__main__':
    molecule_file = open('multimol_withCMNT.pdb', 'r')
    molecules = read_all_molecules(molecule_file)
    molecule_file.close()
    pprint.pprint(molecules)