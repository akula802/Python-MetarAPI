# Classes for re-use

# Core library and/or django imports

# 3rd-party imports

# Local app imports

# Load the .env



### NOTE - API DOCS: https://aviationweather.gov/data/api/#/Data/dataMetars ###



############################

class make_faa_api_request:
    def __init__(self, station_id):
        self.station_id = station_id


    def get_metars(self):
        # Needfuls
        import requests
        import urllib3
        import json
        import math

        # Disable SSL warnings - dev laptop has MITM certs that break everything
        urllib3.disable_warnings()

        # Base METAR query URL
        query_url = "https://www.aviationweather.gov/api/data/metar?ids={}".format(self.station_id)

        # Final list to be returned if query is successful
        #faa_response_final = []

        # Initial query parameters
        #header = {'Authorization': 'Bearer {}'.format(self.bearer_token)}

        # Make the initial query
        try:
            faa_response = requests.get(query_url, verify=False)
            #faa_response = requests.get(query_url)

        except Exception as e:
            fail_message = "Failed to make initial request (1.1). Got HTTP response: {}".format(faa_response.status_code)
            return (fail_message, e)

        # Now check the HTTP status code
        # Some requests (e.g. Custom Fields) return '0' on success in the result content
        if faa_response.status_code == 200:
          
            # Return the data
            if faa_response:

                # Convert the XML to JSON or something else we can work with
                #import xml.etree.ElementTree as ET
                #tree = ET.fromstring(faa_response.text)

                # Get the stuff
                #for thing in tree[6][0]:
                #    print(thing.tag, thing.attrib)
                
                # METAR raw text
                faa_metar_raw_text = faa_response.text

                # Station ID
                #faa_station_id = tree[6][0][1].text

                #return (faa_response.status_code, faa_metar_raw_text)
                return faa_metar_raw_text
            else:
                return "what the fuck"


        # Got a 401, unauthorized
        elif faa_response.status_code == 401:
            # Return the code
            fail_message = "Failed to parse initial request (1.1). Got HTTP response: {}".format(faa_response.status_code)
            return (faa_response.status_code, fail_message)


        # Didn't get a 200 or a 401, so wtf
        else:
            fail_message = "Failed to parse initial request (1.2). Got HTTP response: {}".format(faa_response.status_code)
            return (faa_response.status_code, fail_message)

##########################



