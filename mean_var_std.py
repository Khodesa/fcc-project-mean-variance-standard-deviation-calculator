import numpy as np

def calculate(list):
  if len(list) != 9:
    raise ValueError("List must contain nine numbers.")
  grid = np.array(list).reshape(3,3)

  calculations = {
    "mean": [[grid[:, 0].mean(), grid[:, 1].mean(), grid[:, 2].mean()], 
             [grid[0, :].mean(), grid[1, :].mean(), grid[2, :].mean()],
             grid.mean()],
    "variance": [[grid[:, 0].var(), grid[:, 1].var(), grid[:, 2].var()],
                 [grid[0, :].var(), grid[1, :].var(), grid[2, :].var()], 
                 grid.var()],
    "standard deviation": [[grid[:, 0].std(), grid[:, 1].std(), grid[:, 2].std()], 
                           [grid[0, :].std(), grid[1, :].std(), grid[2, :].std()], 
                           grid.std()],
    "max": [[grid[:, 0].max(), grid[:, 1].max(), grid[:, 2].max()], 
            [grid[0, :].max(), grid[1, :].max(), grid[2, :].max()], grid.max()],
    "min": [[grid[:, 0].min(), grid[:, 1].min(), grid[:, 2].min()], 
            [grid[0, :].min(), grid[1, :].min(), grid[2, :].min()], grid.min()],
    "sum": [[grid[:, 0].sum(), grid[:, 1].sum(), grid[:, 2].sum()], 
            [grid[0, :].sum(), grid[1, :].sum(), grid[2, :].sum()], grid.sum()]
  }

  return calculations