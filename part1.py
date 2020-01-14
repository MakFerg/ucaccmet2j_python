import json
with open('precipitation.json', encoding = 'utf8') as file:
    precipitation_data = json.load(file)

total_precipitation = 0 
for measurement in precipitation_data:
    if measurement['station'] == 'GHCND:US1WAKG0038':
        total_precipitation += measurement['value']
print(total_precipitation)       
#     if measurement["date"] == "2010-01":
        
#         print(measurement)

    



#         for line in Seattle_meas:
# #             total = total + measurement['value']
# print(total)       


# with open('precipitation.json', 'w', encoding = 'utf8') as file:
#     json.dump()