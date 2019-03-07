
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Read the Pharma Sector data 
df = pd.read_csv("C:\Users\Noesys\Desktop\Data-Visualization-using-Seaburn\\Pharma Heatmap data.csv")
print(df.head(10))

# Create an array of stock symbols & their respective percentage price change
symbol = ((np.asarray(df['Symbol'])).reshape(6,5))
perchange = ((np.asarray(df['Change'])).reshape(6,5))

print(symbol)
print(perchange)

# Create a pivot table
result = df.pivot(index='Yrows',columns='Xcols',values='Change')
print(result)

# Create an array to annotate the heatmap
labels = (np.asarray(["{0} \n {1:.2f}".format(symb,value)
                      for symb, value in zip(symbol.flatten(),
                                               perchange.flatten())])
         ).reshape(6,5)

# Define the plot
fig, ax = plt.subplots(figsize=(13,7))

# Add title to the Heat map
title = "Pharma Sector Heat Map"

# Set the font size and the distance of the title from the plot
plt.title(title,fontsize=18)
ttl = ax.title
ttl.set_position([0.5,1.05])

# Hide ticks for X & Y axis
ax.set_xticks([]) 
ax.set_yticks([]) 

# Remove the axes
ax.axis('off')

# Use the heatmap function from the seaborn package
sns.heatmap(result,annot=labels,fmt="",cmap='RdYlGn',linewidths=0.30,ax=ax)

# Display the Pharma Sector Heatmap
plt.show()


