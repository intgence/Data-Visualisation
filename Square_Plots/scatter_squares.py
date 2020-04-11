import matplotlib.pyplot as plt

# Plot a single point.
x_values=list(range(1,1001))
y_values = [i**2 for i in x_values]

#plt.scatter(x_values,y_values,c='red',edgecolors='none',s=40)
plt.scatter(x_values,y_values,c=y_values,cmap=plt.cm.Blues,edgecolors='none',s=40)

# Set chart title and label axes.
plt.title("Square Numbers",fontsize = 24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value",fontsize=14)

plt.tick_params(axis='both',which='major',labelsize=14)

#Set the range for each axis
plt.axis([0,1100,0,1100000])

plt.savefig('Graphs_and_Images/squares_plot.png', bbox_inches='tight')
plt.show()

