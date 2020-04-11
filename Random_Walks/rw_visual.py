import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Make a random walk, and plot the points.
while True:
    rw = RandomWalk(50000)
    rw.fill_walk()

    # Set the size of the plotting window.
    plt.figure(figsize=(10,6))

    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values,rw.y_values,c=point_numbers,cmap=plt.cm.Blues,edgecolors='none',s=1)

    # Emphasize the first and last points.
    plt.scatter(0,0,c='green',edgecolors='none',s=100)
    plt.scatter(rw.x_values[-1],rw.y_values[-1],c='red',edgecolors='none',s=100)

    # Remove the axes
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)


    plt.savefig("Graphs_and_Images/Random_walk_no_axes_50000.png",bbox_inches="tight")
    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break