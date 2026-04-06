import subprocess
import time
import glob
import matplotlib.pyplot as plt

test_files = sorted(glob.glob('data/test_*.in'))

ns = []
times = []

for fpath in test_files:
    with open(fpath) as f:
        lines = f.readlines()
    n = len(lines[-2].strip())

    start = time.perf_counter()
    subprocess.run(['python', 'src/hvlcs.py'], stdin=open(fpath), capture_output=True)
    elapsed = time.perf_counter() - start

    ns.append(n)
    times.append(elapsed)

plt.figure(figsize=(7, 4))
plt.plot(ns, times, marker='o', linewidth=1.5, markersize=5, color='steelblue')
plt.xlabel('n (string length)')
plt.ylabel('time (s)')
plt.title('HVLCS runtime vs input size')
plt.tight_layout()
plt.savefig('data/benchmark.png', dpi=120)
print('saved data/benchmark.png')
