import urllib3
import json


def getWeatherUpdate():
    city_name = input("Enter City Name :")
    http = urllib3.PoolManager()
    req_string = r'https://www.metaweather.com/api/location/search/?query='+city_name
    req = http.request('GET', req_string)
    print(req.status)
    if req.status == 200:
       city_detail = json.loads(req.data)
       if len(city_detail) > 0:
        lat_lon = city_detail[0]['latt_long']
        req_string = 'https://www.metaweather.com/api/location/search/?lattlong=' + lat_lon
        req = http.request('GET', req_string)
        if req.status == 200:
            locations = json.loads(req.data)
            for location in locations:
                woeid = location['woeid']
                api_end_pt = 'https://www.metaweather.com/api/location/'+str(woeid)+'/'
                req = http.request('GET', api_end_pt)
                if req.status == 200:
                    weather_details = json.loads(req.data)
                    for weather_detail in weather_details['consolidated_weather']:
                        print(weather_detail)
                        print(weather_detail['min_temp'])

                else:
                    print("Error using API.")






       else:
           print(r"City "+ city_name +" you enetered is not available")







if __name__ == "__main__":
    getWeatherUpdate()
