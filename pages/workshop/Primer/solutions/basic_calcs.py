# The height of the 700 millibar level assuming a standard atmosphere
height_700 = mpcalc.pressure_to_height_std(700 * units.hPa)
print(height_700)

# Windchill of 263K ambient temperature with 20 m/s wind
windchill = mpcalc.windchill(263 * units.kelvin, 20 * units('m/s'))
print(windchill.to('degF'))

# Calculate the dry adiabatic lapse rate
gamma_d = consts.g / consts.Cp_d
print(gamma_d)
