import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

energy = pd.read_csv('Metro_Interstate_Traffic_Volume.csv')
# sns.heatmap(energy.isnull())
# plt.show()
print(energy['rv1'].head())
print(energy.info())