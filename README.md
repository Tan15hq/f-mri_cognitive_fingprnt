# fMRI Fingerprint Project  
*A complete student-built pipeline for subject identification using resting-state fMRI connectivity and contrastive deep learning.*

---

## Overview
This project builds a full pipeline that goes from resting-state fMRI → ROI time series → functional connectomes → reliability analysis (ICC) → fingerprinting accuracy → Siamese contrastive embeddings.

The entire pipeline is reproducible in Google Colab and uses the Schaefer-200 atlas and publicly available resting-state fMRI from the ADHD-200 dataset.

---

## What the project does
### 1. Preprocessing and Timeseries Extraction
- Load 4D resting-state fMRI.
- Apply **Schaefer-200** atlas.
- Extract region-wise time series (T × 200).
- Save cleaned timeseries as `.npy`.

### 2. Connectivity Matrix Construction  
- Compute **Pearson correlation** between parcels.  
- Convert to **Fisher-Z** (more normal distribution).  
- Save connectomes as `.npz` with metadata + md5 hash.

### 3. Split-Half Reliability & Fingerprinting  
- Split each subject’s scan into **first half** and **second half**.  
- Compute two separate Fisher-Z connectomes.  
- Flatten upper-triangles → compute cosine similarity.  
- Identify if each subject's half-1 best matches their half-2.  
- Compute permutation test for significance.

### 4. ICC (Edge Reliability)  
- Compute **ICC(1,1)** for every edge across subjects.  
- Produce full ICC matrix, heatmap, and top-edge connectome visualization.  
- Generate **accuracy vs K** curve using top-K ICC edges.

### 5. Siamese Contrastive Learning (Deep Learning)  
- Train an **MLP-based Siamese encoder** using NT-Xent loss.  
- Positive pairs = same subject split-halves.  
- Negative pairs = in-batch negatives (different subjects).  
- Learn 64-dim embeddings that cluster same-subject scans.  
- Evaluate using **nearest-neighbor identification accuracy**.  
- Visualize embeddings using **PCA 2-D projection**.

---

## Repository Structure
```
fmri-fingerprint/
├── notebooks/
│   ├── 01_data_and_preprocessing.ipynb
│   ├── 02_connectivity_and_qc.ipynb
│   ├── 03_splithalf_and_icc.ipynb
│   ├── 04_fingerprint_and_accuracy.ipynb
│   └── 05_siamese_contrastive.ipynb
├── scripts/
├── results/
├── README.md
├── requirements.txt
├── DATA_USAGE.md
└── LICENSE
```

---

## How to Run (Google Colab)
1. Open any notebook in Colab.  
2. **Runtime → Change runtime type → GPU (for Siamese model).**  
3. Mount Drive:
```python
from google.colab import drive
drive.mount('/content/drive')
```
4. Set:
```python
WORKDIR = '/content/drive/MyDrive/fmri_fingerprint'
```
5. Run notebooks in this order:
   1. `01_data_and_preprocessing`  
   2. `02_connectivity_and_qc`  
   3. `03_splithalf_and_icc`  
   4. `04_fingerprint_and_accuracy`  
   5. `05_siamese_contrastive`

Results will be saved under:
```
/content/drive/MyDrive/fmri_fingerprint/results/
```

---

## Key Results (saved in `results/`)
These figures are included in the repository to demonstrate the full pipeline and model behavior.





### Split-Half Similarity Matrix
![Split Half Similarity](results/sim_heatmap.png)

### Diagonal Self-Similarity Sorted
![Diagonal Sorted](results/diag_sorted.png)

### ICC Heatmap
![ICC Heatmap](results/icc_heatmap.png)

### Top 500 ICC Connectome
![Top Edges](results/top_500_icc_connectome.png)

### Accuracy vs K (ICC-ranked edges)
![Accuracy vs K](results/accuracy_vs_K_plot.png)

### Siamese Embedding PCA View
![Siamese PCA](results/siamese_embeddings_pca2d.png)





### 1. Split-Half Similarity Matrix  
*Generated in:* **CELL H** (Notebook 03)  
**File:** `sim_heatmap.png`  
Shows diagonally strong within-subject similarity.

### 2. Diagonal Self-Similarity Sorted  
*Generated in:* **CELL H**  
**File:** `diag_sorted.png`  
Visualizes subjects with strongest fingerprint.

### 3. ICC Heatmap  
*Generated in:* **CELL 5** (Notebook 03)  
**File:** `icc_heatmap.png`  
Shows reliability of all edges across subjects.

### 4. Top-500 ICC Connectome  
*Generated in:* **CELL 5**  
**File:** `top_500_icc_connectome.png`  
Visualizes strongest reliable functional connections.

### 5. Accuracy vs Top-K ICC Edges  
*Generated in:* **CELL 7** (Notebook 04)  
**File:** `accuracy_vs_K_plot.png`  
Shows how identification accuracy grows with more reliable edges.

### 6. Siamese Embedding PCA Plot  
*Generated in:* **Final Siamese PCA cell** (Notebook 05)  
**File:** `siamese_embeddings_pca2d.png`  
Shows learned representation: each subject forms a pair cluster.

---

## Short Summary for Professors
**“The model learns a stable subject-specific neural fingerprint from resting-state fMRI.  
Using a Siamese contrastive encoder, the system identifies each individual's second-half scan from their first-half scan with high accuracy.”**

---

## Dataset & Ethics
- Uses de-identified public ADHD-200 (Preprocessed Connectomes Project).  
- No identifiable information stored; only derived features and plots included.

---

## Contact
If you have questions or want a walkthrough, feel free to reach out.  
"# f-mri_cognitive_fingprnt" 
