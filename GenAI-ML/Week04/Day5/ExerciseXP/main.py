"""
GenAI-ML / Week04 / Day5 / ExerciseXP

Instructions:
- Write your solution below.
- Add tests in a __main__ block.
"""
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

sns.set_theme(style='whitegrid')
plt.rcParams.update({'figure.dpi': 130, 'font.size': 11})

df = pd.read_excel(
    r"C:\Users\admin\Documents\GitHub\DI\GenAI-ML\Week04\Day5\ExerciseXP\US Superstore data.xls",
    engine='xlrd'
)




print(f"Rows: {len(df):,}   /   Columns: {df.shape[1]}")
df.head()

def main():
    pass

if __name__ == "__main__":
    main()
