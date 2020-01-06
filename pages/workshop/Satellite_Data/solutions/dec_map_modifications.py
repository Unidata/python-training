# Create the ImagePlot
img = ImagePlot()
img.data = ds
img.field = 'Sectorized_CMI'
img.colormap = 'WVCIMSS'

# Create the MapPanel
panel = MapPanel()
panel.plots = [img]
panel.title = "CONUS GOES-East"

# Create the PanelContainer
pc = PanelContainer()
pc.panels = [panel]
pc.size = (10, 8)

# Show it!
pc.show()
