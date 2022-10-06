import requests
import json
import csv
import urllib.request
import os
from dotenv import load_dotenv

class query:

    def __init__(self): 
        self.url = 'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/92056/2022-10-05/2022-10-12?unitGroup=us&elements=datetime%2CdatetimeEpoch%2Cname%2Ctemp%2Csunrise%2Csunset%2Cmoonphase%2Cconditions%2Cdescription%2Cicon&include=days%2Chours&key=PK44XXYLALVRT4LUY2WVUTEZZ&contentType=json'
        self.url2 = 'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/92056/2022-10-05/2022-10-12?unitGroup=us&elements=datetime%2Cname%2Ctemp%2Csunrise%2Csunset%2Cmoonphase%2Cconditions%2Cdescription%2Cicon&include=days%2Chours&key=PK44XXYLALVRT4LUY2WVUTEZZ&contentType=json'
        self.url3 = 'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/92056/2022-10-05/2022-10-12?unitGroup=us&elements=datetime%2Cname%2Ctemp%2Cdescription%2Cicon&include=days%2Chours&key=PK44XXYLALVRT4LUY2WVUTEZZ&contentType=json'
        self.url4 = 'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/92056/2022-10-05/2022-10-12?unitGroup=us&elements=datetime%2Cname%2Caddress%2Ctemp%2Cdescription%2Cicon&include=days%2Chours&key=PK44XXYLALVRT4LUY2WVUTEZZ&contentType=json'
        #self.new_url = self.url3 = 'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/92056/2022-10-05/2022-10-12?unitGroup=us&elements=datetime%2Cname%2Ctemp%2Cdescription%2Cicon&include=days%2Chours&key=PK44XXYLALVRT4LUY2WVUTEZZ&contentType=json'
        load_dotenv()
        self.API_KEY = os.getenv('PROJECT_API_KEY')
        self.zip_code = None
        self.lat = None
        self.long = None
        self.current_data = None
        self.weekly_data = None
        #self.zip_code

        #self.lat, self.long = self.requests()

        #self.lat = 29.8833
        #self.long = 97.9414

    def set_zip_code(self, zip):
        self.zip_code = zip

    def requests(self):
        parse_json = requests.get(f'https://www.airnowapi.org/aq/forecast/zipCode/?format=application/json&zipCode={self.zip_code}&date=&distance=25&API_KEY={self.API_KEY}')
        json_list = json.loads(parse_json.text)
        try:
            self.lat = json_list[0]['Latitude']
            self.long = json_list[0]['Longitude']
        except IndexError:
            self.lat = 29.8833
            self.long = 97.9414  
        
    def test_query(self): 
        '''
        self.weekly_data holds 8 days of weather forecast data 
        weekly_data[0] gives data for 1st day
        weekly_data[i] gives data for ith day
        ''' 
        current_data = []
        weekly_data = [] 
        placeholder = []
        data = requests.get(self.url3)
        parse_data = json.loads(data.text)
        
        for x in range(0,8):
            if x == 0:
                    current_data.append(parse_data['days'][x]['datetime'])
                    current_data.append(parse_data['days'][x]['temp'])
                    current_data.append(parse_data['days'][x]['icon']) 
                    #print(day)
                    pass
            daily = parse_data['days'][x]['hours']
            placeholder = [parse_data['days'][x]['datetime']]
            #print(placeholder)
            #weather_data_per_day.append(data_j['days'][x]['datetime'])
            #print(data_j['days'][x]['datetime'])
            for day in daily:
                    #save info for that day
                #print(j)
                placeholder.append(day)
            weekly_data.append(placeholder)
        print(current_data)
        #print(parse_data['days'][0]['datetime'])
        #print(parse_data['days'][0]['temp'])
        #print(parse_data['days'][0]['icon'])
        #print(parse_data['days'])
            #weekly_data.append(weather_data_per_day)
        #print(len(weekly_data))
        #print(weekly_data[0])
        #print(weekly_data)
            #print(data_j['days'][x]['hours'])
        #x = 0
        #for item in data_j['days']:
            #print(item[x])
            #print(x)
            #print(item)
            #x = x + 1
        #try_this = data_j['days'][7]['hours'] 
        #print(try_this) 
        
        #print(try_this)
        '''
        try: 
            ResultBytes = urllib.request.urlopen("https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/92056?unitGroup=us&key=PK44XXYLALVRT4LUY2WVUTEZZ&contentType=json")
            # Parse the results as CSV
            CSVText = csv.reader(codecs.iterdecode(ResultBytes, 'utf-8'))
            # Parse the results as JSON
            jsonData = json.loads(ResultBytes.decode('utf-8'))
        except urllib.error.HTTPError  as e:
            ErrorInfo= e.read().decode() 
            print('Error code: ', e.code, ErrorInfo)
            exit()
        except  urllib.error.URLError as e:
            ErrorInfo= e.read().decode() 
            print('Error code: ', e.code,ErrorInfo)
            exit()
        '''
    
    def print_info(self):
        print(self.lat)
        print(self.long)

        
    
    def request(self, api_key):
        requests.get(f'https://www.airnowapi.org/aq/forecast/zipCode/?format=application/json&zipCode=92056&date=&distance=25&API_KEY={api_key}')
    
    #def set_link()
'''
def query():
    link = 'https://www.airnowapi.org/aq/forecast/zipCode/?format=application/json&zipCode=92056&date=&distance=25&API_KEY=1BACE227-E15E-4375-B536-9593E34F7261'
    data = requests.get(link)
    data_r = json.loads(data.text)
    #for item in data_r:
        #for i in item['DateIssue']:
            #print(i)
        #print(item)
    lat = data_r[0]['Latitude']
    long = data_r[0]['Longitude']
    print(data_r[0]['Latitude'])
    #print(data_r)
    #print(type(data_r))
    #print(data_r[0][0])

    

def greeting():

    print("YO this works")
    '''
