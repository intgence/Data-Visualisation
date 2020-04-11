import pygal
from die import Die

# Create two D6 dice.
die = Die()

# Make some rolls, and store results in a list.
results = [die.roll() for roll_num in range(1000)]
#for roll_num in range(1000):
#    results.append(die.roll())

# Analyze the results.
frequencies = [results.count(value) for value in range(1,die.num_sides+1)]
#for value in range(1,die.num_sides+1):
#    frequencies.append(results.count(value))

# Visualize the results.
hist = pygal.Bar()

hist.title = "Results of rolling a die 1000 times"
hist.x_labels = [str(i) for i in range(1,6)]
hist.x_title = "Result"
hist.y_title = 'Frequency of Result'

hist.add('D6', frequencies)
hist.render_to_file('Graphs_and_Images/die_1000.svg')

# print(frequencies)