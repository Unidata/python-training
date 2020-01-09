# Set up an NCSS query from thredds using siphon
query = ncss.query()
query.accept('netcdf4')
query.variables('Temperature_isobaric', 'Geopotential_height_isobaric')
query.vertical_level(50000)
now = datetime.utcnow()
query.time_range(now, now + timedelta(days=1))
query.lonlat_box(west=-110, east=-45, north=50, south=10)

# Download data using NCSS and create Data Array
data = ncss.get_data(query)
ds = xr.open_dataset(NetCDF4DataStore(data))

# Get the first time step as a datetime
plot_time = now + timedelta(hours=12)

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

# Create the map panel and add the plot to it
panel = MapPanel()
panel.plots = [tmp_img, geopot_cnt]
panel.layers = ['coastline', 'borders', 'states']
panel.title = plot_time.strftime('%Y-%m-%d at %H:%MZ')

# Create a panel container and add the panel to it
pc = PanelContainer()
pc.panels = [panel]
pc.size = (10, 8)
pc.show()
