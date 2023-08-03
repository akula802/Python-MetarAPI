# Main app

# Core library and/or django imports
#import requests

# 3rd-party imports

# Local app imports
import pymetar_classes

# Load the .env


# Action
print('Starting...')
faa_request_object = pymetar_classes.make_faa_api_request('KBJC')
faa_request_result = faa_request_object.request_result_all()
print(faa_request_result)
print('End')
