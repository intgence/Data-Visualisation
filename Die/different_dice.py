from die import Die

import pygal

# Create a D6 and a D10.
die_1 = Die()
die_2 = Die(10)

# Make some rolls and store results in a list.
results = [die_1.roll() +die_2.roll() for roll_num in range(50000)]

# Analyze the results.
max_result = die_1.num_sides + die_2.num_sides
frequencies = [results.count(value) for value in range(2,max_result+1)]

# Visualize the results.
hist = pygal.Bar()

hist._title = "Results of rolling a D6 and a D10 50,000 times"
hist.x_labels = [str(i) for i in range(2,17)]
hist._x_title = 'Result'
hist._y_title = 'Frequency of Result'

hist.add('D6 + D10', frequencies)
hist.render_to_file('Graphs_and_Images/dif_dice.svg')
