# Make a temperature image plot
tmp_img = ImagePlot()
tmp_img.data = ds
tmp_img.field = 'Temperature_isobaric'
tmp_img.level = 500 * units.hPa
tmp_img.time = plot_time
tmp_img.colormap = 'coolwarm'
tmp_img.colorbar = 'horizontal'

# Make geopotential contour plot
geopot_cnt = ContourPlot()
geopot_cnt.data = ds
geopot_cnt.field = 'Geopotential_height_isobaric'
geopot_cnt.level = 500 * units.hPa
geopot_cnt.time = plot_time

# Add wind barbs
barbs = BarbPlot()
barbs.data = ds
barbs.level = 500 * units.hPa
barbs.time = plot_time
barbs.field = ('u-component_of_wind_isobaric', 'v-component_of_wind_isobaric')
barbs.skip = (5, 5)

# Create the map panel and add the plot to it
panel = MapPanel()
panel.plots = [tmp_img, geopot_cnt, barbs]
panel.layers = ['coastline', 'borders', 'states']
panel.title = plot_time.strftime('%Y-%m-%d at %H:%MZ')
panel.area = (-110, -45, 50, 10)

# Create a panel container and add the panel to it
pc = PanelContainer()
pc.panels = [panel]
pc.size = (10, 8)
pc.show()
