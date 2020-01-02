# Make a figure
my_fig = plt.figure(figsize=(10, 10))

# Make a SkewT object
my_skew = SkewT(my_fig)

# Plot the temperature and dewpoint
my_skew.plot(my_sounding['pressure'], my_sounding['temperature'], linewidth=2, color='tab:red')
my_skew.plot(my_sounding['pressure'], my_sounding['dewpoint'], linewidth=2, color='tab:blue')
