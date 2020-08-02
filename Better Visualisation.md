<a href ="https://towardsdatascience.com/sorry-but-sns-distplot-just-isnt-good-enough-this-is-though-ef2ddbf28078"> Medium Article </a>
-  First step to develop a great visual is the get the wireframe ready
- Break apart the plots using FacetGrid

Interesting way to obtain visualisation

```py
import pandas as pd
import numpy as np
from scipy.stats import norm
import seaborn as sns
import matplotlib.pyplot as plt

DF = pd.DataFrame({'Dis':norm.rvs(size=10000,loc=1500,scale=300)})

DF.loc[:2499,'C'] = 'A'
DF.loc[2500:4999,'C'] = 'B'
DF.loc[5000:7499,'C'] = 'C'
DF.loc[7500:9999,'C'] = 'D'

g = sns.FacetGrid(DF, # Dataframe to pull from
row="C", # Define the column to be differentiated for 
hue="C",
aspect=10,
height=1.5,
palette=['#4285F4','#EA4335','#FBBC05','#34A853'])

g.map(sns.kdeplot, "Dis",shade=True, alpha=1, lw=1.5, bw=0.2)
g.map(sns.kdeplot, "Dis", lw=4, bw=0.2)
g.map(plt.axhline, y=0, lw =4)

def label(x, color, label):
    ax = plt.gca() #get the axes of the current object
    ax.text(0, .2, #location of text
            label, #text label
            fontweight="bold", color=color, size=20, #text attributes
            ha="left", va="center", #alignment specifications
            transform=ax.transAxes) #specify axes of transformation


g.map(label,"Dis")

sns.set(style="white", rc={"axes.facecolor": (0, 0, 0, 0)})
g.fig.subplots_adjust(hspace= -0.05)

g.set_titles("") #set title to blank
g.set(yticks=[]) #set y ticks to blank
g.despine(bottom=True, left=True) #remove 'spines'
```
