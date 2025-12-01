import os, json, hashlib, numpy as np

def md5_of_file(path, block_size=2**20):
    h = hashlib.md5()
    with open(path,'rb') as f:
        for block in iter(lambda: f.read(block_size), b''):
            h.update(block)
    return h.hexdigest()

def save_conn_npz(mat, subj, ses='ses-1', atlas='schaefer200', outdir='connectivity'):
    os.makedirs(outdir, exist_ok=True)
    base = f"{subj}_{ses}_task-rest_atlas-{atlas}_conn_z"
    npz_path = os.path.join(outdir, base + ".npz")
    np.savez_compressed(npz_path, conn=mat.astype(np.float32))
    meta = {"file": npz_path, "subj": subj, "session": ses, "atlas": atlas, "shape": mat.shape, "dtype": str(mat.dtype)}
    meta['md5'] = md5_of_file(npz_path)
    with open(npz_path.replace('.npz','.json'),'w') as f:
        json.dump(meta, f, indent=2)
    return npz_path, meta

def load_conn_npz(npz_path):
    return np.load(npz_path)['conn']
