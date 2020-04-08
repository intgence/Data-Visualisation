import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Make a random walk, and plot the points.
while True:
    rw = RandomWalk()
    rw.fill_walk()

    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values,rw.y_values,c=point_numbers,cmap=plt.cm.Blues,edgecolors='none',s=15)
    plt.savefig("Random Walks/Random_walk_cmap.png",bbox_inches="tight")
    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break