"""LAMBDA_ - a collective of data science hleper functions"""

import pandas as import pd
import numpy as np

#sample

ONES = pd.DataFrame(np.ones(10))
ZEROS= pd.DataFrame(np.zeros(50))



# sample functions
def increment(x):
    return (x + 1)
