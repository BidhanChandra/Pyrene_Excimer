#!/usr/bin/env python3
"""
02_reduce_dimension.py
Perform Kernel PCA or UMAP dimensionality reduction on SOAP features.
"""

import argparse
import numpy as np
from sklearn.decomposition import KernelPCA
import umap.umap_ as umap

def main(input_file, method, output):
    data = np.load(input_file)["features"]
    if method.lower() == "kpca":
        reducer = KernelPCA(n_components=3, kernel="rbf", gamma=0.01)
    elif method.lower() == "umap":
        reducer = umap.UMAP(n_neighbors=15, n_components=3, random_state=0)
    else:
        raise ValueError("method must be 'kpca' or 'umap'")
    reduced = reducer.fit_transform(data)
    np.savez_compressed(output, reduced=reduced)
    print(f"Reduced data ({method}) saved to {output}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Reduce dimensionality of SOAP features.")
    parser.add_argument("--input", required=True, help="Input NPZ with SOAP features.")
    parser.add_argument("--method", choices=["kpca", "umap"], default="kpca")
    parser.add_argument("--output", default="data/reduced_features.npz")
    args = parser.parse_args()
    main(args.input, args.method, args.output)
