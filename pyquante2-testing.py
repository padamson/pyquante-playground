# %%
import pyquante2

# %%
print(pyquante2.h2o)

# %%
str(pyquante2.h2o)
# %%
repr(pyquante2.h2o)
# %%
from pyquante2 import molecule,rhf,uhf,rohf,h2,h2o,lih,basisset

bfs = basisset(h2,'sto3g')
bfs
# %%
solver = rhf(h2,bfs)
solver

# z axis in chart is the average distance in bohrs (from angstroms)
# %%
ens = solver.converge()
ens

# %%
