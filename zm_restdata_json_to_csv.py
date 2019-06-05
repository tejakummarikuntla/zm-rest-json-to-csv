import os
import requests
import logging
from io import StringIO
import urllib.request 
import requests

from pandas.io.json import json_normalize 
from datetime import datetime
from time import time

zmRootEndpoint = 'https://developers.zomato.com/api/v2.1'
zmApiToken = ''

getSearchDetails = '/search?entity_id={eId}&entity_type={city}&q={q}&lat={lat}&lon={lon}&radius={rad}'

getChennaiURL = zmRootEndpoint + getSearchDetails.format(eId = 7,
                                                      city = 'city',
                                                      q = 'chennai',
                                                      lat = 13.067439,
                                                      lon = 80.237617,
                                                      rad = 30000)

zmChennaiResponse = requests.get(getChennaiURL,\
                                headers = {'user-key':zmApiToken}
                                ).json()
chnDf = json_normalize(zmChennaiResponse['restaurants'])
reqColumnFilter = ['restaurant.R.res_id',
                   'restaurant.name',
                   'restaurant.cuisines',
                   'restaurant.average_cost_for_two',
                   'restaurant.location.locality',
                   'restaurant.location.city',
                   'restaurant.location.address',
                   'restaurant.location.latitude',
                   'restaurant.location.longitude',
                   'restaurant.user_rating.aggregate_rating',
                   'restaurant.user_rating.rating_text',
                   'restaurant.menu_url'
                   ]
reqRestData = chnDf[reqColumnFilter]
reqRestData.to_csv('ChennaiRestData.csv',
                  index = False,
                  encoding = 'utf-8')