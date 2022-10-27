# Your code to create majestic plots goes in here!
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

iris = pd.read_csv('iris.data', header=None)
iris.columns = ['sepal_width','sepal_length','petal_width','petal_length','species']

measurement_names = ['sepal_width','sepal_length','petal_width','petal_length']
plt.boxplot(iris[measurement_names],labels=measurement_names)
plt.ylabel('cm')
plt.savefig('iris_boxplot.png')

plt.clf()

for species_name in set(iris['species']):
    iris_subset = iris[iris['species'] == species_name]
    plt.scatter(iris_subset['sepal_length'], iris_subset['sepal_width'],label=species_name, s=10)
plt.legend()
plt.xlabel('petal_length')
plt.ylabel('petal_width')
plt.savefig('iris_scatterplot.png')

plt.clf()

fig, axes = plt.subplots(1,2)
fig.set_size_inches(10,5)

# left scatter plot
axes[0].boxplot(iris[measurement_names],labels=measurement_names)
axes[0].set_ylabel('cm')

# right boxplot
for species_name in set(iris['species']):
    iris_subset = iris[iris['species'] == species_name]
    axes[1].scatter(iris_subset['sepal_length'], iris_subset['sepal_width'],label=species_name, s=10)
axes[1].legend()
axes[1].set_xlabel('petal_length')
axes[1].set_ylabel('petal_width')

axes[0].spines['top'].set_visible(False)
axes[0].spines['right'].set_visible(False)
axes[0].spines['bottom'].set_visible(True)
axes[0].spines['left'].set_visible(True)

axes[1].spines['top'].set_visible(False)
axes[1].spines['right'].set_visible(False)
axes[1].spines['bottom'].set_visible(True)
axes[1].spines['left'].set_visible(True)

plt.savefig('multi_panel_figure.png')