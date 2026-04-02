# generates 10 random test input files for Q1
import random
import os

ALPHABET = list('abcdefghij')

SIZES = [25, 50, 100, 200, 400, 600, 800, 1000, 1500, 2000]

os.makedirs('data', exist_ok=True)

for i, n in enumerate(SIZES):
    values = {c: random.randint(1, 10) for c in ALPHABET}
    A = ''.join(random.choices(ALPHABET, k=n))
    B = ''.join(random.choices(ALPHABET, k=n))

    fname = f'data/test_{i+1:02d}_n{n}.in'
    with open(fname, 'w') as f:
        f.write(f'{len(ALPHABET)}\n')
        for c, v in values.items():
            f.write(f'{c} {v}\n')
        f.write(A + '\n')
        f.write(B + '\n')
    print(f'generated {fname}')
