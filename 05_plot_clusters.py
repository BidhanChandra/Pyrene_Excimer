#!/usr/bin/env python3
"""
05_plot_clusters.py
Visualize clusters in reduced 2D or 3D space.
"""

import argparse
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def main(reduced_file, cluster_file, output):
    reduced = np.load(reduced_file)["reduced"]
    labels = np.load(cluster_file)["labels"]
    n_dim = reduced.shape[1]

    fig = plt.figure(figsize=(6, 5))
    if n_dim == 3:
        ax = fig.add_subplot(111, projection="3d")
        p = ax.scatter(reduced[:, 0], reduced[:, 1], reduced[:, 2], c=labels, cmap="tab10", s=25)
    else:
        plt.scatter(reduced[:, 0], reduced[:, 1], c=labels, cmap="tab10", s=20)
        plt.xlabel("Component 1")
        plt.ylabel("Component 2")

    plt.title("Clustered Excimer Conformers")
    plt.colorbar(p, label="Cluster ID") if n_dim == 3 else plt.colorbar(label="Cluster ID")
    plt.tight_layout()
    plt.savefig(output, dpi=300)
    plt.close()
    print(f"Cluster plot saved to {output}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Plot clustered reduced data.")
    parser.add_argument("--reduced_file", required=True, help="Reduced data NPZ file.")
    parser.add_argument("--cluster_file", required=True, help="Cluster labels NPZ file.")
    parser.add_argument("--output", default="figures/cluster_plot.png")
    args = parser.parse_args()
    main(args.reduced_file, args.cluster_file, args.output)
