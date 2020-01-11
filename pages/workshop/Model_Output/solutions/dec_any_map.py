# Set up access via NCSS
gfs_catalog = ('http://thredds.ucar.edu/thredds/catalog/grib/NCEP/GFS/'
               'Global_0p5deg/catalog.xml?dataset=grib/NCEP/GFS/Global_0p5deg/Best')
cat = TDSCatalog(gfs_catalog)
ncss = cat.datasets[0].subset()

# Set up an NCSS query from thredds using siphon
query = ncss.query()
query.accept('netcdf4')
query.variables('Temperature_surface', 'Geopotential_height_surface')
now = datetime.utcnow()
query.time_range(now, now + timedelta(days=1))
query.lonlat_box(west=-110, east=-45, north=50, south=10)

# Download data using NCSS and create Data Array
data = ncss.get_data(query)
ds = xr.open_dataset(NetCDF4DataStore(data))

# Create the desired plot time
plot_time = now + timedelta(hours=24)

# Make temperature contour plot
temps_cnt = ContourPlot()
temps_cnt.data = ds
temps_cnt.field = 'Temperature_surface'
temps_cnt.linecolor = 'tab:red'
temps_cnt.linestyle = '--'
temps_cnt.time = plot_time
temps_cnt.clabels = True

# Make height contour plot
heights_cnt = ContourPlot()
heights_cnt.data = ds
heights_cnt.field = 'Geopotential_height_surface'
heights_cnt.time = plot_time
heights_cnt.clabels = True

# Create the map panel and add the plot to it
panel = MapPanel()
panel.plots = [temps_cnt, heights_cnt]
panel.layers = ['coastline', 'borders', 'states']
panel.title = plot_time.strftime('%Y-%m-%d at %H:%MZ')
panel.area = 'ma'

# Create a panel container and add the panel to it
pc = PanelContainer()
pc.panels = [panel]
pc.size = (10, 8)
pc.show()
