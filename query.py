import requests
import json
import os
from dotenv import load_dotenv

class query:

    def __init__(self): 
        load_dotenv()
        self.API_KEY = os.getenv('PROJECT_API_KEY')
        self.zip_code

        #self.lat, self.long = self.requests()

        #self.lat = 29.8833
        #self.long = 97.9414

    def get_zip_code(self, zip):
        self.zip_code = zip

    def requests(self):
        parse_json = requests.get(f'https://www.airnowapi.org/aq/forecast/zipCode/?format=application/json&zipCode={self.zip_code}&date=&distance=25&API_KEY={self.API_KEY}')
        json_list = json.loads(parse_json.text)
        lat = json_list[0]['Latitude']
        long = json_list[0]['Longitude']
        return lat, long
    
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
