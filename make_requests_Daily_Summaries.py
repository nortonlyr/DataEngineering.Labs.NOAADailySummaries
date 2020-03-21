#For NOAA Daily Summaries lab
import json
import requests


file_counter = 0
offset_counter = 1
token = 'vgExQgdFRrflyczUiJQVHBXBqzMwqpXz'

while file_counter <= 3:
    name = ("daily_summaries_FIPS10003_jan_2018_" + str(file_counter))
    url = 'https://www.ncdc.noaa.gov/cdo-web/api/v2/data?datasetid=\
    GHCND&locationid=FIPS:10003&startdate=2018-01-01&enddate=2018-01-31&limit=1000&offset=' \
    + str(offset_counter)
    header = {"Token": token, 'Content-Type': 'application/json'}
    r = requests.get(url=url, headers=header)
    data = r.json()

    with open('./data/daily_summaries/' + \
              (name + ".json"), 'w') as outfile:
        json.dump(data, outfile)
    file_counter += 1
    offset_counter += 1000
