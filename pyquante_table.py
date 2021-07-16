# %%
from pyquante2 import molecule,rhf,uhf,rohf,h2,h2o,lih,oh,co,ch4,he,basisset
import pandas as pd
import time

# %%
basissets = ['sto3g', '6-31g', '6-31g**']
molecules = {'h2': h2, 
             'he': he,
             'lih': lih, 
             'oh': oh, 
             'h2o': h2o,
             'ch4': ch4, 
             'co': co}
basis_mol = [[i, j] for i in basissets for j in molecules.keys()]
data = pd.DataFrame(basis_mol, columns=['basisset', 'molecule'])

# %%
for key, value in molecules.items():
    print(f"{key:3} | name: {value.name:10} mult: {value.multiplicity}")

# %%
energy = []
t = []
for index, contents in data.iterrows():
    start_time = time.time()
    molec = molecules[contents['molecule']]
    bfs = basisset(molec, contents['basisset'])
    solver = rohf(molec, bfs) if molec.multiplicity > 1 else rhf(molec, bfs)
    energy += [solver.converge()[-1]]
    t += [time.time() - start_time]
data['energy'] = pd.Series(energy)
data['t'] = pd.Series(t)

# %%
data.pivot(index='molecule', columns='basisset', values='energy')

# %%
data.pivot(index='molecule', columns='basisset', values='t')

# %%
