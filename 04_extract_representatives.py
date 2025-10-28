#!/usr/bin/env python3
"""
04_extract_representatives.py
Extract representative geometries from each cluster.
"""

import argparse
from pathlib import Path
import numpy as np
from ase.io import read, write

def main(geom_dir, cluster_file, output_dir):
    Path(output_dir).mkdir(exist_ok=True)
    xyz_files = sorted(Path(geom_dir).glob("*.xyz"))
    labels = np.load(cluster_file)["labels"]

    unique_labels = np.unique(labels)
    for lab in unique_labels:
        if lab == -1:
            continue  # skip noise
        idx = np.where(labels == lab)[0][0]
        atoms = read(xyz_files[idx])
        out_path = Path(output_dir) / f"cluster_{lab:02d}.xyz"
        write(out_path, atoms)
        print(f"Representative for cluster {lab} saved to {out_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract representative structures from clusters.")
    parser.add_argument("--geom_dir", required=True, help="Directory with XYZ geometries.")
    parser.add_argument("--cluster_file", required=True, help="NPZ file with cluster labels.")
    parser.add_argument("--output_dir", default="data/representatives")
    args = parser.parse_args()
    main(args.geom_dir, args.cluster_file, args.output_dir)
