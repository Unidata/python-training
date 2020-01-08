# Make the observation plot
obs = PlotObs()
obs.data = df
obs.time = datetime.utcnow()
obs.level = None
obs.fields = ['air_temperature', 'dew_point_temperature', 'altimeter', 'cloud_coverage']
obs.locations = ['NW', 'SW', 'NE', 'C']
obs.colors = ['tab:red', 'tab:green', 'black', 'black']
obs.formats = [None, None, lambda v: format(10 * v, '.0f')[-3:], 'sky_cover']
obs.vector_field = ['eastward_wind', 'northward_wind']
obs.reduce_points = 1

# Make the map panel
panel = MapPanel()
panel.area = 'fl'
panel.projection = ccrs.PlateCarree()
panel.layers = ['coastline', 'borders', 'states']
panel.plots = [obs]
panel.title = f'Surface Observations {datetime.utcnow():%Y-%m-%d}'

# Make the panel container
pc = PanelContainer()
pc.size = (10, 10)
pc.panels = [panel]

# Show the plot
pc.show()
