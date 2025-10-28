#!/usr/bin/env python3
"""
01_generate_soap.py
Compute SOAP descriptors for all geometries in the input directory.
"""

import argparse
from pathlib import Path
import numpy as np
from ase.io import read
from dscribe.descriptors import SOAP

def main(input_dir, output):
    xyz_files = sorted(Path(input_dir).glob("*.xyz"))
    if not xyz_files:
        raise FileNotFoundError(f"No XYZ files found in {input_dir}")

    # Example parameters — modify as needed
    soap = SOAP(
        species=["C", "H"],
        periodic=False,
        rcut=6.0,
        nmax=8,
        lmax=6,
        sigma=0.3,
        sparse=False,
    )

    all_features = []
    for f in xyz_files:
        atoms = read(f)
        desc = soap.create(atoms)
        all_features.append(desc.flatten())
    np.savez_compressed(output, features=np.array(all_features))
    print(f"SOAP features saved to {output}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate SOAP descriptors from XYZ files.")
    parser.add_argument("--input_dir", required=True, help="Directory with XYZ geometries.")
    parser.add_argument("--output", default="data/soap_features.npz", help="Output file.")
    args = parser.parse_args()
    main(args.input_dir, args.output)
