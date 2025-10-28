# Pyrene Excimer Dynamics: Unsupervised Machine Learning Analysis of Excited-State Trajectories

## 📘 Overview
This repository contains the data processing and analysis workflow used in the study:

> **“Conformational Dynamics of the Pyrene Excimer”**  
> *Phys. Chem. Chem. Phys.*, 2024.  
> DOI: [10.1039/d4cp03947e](https://doi.org/10.1039/d4cp03947e)

The project investigates how conformational diversity in the pyrene dimer governs its excimer fluorescence.  
By combining **TDDFT-based excited-state optimization** with **unsupervised machine learning**, we reveal distinct structural motifs that dominate the emission process.

---

## 🧠 Scientific Summary
The pyrene excimer exhibits broad, red-shifted fluorescence due to the coexistence of multiple metastable conformations on the excited-state potential energy surface (PES).  
Using **surface-hopping dynamics** and **SOAP-based molecular representations**, we identify and characterize these conformers without prior structural assumptions.

### Key Steps
1. **Geometry Generation**
   - Performed excited state optimization at the TD-CAMB3LYP/def2-SVP level.

2. **Feature Extraction**
   - Converted atomic coordinates into **SOAP descriptors** using the `DScribe` library.
   - Standardized feature vectors.

3. **Dimensionality Reduction**
   - Applied **Kernel PCA** (RBF kernel) to map high-dimensional SOAP space into low-dimensional manifolds.
   - This representation preserves the geometric relationships between conformers.

4. **Clustering and Classification**
   - **k-means** to identify metastable states.
   - Cluster labels correspond to distinct excimer geometries (parallel, twisted, slipped, stacked-twisted).

5. **Visualization**
   - 2D and 3D scatter plots reveal clear clustering patterns.
   - Representative structures extracted per cluster for structural and energetic analysis.

---



