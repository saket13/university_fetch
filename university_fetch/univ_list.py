from datetime import datetime
import os 
import requests
import math

API_URL = ('http://universities.hipolabs.com/search?country={}')

def query_api(country):    
    try:        
        #print(API_URL.format(country))        
        data = requests.get(API_URL.format(country)).json()
        return data    
    except Exception as exc:        
        print(exc)        
        data = None    
    
