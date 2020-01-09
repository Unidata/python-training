def make_channel_image_plot(channel):
    url = ('https://thredds.ucar.edu/thredds/catalog/satellite/goes/east/products/'
                f'CloudAndMoistureImagery/{region}/Channel{channel:02d}/'
                f'{datetime.utcnow():%Y%m%d}/catalog.xml')
    cat = TDSCatalog(url)
    band_data = cat.datasets[-2].remote_access(use_xarray=True)
    
    img = ImagePlot()
    img.data = band_data
    img.field = 'Sectorized_CMI'
    return img

#
# Make the plot
#
band_7_img = make_channel_image_plot(7)
band_10_img = make_channel_image_plot(10)

band_7_img.colormap = 'ir_rgbv'
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
