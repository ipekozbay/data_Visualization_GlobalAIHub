import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

sns.set(rc={'figure.figsize':(5,5)})
df = pd.read_csv('world-happiness-report.csv')
df.head(10) 

df.info()
df['Country name'].value_counts()

from os import mkdir

try:
  mkdir('Plots')
except:
  pass  

mypath='Plots'  

f, axes = plt.subplots(5, 2, figsize=(20, 30))
f.tight_layout(pad=8)
f.suptitle('box plots')
cols = df.select_dtypes(exclude='object').columns

x_axes = 0
y_axes = 0

for col in cols:
  sns.boxplot(data=df, x=col, ax=axes[x_axes,y_axes])
  if y_axes == 1:
    y_axes = 0
    x_axes +=1
  else:
    y_axes+=1  

plt.savefig('Plots/box_plots.png')
plt.show()    

year_group = df.groupby(by='year').sum()

year_group['Positive affect'].plot()
plt.savefig('Plots/positive_affect_plot.png')

year_group['Negative affect'].plot()
plt.savefig('Plots/Negative_affect_plot.png')

ax1= sns.barplot(x=year_group.index, y=year_group['Social support'].values)
ax1.tick_params(axis='x',rotation=90)
plt.savefig('Plots/socailSupport.png')

sns.set(rc={'figure.figsize':(15,10)})
plt.title('correlation matrix')
sns.heatmap(df.corr(), annot=True)
plt.savefig('Plots/correlation_matrix.png')

sns.jointplot(data=df, x='year', y='Social support')
sns.jointplot(data=df, x='Life Ladder', y='Social support')
plt.savefig('Plots/jointplots.png')

import os
from os import listdir, mkdir

all_files=os.listdir('Plots')
reports=[f'Plots/{file}'for file in all_files]

!pip install FPDF

from fpdf import FPDF

WIDTH=210
HEIGHT = 297

pdf= FPDF()
pdf.set_font('Arial','B',24)
pdf.add_page()
pdf.cell(190,20, txt='REPORT',align='C')


for report in reports:
  pdf.add_page()
  pdf.cell(190,20,txt=report,align='C')
  pdf.image(report,5,30,WIDTH-5)

pdf.output('Countiries_report.pdf')  
