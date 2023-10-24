# Main app

# Core library and/or django imports
#import requests

# 3rd-party imports

# Local app imports
import pymetar_classes

# Load the .env


# Action
print('\nStarting...\n')
faa_request_object = pymetar_classes.make_faa_api_request('KBJC,KEIK,KLMO,KFNL,KGXY,KDEN,KAPA')
faa_request_result = faa_request_object.get_metars()
print(faa_request_result)
print('End\n')
