import pygal

wm = pygal.maps.world.World()
wm.title = 'Populations of countries in North America'
wm.add('North America', {'ca': 34126000, 'us': 309349000, 'mx': 113423000})

wm.render_to_file('Graphs_and_Images/na_pop.svg')
