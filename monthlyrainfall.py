import json
with open('precipitation.json', encoding = 'utf8') as file:
    precipitation_data = json.load(file)

months= [0,0,0,0,0,0,0,0,0,0,0,0]
total_precipitation = 0 
for measurement in precipitation_data:
    if measurement['station'] == 'GHCND:US1WAKG0038':
        total_precipitation += measurement['value']
print(total_precipitation)      

for measurement in precipitation_data:
    if measurement['station'] == 'GHCND:US1WAKG0038':
        dateparts = measurement["date"].split(sep='-')
        month_of_this_measurement = dateparts[1] 
        rainfall_of_this_measurement = measurement['value']
        index_for_our_list = int(dateparts[1]) - 1
        months[index_for_our_list] = months[index_for_our_list] + rainfall_of_this_measurement
        print(months)


with open('precipitation_output.json', 'w', encoding = 'utf8') as file:
    json.dump(total_precipitation, file)
