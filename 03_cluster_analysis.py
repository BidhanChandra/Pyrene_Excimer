#!/usr/bin/env python3
"""
03_cluster_analysis.py
Cluster reduced SOAP data using KMeans or DBSCAN.
"""

import argparse
import numpy as np
from sklearn.cluster import KMeans, DBSCAN
from sklearn.metrics import silhouette_score

def main(input_file, method, n_clusters, output):
    X = np.load(input_file)["reduced"]
    if method.lower() == "kmeans":
        model = KMeans(n_clusters=n_clusters, random_state=0)
    elif method.lower() == "dbscan":
        model = DBSCAN(eps=0.8, min_samples=5)
    else:
        raise ValueError("method must be 'kmeans' or 'dbscan'")

    labels = model.fit_predict(X)
    np.savez_compressed(output, labels=labels)

    if len(set(labels)) > 1 and -1 not in labels:
        sil = silhouette_score(X, labels)
        print(f"Silhouette score = {sil:.3f}")
    print(f"Cluster labels saved to {output}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Cluster reduced SOAP data.")
    parser.add_argument("--input", required=True, help="Input NPZ file with reduced data.")
    parser.add_argument("--method", choices=["kmeans", "dbscan"], default="kmeans")
    parser.add_argument("--n_clusters", type=int, default=9)
    parser.add_argument("--output", default="data/cluster_labels.npz")
    args = parser.parse_args()
    main(args.input, args.method, args.n_clusters, args.output)
