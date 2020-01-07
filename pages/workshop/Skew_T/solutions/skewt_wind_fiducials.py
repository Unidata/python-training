# Plot wind barbs
my_skew.plot_barbs(my_sounding['pressure'], my_sounding['u_wind'], my_sounding['v_wind'])

# Add dry adiabats
my_skew.plot_dry_adiabats()

# Add moist adiabats
my_skew.plot_moist_adiabats()

# Add mixing ratio lines
my_skew.plot_mixing_lines()

# Redisplay figure
my_fig
