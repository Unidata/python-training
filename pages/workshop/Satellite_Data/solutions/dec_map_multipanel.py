#
# Get the data
#

# Get the data for band 7
url = ('https://thredds.ucar.edu/thredds/catalog/satellite/goes/east/products/'
            f'CloudAndMoistureImagery/{region}/Channel07/'
            f'{datetime.utcnow():%Y%m%d}/catalog.xml')
cat = TDSCatalog(url)
band_7 = cat.datasets[-2].remote_access(use_xarray=True)

# Get the data for band 10
url = ('https://thredds.ucar.edu/thredds/catalog/satellite/goes/east/products/'
            f'CloudAndMoistureImagery/{region}/Channel10/'
            f'{datetime.utcnow():%Y%m%d}/catalog.xml')
cat = TDSCatalog(url)
band_10 = cat.datasets[-2].remote_access(use_xarray=True)

#
# Make the plot
#
band_7_img = ImagePlot()
band_7_img.data = band_7
band_7_img.field = 'Sectorized_CMI'
band_7_img.colormap = 'ir_rgbv'

band_10_img = ImagePlot()
band_10_img.data = band_10
band_10_img.field = 'Sectorized_CMI'
band_10_img.colormap = 'WVCIMSS'

left_panel = MapPanel()
left_panel.plots = [band_7_img]
left_panel.title = 'IR - GOES EAST'
left_panel.layout = (1, 2, 1)

right_panel = MapPanel()
right_panel.plots = [band_10_img]
right_panel.title = 'Mid-Level Water Vapor - GOES EAST'
right_panel.layout = (1, 2, 2)

pc = PanelContainer()
pc.panels = [left_panel, right_panel]
pc.size = (12, 10)

pc.show()
