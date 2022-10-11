latitude = "20-55-70.010N"
longitude = "32-11-50.000W"

##assuming N latitude and W longitude
latitude = sum(float(x) / 60 ** n for n, x in enumerate(latitude[:-1].split('-')))  * (1 if 'N' in latitude[-1] else -1)
longitude = sum(float(x) / 60 ** n for n, x in enumerate(longitude[:-1].split('-'))) * (1 if 'E' in longitude[-1] else -1)