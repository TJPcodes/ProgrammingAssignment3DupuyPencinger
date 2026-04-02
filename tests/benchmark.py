# times hvlcs.py on each test file, use output to make the Q1 graph
import subprocess
import time
import glob
import os

test_files = sorted(glob.glob('data/test_*.in'))

print(f"{'file':<30} {'n':<12} {'time (s)':<10}")
print('-' * 52)

for fpath in test_files:
    with open(fpath) as f:
        lines = f.readlines()
    n = len(lines[-2].strip())

    start = time.perf_counter()
    subprocess.run(['python', 'src/hvlcs.py'], stdin=open(fpath), capture_output=True)
    elapsed = time.perf_counter() - start

    print(f"{os.path.basename(fpath):<30} {n:<12} {elapsed:.4f}")
