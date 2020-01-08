# define the time range we are interested in
end_time = datetime(2017, 9, 12, 0)
start_time = end_time - timedelta(days=2)

# build the query
query = ncss.query()
query.lonlat_point(-155.1, 19.7)
query.time_range(start_time, end_time)
query.variables('altimeter_setting', 'temperature', 'dewpoint',
                'wind_direction', 'wind_speed')
query.accept('csv')

data = ncss.get_data(query)

df = pd.DataFrame(data)

# Parse the date time stamps
df['time'] = pd.to_datetime(df['time'].str.decode('utf-8'), infer_datetime_format=True)

# Station names are bytes, we need to convert them to strings
df['station'] = df['station'].str.decode('utf-8')

# Make the plot
ax = df.plot(x='time', y=['temperature', 'dewpoint'],
             color=['tab:red', 'tab:green'],
             grid=True,
             figsize=(10,6),
             fontsize=14)

# Set good labels
ax.set_xlabel('Time', fontsize=16)
ax.set_ylabel('DegC', fontsize=16)
ax.set_title(f"{df['station'][0]} {df['time'][0]:%Y/%m/%d}", fontsize=22)

# Improve on the default ticking
locator = AutoDateLocator()
hoursFmt = DateFormatter('%H')
ax.xaxis.set_major_locator(locator)
ax.xaxis.set_major_formatter(hoursFmt)