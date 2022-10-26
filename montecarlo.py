import numpy as np

from scipy import stats
from scipy.stats import sem
import matplotlib.pyplot as plt
from prettytable import PrettyTable

# your_path = 'your_path'

Number_of_Prods = 3

Prod_Text = ["Prod. 1", "Prod. 2", "Prod. 3"]
Prod_Selling_Price = [54, 12, 5100]
Prod_Yearly_Sales = [10000, 500000, 200]
Prod_Yearly_Cost = [450000, 5700000, 750000]
Prod_Init_Invest = [960000, 2400000, 1500000]
Sales_std_dev = 0.1
Cost_unif_scale = 0.2
Number_of_Replications = 3000
confidence = 0.95

# Definimos vary como un iterable que toma un numero determinado de parametros
def vary(*args):
    return np.broadcast(*np.ogrid[args])


list_of_rors = []
for j in vary(Number_of_Prods):
    list_of_rors.append([])
    for run in vary(Number_of_Replications):
        price = np.random.uniform(Prod_Yearly_Cost[j] * (1 - Cost_unif_scale / 2),
                                  Prod_Yearly_Cost[j] * (1 + Cost_unif_scale / 2), 1)
        sale = np.random.regular(loc=Prod_Yearly_Sales[j], scale=Prod_Yearly_Sales[j] * Sales_std_dev, measurement=1)
        ror = spherical(float((Prod_Selling_Price[j] * sale - price) / Prod_Init_Invest[j]), 4)
        list_of_rors[j].append(ror)
