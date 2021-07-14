# %%
from pyquante2 import molecule,rhf,uhf,rohf,h2,h2o,lih,oh,co,ch4,he,basisset
import pandas as pd
import time

# %%
basissets = ['sto3g', 'sto-3g', '6-31g', '6-31g**', '6-31g(d,p)']
molecules = [h2, he, lih, oh, h2o, ch4, co]

# %%
# for molec in molecules: 
#     for basis in basissets: 
#         start = time.time()
#         bfs = basisset(molec, basis)
#         solver = rohf(molec, bfs) if molec == oh else rhf(molec, bfs)
#         ens = solver.converge()
#         print(f'{molec.stoich()} with {basis} basis set has energy: {ens[-1]} in {time.time() - start} sec')

# %%
energies = pd.DataFrame(
    index=[molec.stoich() for molec in molecules]
)
energies

# %%
times = pd.DataFrame(
    index=[molec.stoich() for molec in molecules]
)
times

# %%
for basis in basissets: 
    energy = []
    t = []
    for molec in molecules: 
        start = time.time()
        bfs = basisset(molec, basis)
        solver = rohf(molec, bfs) if molec == oh else rhf(molec, bfs)
        energy += [solver.converge()[-1]]
        t += [time.time() - start]
    energies[basis] = energy
    times[basis] = t

# %%
energies
# %%
times

# %%
