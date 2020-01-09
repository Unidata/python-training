# Solution from above in case you had trouble
date = datetime.utcnow() - timedelta(days=1)
cat = TDSCatalog(f'https://thredds.ucar.edu/thredds/catalog/nexrad/level2/KINX/{date:%Y%m%d}/catalog.xml')
request_time = date.replace(hour=12, minute=0, second=0, microsecond=0)
datasets = cat.datasets.filter_time_range(request_time, request_time + timedelta(hours=6))
print(datasets)
