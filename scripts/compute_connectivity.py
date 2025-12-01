#!/usr/bin/env python3
"""
Small CLI wrapper to compute Fisher-Z connectomes from timeseries .npy files.
"""
import os, glob, numpy as np
from scripts.utils_io import save_conn_npz

def compute_z(ts):
    C = np.corrcoef(ts.T)
    np.fill_diagonal(C, 1.0)
    C = np.clip(C, -0.999999, 0.999999)
    return np.arctanh(C)

def main(ts_dir='timeseries', out_dir='connectivity'):
    os.makedirs(out_dir, exist_ok=True)
    ts_files = sorted(glob.glob(os.path.join(ts_dir, '*_ts.npy')))
    for f in ts_files:
        subj = os.path.basename(f).replace('_ts.npy','')
        ts = np.load(f).astype(np.float32)
        Z = compute_z(ts)
        save_conn_npz(Z, subj, outdir=out_dir)
        print('Saved', subj)

if __name__ == '__main__':
    main()
